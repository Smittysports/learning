#!/usr/bin/env python

""" Example usage
Perform a ReadProperty for the ‘presentValue’ of an Analog Input:
py AWS/AWS_ReadProperty.py --ini BACpypesClient.ini 599 10.169.94.127 analogInput 1 presentValue

Perform a ReadProperty of the BTF for the ‘objectName’ of a Network Port:
py AWS/AWS_ReadProperty.py --ini BACpypesClient.ini 4194302 10.169.94.208 networkPort 1 objectName

Perform a ReadProperty of the RP for the ‘objectName’ of a Network Port:
py AWS/AWS_ReadProperty.py --ini BACpypesClient.ini 94128 10.169.94.128 networkPort 64040 objectName

"""
from collections import deque

from bacpypes.debugging import bacpypes_debugging, ModuleLogger
from bacpypes.consolelogging import ConfigArgumentParser

from bacpypes.core import run, deferred, stop
from bacpypes.iocb import IOCB

from bacpypes.primitivedata import ObjectIdentifier, CharacterString, Unsigned
from bacpypes.constructeddata import ArrayOf

from bacpypes.pdu import Address
from bacpypes.apdu import ReadPropertyRequest, ReadPropertyACK

from bacpypes.app import BIPSimpleApplication
from bacpypes.local.device import LocalDeviceObject
from bacpypes.object import get_object_class, get_datatype
from bacpypes.constructeddata import Array

# globals
this_device = None
this_application = None

# convenience definition
ArrayOfObjectIdentifier = ArrayOf(ObjectIdentifier)

#
#   ObjectListContext
#

class ObjectListContext:

    def __init__(self, device_id, device_addr):
        self.device_id = device_id
        self.device_addr = device_addr

        self.object_list = []
        self.object_names = []

        self._object_list_queue = None

    def completed(self, had_error=None):
        if had_error:
            print("had error: %r" % (had_error,))
        else:
            for objid, objname in zip(self.object_list, self.object_names):
                print("%s: %s" % (objid, objname))

        stop()

@bacpypes_debugging
class ReadPropertyApplication(BIPSimpleApplication):

    def __init__(self, *args):
        BIPSimpleApplication.__init__(self, *args)

    def read_property_value(self, device_id, device_addr, object_type, object_id, property_id):
        # create a context to hold the results
        context = ObjectListContext(device_id, device_addr)

        # build a request for the object name
        
        if (property_id == 'objectList'):
            request = ReadPropertyRequest(
                destination=context.device_addr,
                objectIdentifier=context.device_id,
                propertyIdentifier='objectList',
                )
        else:
            request = ReadPropertyRequest(
                destination=context.device_addr,
                objectIdentifier=(object_type, object_id),
                propertyIdentifier=property_id,
                )

        # make an IOCB, reference the context
        iocb = IOCB(request)
        iocb.context = context

        # let us know when its complete
        if (property_id == 'objectList'):
            iocb.add_callback(self.object_list_results)
        else:
            iocb.add_callback(self.object_property_results)

        # give it to the application
        self.request_io(iocb)

    
    def object_list_results(self, iocb):
        """ Used for reading the object list
        """
        # extract the context
        context = iocb.context

        # do something for error/reject/abort
        if iocb.ioError:
            context.completed(iocb.ioError)
            return

        # do something for success
        apdu = iocb.ioResponse

        # should be an ack
        if not isinstance(apdu, ReadPropertyACK):
            context.completed(RuntimeError("read property ack expected"))
            return

        # pull out the content
        object_list = apdu.propertyValue.cast_out(ArrayOfObjectIdentifier)

        # store it in the context
        context.object_list = object_list

        # make a queue of the identifiers to read, start reading them
        context._object_list_queue = deque(object_list)
        deferred(self.read_next_object, context)

    def read_next_object(self, context):
        """ Used for reading the object list
        """
        # if there's nothing more to do, we're done
        if not context._object_list_queue:
            context.completed()
            return

        # pop off the next object identifier
        object_id = context._object_list_queue.popleft()

        # build a request for the object name
        request = ReadPropertyRequest(
            destination=context.device_addr,
            objectIdentifier=object_id,
            propertyIdentifier='objectName',
            )

        # make an IOCB, reference the context
        iocb = IOCB(request)
        iocb.context = context

        # let us know when its complete
        iocb.add_callback(self.object_name_results)

        # give it to the application
        self.request_io(iocb)

    def object_name_results(self, iocb):
        """ Used for reading the object list
        """
        # extract the context
        context = iocb.context

        # do something for error/reject/abort
        if iocb.ioError:
            context.completed(iocb.ioError)
            return

        # do something for success
        apdu = iocb.ioResponse

        # should be an ack
        if not isinstance(apdu, ReadPropertyACK):
            context.completed(RuntimeError("read property ack expected"))
            return

        # pull out the name
        object_name = apdu.propertyValue.cast_out(CharacterString)

        # store it in the context
        context.object_names.append(object_name)

        # read the next one
        deferred(self.read_next_object, context)

    def object_property_results(self, iocb):
        """ Used for reading all other properties other than the object list
        TODO: Update this to work with all properties
        """
        # extract the context
        context = iocb.context

        # do something for error/reject/abort
        if iocb.ioError:
            context.completed(iocb.ioError)
            return

        elif iocb.ioResponse:
            apdu = iocb.ioResponse
            # should be an ack
            if not isinstance(apdu, ReadPropertyACK):
                print("    - not an ack")
                context.completed()
                return

            print("apdu.objectIdentifier[0] =", apdu.objectIdentifier[0])
            print("apdu.propertyIdentifier =", apdu.propertyIdentifier)
            # find the datatype
            datatype = get_datatype(
                apdu.objectIdentifier[0], apdu.propertyIdentifier
            )
            print("    - datatype: ", datatype)
            if not datatype:
                # TODO: Fix this, since some properties are not being found by get_datatype
                #value = apdu.propertyValue.cast_out(Unsigned)
                #value = apdu.propertyValue.cast_out(CharacterString)
                #print("Value = ", value)
                print("unknown datatype")
                context.completed()
                return

            # special case for array parts, others are managed by cast_out
            if issubclass(datatype, Array) and (
                apdu.propertyArrayIndex is not None
            ):
                if apdu.propertyArrayIndex == 0:
                    value = apdu.propertyValue.cast_out(Unsigned)
                else:
                    value = apdu.propertyValue.cast_out(datatype.subtype)
            else:
                value = apdu.propertyValue.cast_out(datatype)
            print("    - value: ", value)
            context.completed()
            stop()

        # do something with nothing?
        else:
            print("    - ioError or ioResponse expected")

#
#   __main__
#

def readProperty(server_addr, device_id, device_addr, object_type, object_id, property_id):
    """
    This function will be used to perform a ReadProperty from another script.
    Ex... The AWS_Client.py script will call this in order to perform a ReadProperty.

    TODO: Get the LocalDeviceObject to work without having to utilize an ini file. I may
    have to dynamically create the ini file sincce it looks like it is needed by the existing
    BACpypes framework
    """

    """
    # make a device object
    this_device = LocalDeviceObject(ini=args.ini)

    # make a simple application
    this_application = ReadPropertyApplication(this_device, server_addr)

    print("Device IP Address =             ", device_addr)
    print("Device ID =                      ", device_id)
    print("Object ID =                      <", object_type, ",", object_id, ">")
    print("Property ID =                   ", property_id)

    # kick off the process after the core is up and running
    deferred(this_application.read_property_value, device_id, device_addr, object_type, object_id, property_id)
    """

def main():
    global this_device
    global this_application

    # parse the command line arguments
    parser = ConfigArgumentParser(description=__doc__)

    # add an argument for the device identifier
    parser.add_argument('device_id', type=int,
          help='device identifier',
          )

    # add an argument for the address of the device
    parser.add_argument('device_addr', type=str,
          help='device address',
          )
    
    parser.add_argument('object_type', type=str,
          help='object type',
          )
    
    parser.add_argument('object_id', type=int,
          help='object id',
          )
    
    parser.add_argument('property_id', type=str,
          help='property id',
          )
    
    # parse the args
    args = parser.parse_args()

    # make a device object
    this_device = LocalDeviceObject(ini=args.ini)

    print("args.ini = \n", args.ini)

    # make a simple application
    this_application = ReadPropertyApplication(this_device, args.ini.address)

    # build a device object identifier
    device_id = ('device', args.device_id)

    # translate the address
    device_addr = Address(args.device_addr)
    object_type = args.object_type # Ex... analogInput (see the ObjectTypesSupported class)
    object_id = args.object_id
    property_id = args.property_id # Ex... 'presentValue'  equivilent to (85)

    print("Client IP Address =             ", args.ini.address)
    print("Client Device ID =              ", args.ini.objectidentifier)
    print("Server IP Address =             ", device_addr)
    print("Server Device ID =              ", device_id)
    print("Object ID =                      <", object_type, ",", object_id, ">")
    print("Property ID =                   ", property_id)

    # kick off the process after the core is up and running
    deferred(this_application.read_property_value, device_id, device_addr, object_type, object_id, property_id)

    run()

if __name__ == "__main__":
    main()
