#!/usr/bin/env python

"""
This application is given the IP address, instance number, object type, object ID and then reads
the present-value.

TODO: Make this do much more
"""
import sys
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

def object_results(iocb):
    context = iocb.context

    if iocb.ioError:
        context.completed(iocb.ioError)
        return

    # do something for success
    elif iocb.ioResponse:
        apdu = iocb.ioResponse
        # should be an ack
        if not isinstance(apdu, ReadPropertyACK):
            print("    - not an ack")
            return

        # find the datatype
        datatype = get_datatype(
            apdu.objectIdentifier[0], apdu.propertyIdentifier
        )
        print("    - datatype: ", datatype)
        if not datatype:
            print("unknown datatype")
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
        stop()

    # do something with nothing?
    else:
        print("    - ioError or ioResponse expected")

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
    
    # parse the args
    args = parser.parse_args()

    # make a device object
    this_device = LocalDeviceObject(ini=args.ini)

    # make a simple application
    this_application = BIPSimpleApplication(this_device, args.ini.address)

    # build a device object identifier
    device_id = ('device', args.device_id)

    # translate the address
    device_addr = Address(args.device_addr)
    object_type = args.object_type # Ex... analogInput (see the ObjectTypesSupported class)
    object_id = args.object_id
    prop_id = 'presentValue'     # present-value (85)

    print("Client IP Address =             ", args.ini.address)
    print("Client Device ID =              ", args.ini.objectidentifier)
    print("Server IP Address =             ", device_addr)
    print("Server Device ID =              ", device_id)
    print("Object ID =                      <", object_type, ",", object_id, ">")
    print("Property ID =                   ", prop_id)
   
    # TODO: Figure out what this stuff is
    # create a context to hold the results
    context = ObjectListContext(device_id, device_addr)
    
    # kick off the process after the core is up and running
    request = ReadPropertyRequest(
            objectIdentifier=(object_type, object_id),
            propertyIdentifier='presentValue',
            )
    
    request.pduDestination = context.device_addr
    
    iocb = IOCB(request)
    iocb.context = context
    iocb.add_callback(object_results)

    # give it to the application
    deferred(this_application.request_io, iocb)

    # wait for it to complete
    # TODO: Figure out how to remove the 5 second wait and have it return when finished
    iocb.wait(5)

    # do something for error/reject/abort
    if iocb.ioError:
        print(str(iocb.ioError) + "\n")
        return
    
    run()

if __name__ == "__main__":
    main()
