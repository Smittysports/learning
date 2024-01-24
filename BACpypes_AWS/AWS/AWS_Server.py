#!/usr/bin/env python

"""
This sample application is a server that contains AWS objects.

I modified the COVServer.py file and extended many Objects so that they are fully Writable.

TODO: Test how COV actually works with BACpypes
"""

import time
from threading import Thread

from bacpypes.debugging import bacpypes_debugging, ModuleLogger
from bacpypes.consolelogging import ConfigArgumentParser
from bacpypes.consolecmd import ConsoleCmd

from bacpypes.core import run, deferred, enable_sleeping
from bacpypes.task import RecurringTask

from bacpypes.app import BIPSimpleApplication
from bacpypes.primitivedata import Real
from bacpypes.object import (
    WritableProperty,
    ReadableProperty,
    AnalogValueObject,
    BinaryValueObject,
    DateTimeValueObject,
    DateTimePatternValueObject,
    register_object_type,
    TrendLogObject,
    TrendLogMultipleObject,
    AnalogInputObject,
    BinaryOutputObject,
    MultiStateValueObject,
    PropertyError
)
from bacpypes.errors import ExecutionError, RejectException
from bacpypes.local.device import LocalDeviceObject
from bacpypes.service.cov import ChangeOfValueServices
from bacpypes.basetypes import AccessCredentialDisable, AccessCredentialDisableReason, \
    AccessEvent, AccessPassbackMode, AccessRule, AccessThreatLevel, \
    AccessUserType, AccessZoneOccupancyState, AccumulatorRecord, Action, \
    ActionList, AddressBinding, AssignedAccessRights, AuditOperationFlags, AuditLevel, \
    AuthenticationFactor, \
    AuthenticationFactorFormat, AuthenticationPolicy, AuthenticationStatus, \
    AuthorizationException, AuthorizationMode, BackupState, BDTEntry, BinaryPV, \
    COVSubscription, CalendarEntry, ChannelValue, ClientCOV, \
    CredentialAuthenticationFactor, DailySchedule, DateRange, DateTime, \
    Destination, DeviceObjectPropertyReference, DeviceObjectReference, \
    DeviceStatus, DoorAlarmState, DoorSecuredStatus, DoorStatus, DoorValue, \
    EngineeringUnits, EventNotificationSubscription, EventParameter, \
    EventState, EventTransitionBits, EventType, FaultParameter, FaultType, \
    FileAccessMethod, FDTEntry, IPMode, HostNPort, LifeSafetyMode, LifeSafetyOperation, LifeSafetyState, \
    LightingCommand, LightingInProgress, LightingTransition, LimitEnable, \
    LockStatus, LogMultipleRecord, LogRecord, LogStatus, LoggingType, \
    Maintenance, NameValue, NetworkNumberQuality, NetworkPortCommand, \
    NetworkSecurityPolicy, NetworkType, NodeType, NotifyType, \
    ObjectPropertyReference, ObjectTypesSupported, OptionalCharacterString, \
    Polarity, PortPermission, Prescale, PriorityArray, PriorityValue, ProcessIdSelection, \
    ProgramError, ProgramRequest, ProgramState, PropertyAccessResult, \
    PropertyIdentifier, ProtocolLevel, Recipient, Reliability, RestartReason, \
    RouterEntry, Scale, SecurityKeySet, SecurityLevel, Segmentation, \
    ServicesSupported, SetpointReference, ShedLevel, ShedState, SilencedState, \
    SpecialEvent, StatusFlags, TimeStamp, VTClass, VTSession, VMACEntry, \
    WriteStatus, OptionalUnsigned, PriorityFilter, ValueSource, \
    OptionalPriorityFilter, OptionalReal, AuditNotification, PropertyReference, \
    AuditLogRecord, ObjectSelector, OptionalBinaryPV, BinaryLightingPV, \
    COVMultipleSubscription, LiftGroupMode, LandingCallStatus, LiftCarDirection, \
    EscalatorOperationDirection, EscalatorMode, LiftFault, AssignedLandingCalls, \
    LiftCarCallList, LiftCarDoorCommand, LiftCarDriveStatus, LiftCarMode, \
    LandingDoorStatus, StageLimitValue, NameValueCollection, Relationship, \
    TimerState, TimerStateChangeValue, TimerTransition, LogRecordLogDatum
from bacpypes.primitivedata import Null, Atomic, BitString, Boolean, CharacterString, Date, \
    Double, Integer, ObjectIdentifier, ObjectType, OctetString, Real, Time, \
    Unsigned, Unsigned8, Unsigned16
from bacpypes.constructeddata import ArrayOf, ListOf, List, Array, SequenceOfAny
from AWS_Variables import current_date_time, log_record, log_record_datum, status_flags, date_time, \
    defaultCommandTime, defaultCommandTimeArray, defaultEventMessageTexts, defaultEventMessageTextsConfig, \
    defaultEventTimestamps, defaultPriorityArrayValues
import AWS_Objects
from bacpypes.apdu import ReadRangeACK

# some debugging
_debug = 0
_log = ModuleLogger(globals())

# test globals
test_av = None
test_bv = None
test_application = None
        
#
#   SubscribeCOVApplication
#


@bacpypes_debugging
class SubscribeCOVApplication(BIPSimpleApplication, ChangeOfValueServices):
    pass


@bacpypes_debugging
class ReadRangeApplication(BIPSimpleApplication):
    def __init__(self, *args):
        if _debug:
            ReadRangeApplication._debug("__init__ %r", args)
        BIPSimpleApplication.__init__(self, *args)

    def do_ReadRangeRequest(self, apdu):
        if _debug:
            ReadRangeApplication._debug("do_ReadRangeRequest %r", apdu)

        # extract the object identifier
        objId = apdu.objectIdentifier

        # get the object
        obj = self.get_object_id(objId)
        if _debug:
            ReadRangeApplication._debug("    - object: %r", obj)

        if not obj:
            raise ExecutionError(errorClass="object", errorCode="unknownObject")

        # get the datatype
        datatype = obj.get_datatype(apdu.propertyIdentifier)
        if _debug:
            ReadRangeApplication._debug("    - datatype: %r", datatype)

        # must be a list, or an array of lists
        if issubclass(datatype, List):
            pass
        elif (
            (apdu.propertyArrayIndex is not None)
            and issubclass(datatype, Array)
            and issubclass(datatype.subtype, List)
        ):
            pass
        else:
            raise ExecutionError(errorClass="property", errorCode="propertyIsNotAList")

        # get the value
        value = obj.ReadProperty(apdu.propertyIdentifier, apdu.propertyArrayIndex)
        if _debug:
            ReadRangeApplication._debug("    - value: %r", value)
        if value is None:
            raise PropertyError(apdu.propertyIdentifier)
        if isinstance(value, List):
            ReadRangeApplication._debug("    - value is a list of: %r", datatype.subtype)

        #if apdu.range.byPosition:
        #    range_by_position = apdu.range.byPosition
        #    if _debug:
        #        ReadRangeApplication._debug("    - range_by_position: %r", range_by_position)

        #elif apdu.range.bySequenceNumber:
        #    range_by_sequence_number = apdu.range.bySequenceNumber
        #    if _debug:
        #        ReadRangeApplication._debug("    - range_by_sequence_number: %r", range_by_sequence_number)

        #elif apdu.range.byTime:
        #    range_by_time = apdu.range.byTime
        #    if _debug:
        #        ReadRangeApplication._debug("    - range_by_time: %r", range_by_time)

        #else:
        #    raise RejectException("missingRequiredParameter")

        # this is an ack
        resp = ReadRangeACK(context=apdu)
        resp.objectIdentifier = objId
        resp.propertyIdentifier = apdu.propertyIdentifier
        resp.propertyArrayIndex = apdu.propertyArrayIndex

        resp.resultFlags = [1, 1, 0]
        resp.itemCount = len(value)

        # save the result in the item data
        resp.itemData = SequenceOfAny()
        resp.itemData.cast_in(datatype(value))
        if _debug:
            ReadRangeApplication._debug("    - resp: %r", resp)

        # return the result
        self.response(resp)

#
#   COVConsoleCmd
#


@bacpypes_debugging
class COVConsoleCmd(ConsoleCmd):
    def do_status(self, args):
        """status"""
        args = args.split()
        if _debug:
            COVConsoleCmd._debug("do_status %r", args)
        global test_application

        # dump from the COV detections dict
        for obj_ref, cov_detection in test_application.cov_detections.items():
            print("{} {}".format(obj_ref.objectIdentifier, obj_ref))

            for cov_subscription in cov_detection.cov_subscriptions:
                print(
                    "    {} proc_id={} confirmed={} lifetime={}".format(
                        cov_subscription.client_addr,
                        cov_subscription.proc_id,
                        cov_subscription.confirmed,
                        cov_subscription.lifetime,
                    )
                )

    def do_trigger(self, args):
        """trigger object_name"""
        args = args.split()
        if _debug:
            COVConsoleCmd._debug("do_trigger %r", args)
        global test_application

        if not args:
            print("object name required")
            return

        obj = test_application.get_object_name(args[0])
        if not obj:
            print("no such object")
            return

        # get the detection algorithm object
        cov_detection = test_application.cov_detections.get(obj, None)
        if (not cov_detection) or (len(cov_detection.cov_subscriptions) == 0):
            print("no subscriptions for that object")
            return

        # tell it to send out notifications
        cov_detection.send_cov_notifications()

    def do_set(self, args):
        """set object_name [ . ] property_name [ = ] value"""
        args = args.split()
        if _debug:
            COVConsoleCmd._debug("do_set %r", args)
        global test_application

        try:
            object_name = args.pop(0)
            if "." in object_name:
                object_name, property_name = object_name.split(".")
            else:
                property_name = args.pop(0)
            if _debug:
                COVConsoleCmd._debug("    - object_name: %r", object_name)
            if _debug:
                COVConsoleCmd._debug("    - property_name: %r", property_name)

            obj = test_application.get_object_name(object_name)
            if _debug:
                COVConsoleCmd._debug("    - obj: %r", obj)
            if not obj:
                raise RuntimeError("object not found: %r" % (object_name,))

            datatype = obj.get_datatype(property_name)
            if _debug:
                COVConsoleCmd._debug("    - datatype: %r", datatype)
            if not datatype:
                raise RuntimeError("not a property: %r" % (property_name,))

            # toss the equals
            if args[0] == "=":
                args.pop(0)

            # evaluate the value
            value = eval(args.pop(0))
            if _debug:
                COVConsoleCmd._debug("    - raw value: %r", value)

            # see if it can be built
            obj_value = datatype(value)
            if _debug:
                COVConsoleCmd._debug("    - obj_value: %r", obj_value)

            # normalize
            value = obj_value.value
            if _debug:
                COVConsoleCmd._debug("    - normalized value: %r", value)

            # change the value
            setattr(obj, property_name, value)

        except IndexError:
            print(COVConsoleCmd.do_set.__doc__)
        except Exception as err:
            print("exception: %s" % (err,))

    def do_write(self, args):
        """write object_name [ . ] property [ = ] value"""
        args = args.split()
        if _debug:
            COVConsoleCmd._debug("do_set %r", args)
        global test_application

        try:
            object_name = args.pop(0)
            if "." in object_name:
                object_name, property_name = object_name.split(".")
            else:
                property_name = args.pop(0)
            if _debug:
                COVConsoleCmd._debug("    - object_name: %r", object_name)
            if _debug:
                COVConsoleCmd._debug("    - property_name: %r", property_name)

            obj = test_application.get_object_name(object_name)
            if _debug:
                COVConsoleCmd._debug("    - obj: %r", obj)
            if not obj:
                raise RuntimeError("object not found: %r" % (object_name,))

            datatype = obj.get_datatype(property_name)
            if _debug:
                COVConsoleCmd._debug("    - datatype: %r", datatype)
            if not datatype:
                raise RuntimeError("not a property: %r" % (property_name,))

            # toss the equals
            if args[0] == "=":
                args.pop(0)

            # evaluate the value
            value = eval(args.pop(0))
            if _debug:
                COVConsoleCmd._debug("    - raw value: %r", value)

            # see if it can be built
            obj_value = datatype(value)
            if _debug:
                COVConsoleCmd._debug("    - obj_value: %r", obj_value)

            # normalize
            value = obj_value.value
            if _debug:
                COVConsoleCmd._debug("    - normalized value: %r", value)

            # pass it along
            obj.WriteProperty(property_name, value)

        except IndexError:
            print(COVConsoleCmd.do_write.__doc__)
        except Exception as err:
            print("exception: %s" % (err,))


@bacpypes_debugging
class TestAnalogValueTask(RecurringTask):

    """
    An instance of this class is created when '--avtask <interval>' is
    specified as a command line argument.  Every <interval> seconds it
    changes the value of the test_av present value.
    """

    def __init__(self, interval):
        if _debug:
            TestAnalogValueTask._debug("__init__ %r", interval)
        RecurringTask.__init__(self, interval * 1000)

        # make a list of test values
        self.test_values = list(float(i * 10) for i in range(10))

    def process_task(self):
        if _debug:
            TestAnalogValueTask._debug("process_task")
        global test_av

        # pop the next value
        next_value = self.test_values.pop(0)
        self.test_values.append(next_value)
        if _debug:
            TestAnalogValueTask._debug("    - next_value: %r", next_value)

        # change the point
        test_av.presentValue = next_value


@bacpypes_debugging
class TestAnalogValueThread(Thread):

    """
    An instance of this class is created when '--avthread <interval>' is
    specified as a command line argument.  Every <interval> seconds it
    changes the value of the test_av present value.
    """

    def __init__(self, interval):
        if _debug:
            TestAnalogValueThread._debug("__init__ %r", interval)
        Thread.__init__(self)

        # runs as a daemon
        self.daemon = True

        # save the interval
        self.interval = interval

        # make a list of test values
        self.test_values = list(100.0 + float(i * 10) for i in range(10))

    def run(self):
        if _debug:
            TestAnalogValueThread._debug("run")
        global test_av

        while True:
            # pop the next value
            next_value = self.test_values.pop(0)
            self.test_values.append(next_value)
            if _debug:
                TestAnalogValueThread._debug("    - next_value: %r", next_value)

            # change the point
            test_av.presentValue = next_value

            # sleep
            time.sleep(self.interval)


@bacpypes_debugging
class TestBinaryValueTask(RecurringTask):

    """
    An instance of this class is created when '--bvtask <interval>' is
    specified as a command line argument.  Every <interval> seconds it
    changes the value of the test_bv present value.
    """

    def __init__(self, interval):
        if _debug:
            TestBinaryValueTask._debug("__init__ %r", interval)
        RecurringTask.__init__(self, interval * 1000)

        # save the interval
        self.interval = interval

        # make a list of test values
        self.test_values = [True, False]

    def process_task(self):
        if _debug:
            TestBinaryValueTask._debug("process_task")
        global test_bv

        # pop the next value
        next_value = self.test_values.pop(0)
        self.test_values.append(next_value)
        if _debug:
            TestBinaryValueTask._debug("    - next_value: %r", next_value)

        # change the point
        test_bv.presentValue = next_value


@bacpypes_debugging
class TestBinaryValueThread(RecurringTask, Thread):

    """
    An instance of this class is created when '--bvthread <interval>' is
    specified as a command line argument.  Every <interval> seconds it
    changes the value of the test_bv present value.
    """

    def __init__(self, interval):
        if _debug:
            TestBinaryValueThread._debug("__init__ %r", interval)
        Thread.__init__(self)

        # runs as a daemon
        self.daemon = True

        # save the interval
        self.interval = interval

        # make a list of test values
        self.test_values = [True, False]

    def run(self):
        if _debug:
            TestBinaryValueThread._debug("run")
        global test_bv

        while True:
            # pop the next value
            next_value = self.test_values.pop(0)
            self.test_values.append(next_value)
            if _debug:
                TestBinaryValueThread._debug("    - next_value: %r", next_value)

            # change the point
            test_bv.presentValue = next_value

            # sleep
            time.sleep(self.interval)


def main():
    global test_av, test_bv, test_application

    # make a parser
    parser = ConfigArgumentParser(description=__doc__)
    parser.add_argument(
        "--console", action="store_true", default=False, help="create a console",
    )

    # analog value task and thread
    parser.add_argument(
        "--avtask", type=float, help="analog value recurring task",
    )
    parser.add_argument(
        "--avthread", type=float, help="analog value thread",
    )

    # analog value task and thread
    parser.add_argument(
        "--bvtask", type=float, help="binary value recurring task",
    )
    parser.add_argument(
        "--bvthread", type=float, help="binary value thread",
    )

    # provide a different spin value
    parser.add_argument(
        "--spin", type=float, help="spin time", default=1.0,
    )

    # parse the command line arguments
    args = parser.parse_args()

    # make a device object
    this_device = LocalDeviceObject(ini=args.ini)

    print("IP Address =             ", args.ini.address)
    print("Device ID =              ", args.ini.objectidentifier)
    
    # make a sample application
    test_application = ReadRangeApplication(this_device, args.ini.address)

    """
    # make a binary value object
    test_bv = BinaryValueObject(
        objectIdentifier=("binaryValue", 1),
        objectName="bv",
        presentValue="inactive",
        statusFlags=[0, 0, 0, 0],
    )
    _log.debug("    - test_bv: %r", test_bv)

    # add it to the device
    test_application.add_object(test_bv)
    """

     ##### B-AWS Objects
    test_ai = AWS_Objects.createAnalogInputObject("Analog Input", 1)
    test_application.add_object(test_ai)
    print("Analog Input             <0, 1>")

    test_bo = AWS_Objects.createBinaryOutputObject("Binary Output", 1)
    test_application.add_object(test_bo)
    print("Binary Output            <4, 1>")
        
    test_tlm = AWS_Objects.createTrendLogMultipleObject("Trend Log Multiple", 1)
    test_application.add_object(test_tlm)
    print("Trend Log Multiple       <27, 1>")

    test_tl = AWS_Objects.createTrendLogObject("Trend Log", 1)
    test_application.add_object(test_tl)
    print("Trend Log                <20, 1>")

    test_el = AWS_Objects.createEventLogObject("Event Log", 1)
    test_application.add_object(test_el)
    print("Event Log                <25, 1>")

    test_dtv = AWS_Objects.createDateTimeValueObject("Date Time Value", 1)
    test_application.add_object(test_dtv)
    print("Date Time Value          <44, 1>")

    test_dtpv = AWS_Objects.createDateTimePatternValueObject("Date Time Pattern Value", 1)
    test_application.add_object(test_dtpv)
    print("Date Time Pattern Value  <43, 1>")

    #test_msi = AWS_Objects.createMultiStateInputObject("MultiState Input", 1)
    #test_application.add_object(test_msi)
    
    """
    msvo = MultiStateValueObject(
        objectIdentifier=('multiStateValue', 1),
        objectName='My Special Object',
        presentValue=1,
        numberOfStates=3,
        stateText=[CharacterString('red'), CharacterString('green'), CharacterString('blue')],
        )
    test_application.add_object(msvo)
    """
  

    # make a console
    if args.console:
        test_console = COVConsoleCmd()
        _log.debug("    - test_console: %r", test_console)

        # enable sleeping will help with threads
        enable_sleeping()

    # analog value task
    if args.avtask:
        test_av_task = TestAnalogValueTask(args.avtask)
        test_av_task.install_task()

    # analog value thread
    if args.avthread:
        test_av_thread = TestAnalogValueThread(args.avthread)
        deferred(test_av_thread.start)

    # binary value task
    if args.bvtask:
        test_bv_task = TestBinaryValueTask(args.bvtask)
        test_bv_task.install_task()

    # binary value thread
    if args.bvthread:
        test_bv_thread = TestBinaryValueThread(args.bvthread)
        deferred(test_bv_thread.start)

    _log.debug("running")

    run(args.spin)

    _log.debug("fini")


if __name__ == "__main__":
    main()
