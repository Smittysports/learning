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

from bacpypes.primitivedata import Boolean, CharacterString, Tag, Null, Atomic, Integer, Unsigned, Real, ObjectIdentifier, Enumerated
from bacpypes.constructeddata import ArrayOf, Any

from bacpypes.pdu import Address
from bacpypes.apdu import ReadPropertyACK, WritePropertyRequest, SimpleAckPDU

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

class WritePropertyApplication(BIPSimpleApplication):

    def __init__(self, *args):
        BIPSimpleApplication.__init__(self, *args)

    def read_property_value(self, device_id, device_addr, object_type, object_id, value_type, property_id, new_value):
        # create a context to hold the results
        context = ObjectListContext(device_id, device_addr)
            
        request = WritePropertyRequest(
                destination=context.device_addr,
                objectIdentifier=(object_type, object_id),
                propertyIdentifier=property_id,
                )
        request.propertyValue = Any()

        # The types used in the request are shown in primitivedata.py
        if (value_type == "float") or (value_type == "f"):
            request.propertyValue.cast_in(Real(float(new_value)))
        elif (value_type == "characterstring") or (value_type == "c"):
            request.propertyValue.cast_in(CharacterString(new_value))
        elif (value_type == "enumerated") or (value_type == "e"):
            request.propertyValue.cast_in(Enumerated(int(new_value)))
        elif (value_type == "bool") or (value_type == "boolean") or (value_type == "b"):
            request.propertyValue.cast_in(Boolean(new_value))
        elif (value_type == "unsigned") or (value_type == "u"):
            request.propertyValue.cast_in(Unsigned(new_value))
        else:
            print("Invalid value type passed in")
            exit
        
        # make an IOCB, reference the context
        iocb = IOCB(request)
        iocb.context = context
        iocb.add_callback(self.object_property_results)

        self.request_io(iocb)

    def object_property_results(self, iocb):
        context = iocb.context

        if iocb.ioError:
            print("    - error: ", iocb.ioError)
            context.completed()
            return

        # do something for success
        elif iocb.ioResponse:
            apdu = iocb.ioResponse
            # should be an ack
            if isinstance(apdu, SimpleAckPDU):
                print("    - obtained a simple ack")
                context.completed()
                return
            elif not isinstance(apdu, ReadPropertyACK):
                print("    - not a simple ACK")
                context.completed()
                return

            print("    - unknown response")
            context.completed()
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
    
    parser.add_argument('property_id', type=str,
          help='property id',
          )
    
    parser.add_argument('value_type', type=str,
          help='value type',
          )
    
    parser.add_argument('new_value', type=str,
          help='value',
          )
    
    # parse the args
    args = parser.parse_args()

    # make a device object
    this_device = LocalDeviceObject(ini=args.ini)

    # make a simple application
    this_application = WritePropertyApplication(this_device, args.ini.address)

    # build a device object identifier
    device_id = ('device', args.device_id)

    # translate the address
    device_addr = Address(args.device_addr)
    object_type = args.object_type # Ex... analogInput (see the ObjectTypesSupported class)
    object_id = args.object_id
    property_id = args.property_id # Ex... 'presentValue'  equivilent to (85)
    value_type = args.value_type
    new_value = args.new_value

    print("Client IP Address =             ", args.ini.address)
    print("Client Device ID =              ", args.ini.objectidentifier)
    print("Server IP Address =             ", device_addr)
    print("Server Device ID =              ", device_id)
    print("Object ID =                      <", object_type, ",", object_id, ">")
    print("Property ID =                   ", property_id)
    print("Value type =                    ", value_type)
    print("Value =                         ", new_value)
      
    # kick off the process after the core is up and running
    deferred(this_application.read_property_value, device_id, device_addr, object_type, object_id, value_type, property_id, new_value)
    
    run()

if __name__ == "__main__":
    main()
