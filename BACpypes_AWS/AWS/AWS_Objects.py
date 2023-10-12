#!/usr/bin/env python

"""
The writable objects needed for validating AWS
"""

from AWS_Variables import current_date_time, log_record, log_record_datum, status_flags, date_time, \
    defaultCommandTime, defaultCommandTimeArray, defaultEventMessageTexts, defaultEventMessageTextsConfig, \
    defaultEventTimestamps, defaultPriorityArrayValues, listOfLogDeviceObjectProperties

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
    MultiStateInputObject
)

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
from bacpypes.constructeddata import ArrayOf, ListOf

@register_object_type(vendor_id=10)
class WritableDateTimeValueObject(DateTimeValueObject):
    properties = \
    [ 
        WritableProperty('presentValue', DateTime)
        , WritableProperty('statusFlags', StatusFlags)
        , WritableProperty('description', CharacterString)
        , WritableProperty('description', CharacterString)
        , WritableProperty('eventState', EventState)
        , WritableProperty('reliability', Reliability)
        , WritableProperty('outOfService', Boolean)
        , WritableProperty('priorityArray', PriorityArray)
        , WritableProperty('relinquishDefault', DateTime)
        , WritableProperty('isUTC', Boolean)
        , WritableProperty('reliabilityEvaluationInhibit', Boolean)
        , WritableProperty('eventDetectionEnable', Boolean)
        , WritableProperty('notificationClass', Unsigned)
        , WritableProperty('eventEnable', EventTransitionBits)
        , WritableProperty('ackedTransitions', EventTransitionBits)
        , WritableProperty('notifyType', NotifyType)
        , WritableProperty('eventTimeStamps', ArrayOf(TimeStamp, 3))
        , WritableProperty('eventMessageTexts', ArrayOf(CharacterString, 3))
        , WritableProperty('eventMessageTextsConfig', ArrayOf(CharacterString, 3))
        , WritableProperty('currentCommandPriority', OptionalUnsigned)
        , WritableProperty('valueSource', ValueSource)
        , WritableProperty('valueSourceArray', ArrayOf(ValueSource, 16))
        , WritableProperty('lastCommandTime', TimeStamp)
        , WritableProperty('commandTimeArray', ArrayOf(TimeStamp, 16))
        , WritableProperty('auditablePriorityFilter', OptionalPriorityFilter)
    ]

@register_object_type(vendor_id=10)
class WritableDateTimePatternValueObject(DateTimePatternValueObject):
    properties = \
    [ 
        WritableProperty('presentValue', DateTime)
        , WritableProperty('statusFlags', StatusFlags)
        , WritableProperty('description', CharacterString)
        , WritableProperty('eventState', EventState)
        , WritableProperty('reliability', Reliability)
        , WritableProperty('outOfService', Boolean)
        , WritableProperty('priorityArray', PriorityArray)
        , WritableProperty('relinquishDefault', DateTime)
        , WritableProperty('isUTC', Boolean)
        , WritableProperty('reliabilityEvaluationInhibit', Boolean)
        , WritableProperty('eventDetectionEnable', Boolean)
        , WritableProperty('notificationClass', Unsigned)
        , WritableProperty('eventEnable', EventTransitionBits)
        , WritableProperty('ackedTransitions', EventTransitionBits)
        , WritableProperty('notifyType', NotifyType)
        , WritableProperty('eventTimeStamps', ArrayOf(TimeStamp, 3))
        , WritableProperty('eventMessageTexts', ArrayOf(CharacterString, 3))
        , WritableProperty('eventMessageTextsConfig', ArrayOf(CharacterString, 3))
        , WritableProperty('currentCommandPriority', OptionalUnsigned)
        , WritableProperty('valueSource', ValueSource)
        , WritableProperty('valueSourceArray', ArrayOf(ValueSource, 16))
        , WritableProperty('lastCommandTime', TimeStamp)
        , WritableProperty('commandTimeArray', ArrayOf(TimeStamp, 16))
        , WritableProperty('auditablePriorityFilter', OptionalPriorityFilter)
    ]

@register_object_type(vendor_id=10)
class WritableTrendLogMultipleObject(TrendLogMultipleObject):
    properties = \
        [ WritableProperty('statusFlags', StatusFlags)
        , WritableProperty('eventState', EventState)
        , WritableProperty('reliability', Reliability)
        , WritableProperty('enable', Boolean)
        , WritableProperty('startTime', DateTime)
        , WritableProperty('stopTime', DateTime)
        , WritableProperty('logDeviceObjectProperty', ArrayOf(DeviceObjectPropertyReference))
        , WritableProperty('loggingType', LoggingType)
        , WritableProperty('logInterval', Unsigned)
        , WritableProperty('alignIntervals', Boolean)
        , WritableProperty('intervalOffset', Unsigned)
        , WritableProperty('trigger', Boolean)
        , WritableProperty('stopWhenFull', Boolean)
        , WritableProperty('bufferSize', Unsigned)
        , WritableProperty('logBuffer', ListOf(LogMultipleRecord))
        , WritableProperty('recordCount', Unsigned)
        , WritableProperty('totalRecordCount', Unsigned)
        , WritableProperty('notificationThreshold', Unsigned)
        , WritableProperty('recordsSinceNotification', Unsigned)
        , WritableProperty('lastNotifyRecord', Unsigned)
        , WritableProperty('notificationClass', Unsigned)
        , WritableProperty('eventEnable', EventTransitionBits)
        , WritableProperty('ackedTransitions', EventTransitionBits)
        , WritableProperty('notifyType', NotifyType)
        , WritableProperty('eventTimeStamps', ArrayOf(TimeStamp, 3))
        , WritableProperty('eventMessageTexts', ArrayOf(CharacterString, 3))
        , WritableProperty('eventMessageTextsConfig', ArrayOf(CharacterString, 3))
        , WritableProperty('eventDetectionEnable', Boolean)
        , WritableProperty('eventAlgorithmInhibitRef', ObjectPropertyReference)
        , WritableProperty('eventAlgorithmInhibit', Boolean)
        , WritableProperty('reliabilityEvaluationInhibit', Boolean)
    ]

@register_object_type(vendor_id=10)
class WritableTrendLogObject(TrendLogObject):
    objectType = 'trendLog'
    properties = \
        [ WritableProperty('statusFlags', StatusFlags)
        , WritableProperty('eventState', EventState)
        , WritableProperty('reliability', Reliability)
        , WritableProperty('enable', Boolean)
        , WritableProperty('startTime', DateTime)
        , WritableProperty('stopTime', DateTime)
        , WritableProperty('logDeviceObjectProperty', DeviceObjectPropertyReference)
        , WritableProperty('logInterval', Unsigned)
        , WritableProperty('covResubscriptionInterval', Unsigned)
        , WritableProperty('clientCovIncrement', ClientCOV)
        , WritableProperty('stopWhenFull', Boolean)
        , WritableProperty('bufferSize', Unsigned)
        , WritableProperty('logBuffer', ListOf(LogRecord))
        , WritableProperty('recordCount', Unsigned)
        , WritableProperty('totalRecordCount', Unsigned)
        , WritableProperty('loggingType', LoggingType)
        , WritableProperty('alignIntervals', Boolean)
        , WritableProperty('intervalOffset', Unsigned)
        , WritableProperty('trigger', Boolean)
        , WritableProperty('statusFlags', StatusFlags)
        , WritableProperty('reliability', Reliability)
        , WritableProperty('notificationThreshold', Unsigned)
        , WritableProperty('recordsSinceNotification', Unsigned)
        , WritableProperty('lastNotifyRecord', Unsigned)
        , WritableProperty('eventState', EventState)
        , WritableProperty('notificationClass', Unsigned)
        , WritableProperty('eventEnable', EventTransitionBits)
        , WritableProperty('ackedTransitions', EventTransitionBits)
        , WritableProperty('notifyType', NotifyType)
        , WritableProperty('eventTimeStamps', ArrayOf(TimeStamp, 3))
        , WritableProperty('eventMessageTexts', ArrayOf(CharacterString, 3))
        , WritableProperty('eventMessageTextsConfig', ArrayOf(CharacterString, 3))
        , WritableProperty('eventDetectionEnable', Boolean)
        , WritableProperty('eventAlgorithmInhibitRef', ObjectPropertyReference)
        , WritableProperty('eventAlgorithmInhibit', Boolean)
        , WritableProperty('reliabilityEvaluationInhibit', Boolean)
        ]


@register_object_type
class WritableAnalogInputObject(AnalogInputObject):
    objectType = 'analogInput'
    _object_supports_cov = True

    properties = \
        [ WritableProperty('presentValue', Real)
        , WritableProperty('deviceType', CharacterString)
        , WritableProperty('statusFlags', StatusFlags)
        , WritableProperty('eventState', EventState)
        , WritableProperty('reliability', Reliability)
        , WritableProperty('outOfService', Boolean)
        , WritableProperty('updateInterval', Unsigned)
        , WritableProperty('units', EngineeringUnits)
        , WritableProperty('minPresValue', Real)
        , WritableProperty('maxPresValue', Real)
        , WritableProperty('resolution', Real)
        , WritableProperty('covIncrement', Real)
        , WritableProperty('timeDelay', Unsigned)
        , WritableProperty('notificationClass', Unsigned)
        , WritableProperty('highLimit', Real)
        , WritableProperty('lowLimit', Real)
        , WritableProperty('deadband', Real)
        , WritableProperty('limitEnable', LimitEnable)
        , WritableProperty('eventEnable', EventTransitionBits)
        , WritableProperty('ackedTransitions', EventTransitionBits)
        , WritableProperty('notifyType', NotifyType)
        , WritableProperty('eventTimeStamps', ArrayOf(TimeStamp, 3))
        , WritableProperty('eventMessageTexts', ArrayOf(CharacterString, 3))
        , WritableProperty('eventMessageTextsConfig', ArrayOf(CharacterString, 3))
        , WritableProperty('eventDetectionEnable', Boolean)
        , WritableProperty('eventAlgorithmInhibitRef', ObjectPropertyReference)
        , WritableProperty('eventAlgorithmInhibit', Boolean)
        , WritableProperty('timeDelayNormal', Unsigned)
        , WritableProperty('reliabilityEvaluationInhibit', Boolean)
        , WritableProperty('interfaceValue', OptionalReal)
        , WritableProperty('faultHighLimit', Real)
        , WritableProperty('faultLowLimit', Real)
        ]
    

@register_object_type
class WritableBinaryOutputObject(BinaryOutputObject):
    objectType = 'binaryOutput'
    _object_supports_cov = True

    properties = \
        [ WritableProperty('presentValue', BinaryPV)
        , WritableProperty('deviceType', CharacterString)
        , WritableProperty('statusFlags', StatusFlags)
        , WritableProperty('eventState', EventState)
        , WritableProperty('reliability', Reliability)
        , WritableProperty('outOfService', Boolean)
        , WritableProperty('polarity', Polarity)
        , WritableProperty('inactiveText', CharacterString)
        , WritableProperty('activeText', CharacterString)
        , WritableProperty('changeOfStateTime', DateTime)
        , WritableProperty('changeOfStateCount', Unsigned)
        , WritableProperty('timeOfStateCountReset', DateTime)
        , WritableProperty('elapsedActiveTime', Unsigned)
        , WritableProperty('timeOfActiveTimeReset', DateTime)
        , WritableProperty('minimumOffTime', Unsigned)
        , WritableProperty('minimumOnTime', Unsigned)
        , WritableProperty('priorityArray', PriorityArray)
        , WritableProperty('relinquishDefault', BinaryPV)
        , WritableProperty('timeDelay', Unsigned)
        , WritableProperty('notificationClass', Unsigned)
        , WritableProperty('feedbackValue', BinaryPV)
        , WritableProperty('eventEnable', EventTransitionBits)
        , WritableProperty('ackedTransitions', EventTransitionBits)
        , WritableProperty('notifyType', NotifyType)
        , WritableProperty('eventTimeStamps', ArrayOf(TimeStamp, 3))
        , WritableProperty('eventMessageTexts', ArrayOf(CharacterString, 3))
        , WritableProperty('eventMessageTextsConfig', ArrayOf(CharacterString, 3))
        , WritableProperty('eventDetectionEnable', Boolean)
        , WritableProperty('eventAlgorithmInhibitRef', ObjectPropertyReference)
        , WritableProperty('eventAlgorithmInhibit', Boolean)
        , WritableProperty('timeDelayNormal', Unsigned)
        , WritableProperty('reliabilityEvaluationInhibit', Boolean)
        , WritableProperty('interfaceValue', OptionalBinaryPV)
        , WritableProperty('currentCommandPriority', OptionalUnsigned)
        , WritableProperty('valueSource', ValueSource)
        , WritableProperty('valueSourceArray', ArrayOf(ValueSource, 16))
        , WritableProperty('lastCommandTime', TimeStamp)
        , WritableProperty('commandTimeArray', ArrayOf(TimeStamp, 16))
        , WritableProperty('auditablePriorityFilter', OptionalPriorityFilter)
        ]

@register_object_type
class WritableMultiStateInputObject(MultiStateInputObject):
    objectType = 'multiStateInput'
    _object_supports_cov = True

    properties = \
        [ WritableProperty('presentValue', Unsigned)
        , WritableProperty('deviceType', CharacterString)
        , WritableProperty('statusFlags', StatusFlags)
        , WritableProperty('eventState', EventState)
        , WritableProperty('reliability', Reliability)
        , WritableProperty('outOfService', Boolean)
        , WritableProperty('numberOfStates', Unsigned)
        , WritableProperty('stateText', ArrayOf(CharacterString))
        , WritableProperty('timeDelay', Unsigned)
        , WritableProperty('notificationClass', Unsigned)
        , WritableProperty('alarmValues', ListOf(Unsigned))
        , WritableProperty('faultValues', ListOf(Unsigned))
        , WritableProperty('eventEnable', EventTransitionBits)
        , WritableProperty('ackedTransitions', EventTransitionBits)
        , WritableProperty('notifyType', NotifyType)
        , WritableProperty('eventTimeStamps', ArrayOf(TimeStamp, 3))
        , WritableProperty('eventMessageTexts', ArrayOf(CharacterString, 3))
        , WritableProperty('eventMessageTextsConfig', ArrayOf(CharacterString, 3))
        , WritableProperty('eventDetectionEnable', Boolean)
        , WritableProperty('eventAlgorithmInhibitRef', ObjectPropertyReference)
        , WritableProperty('eventAlgorithmInhibit', Boolean)
        , WritableProperty('timeDelayNormal', Unsigned)
        , WritableProperty('reliabilityEvaluationInhibit', Boolean)
        , WritableProperty('interfaceValue', OptionalUnsigned)
        ]

def createAnalogInputObject(name, id):
    """ Create a writable Analog Input object with some default variables
    """
    object = WritableAnalogInputObject(
        objectIdentifier = ("analogInput", id),
        objectName = name,
        description = name + " Description",
        presentValue = 1.2,
        statusFlags = [0, 0, 0, 0],
        eventState = 'normal',
        outOfService = False,
        units = None,
        reliabilityEvaluationInhibit = False,
        eventDetectionEnable = True,
        eventAlgorithmInhibitRef = ObjectPropertyReference(
                    objectIdentifier=("binaryOutput", 1),
                    propertyIdentifier="presentValue",
                    ),
        eventAlgorithmInhibit = False,
        reliability = 'noFaultDetected',
        #notificationClass = 1,
        eventEnable = [1, 1, 1],
        ackedTransitions = [1, 1, 1],
        notifyType = 1,
        eventTimeStamps = defaultEventTimestamps,
        eventMessageTexts = defaultEventMessageTexts,
        eventMessageTextsConfig = defaultEventMessageTextsConfig,
        #ValueSource = 
        #valueSourceArray = 
        #lastCommandTime = defaultCommandTime,
        #commandTimeArray = defaultCommandTimeArray,
        #auditablePriorityFilter = 
    )
    return object

def createBinaryOutputObject(name, id):
    """ Create a writable Binary Output object with some default variables
    """
    object = WritableBinaryOutputObject(
        objectIdentifier = ("binaryOutput", id),
        objectName = name,
        description = name + " Description",
        presentValue = 'active',
        statusFlags = [0, 0, 0, 0],
        eventState = 'normal',
        outOfService = False,
        reliabilityEvaluationInhibit = False,
        eventDetectionEnable = True,
        eventAlgorithmInhibitRef = ObjectPropertyReference(
                    objectIdentifier=("binaryOutput", 4194303),
                    propertyIdentifier="presentValue",
                    ),
        eventAlgorithmInhibit = False,
        reliability = 'noFaultDetected',
        notificationClass = 1,
        eventEnable = [1, 1, 1],
        ackedTransitions = [1, 1, 1],
        notifyType = 1,
        eventTimeStamps = defaultEventTimestamps,
        eventMessageTexts = defaultEventMessageTexts,
        eventMessageTextsConfig = defaultEventMessageTextsConfig,        
        relinquishDefault = 'active',
        priorityArray = defaultPriorityArrayValues,
        currentCommandPriority = 16,
        #ValueSource = 
        #valueSourceArray = 
        #lastCommandTime = defaultCommandTime,
        #commandTimeArray = defaultCommandTimeArray,
        # auditablePriorityFilter = 
    )
    return object

def createMultiStateInputObject(name, id):
    """ Create a writable MultiState Input object with some default variables
    """
    object = WritableMultiStateInputObject(
        objectIdentifier = ("multiStateInput", id),
        objectName = name,
        description = name + " Description",
        presentValue = 1,
        statusFlags = [0, 0, 0, 0],
        eventState = 'normal',
        outOfService = False,
        reliabilityEvaluationInhibit = False,
        eventDetectionEnable = True,
        eventAlgorithmInhibitRef = ObjectPropertyReference(
                    objectIdentifier=("multiStateInput", 1),
                    propertyIdentifier="presentValue",
                    ),
        eventAlgorithmInhibit = False,
        reliability = 'noFaultDetected',
        notificationClass = 1,
        eventEnable = [1, 1, 1],
        ackedTransitions = [1, 1, 1],
        notifyType = 1,
        eventTimeStamps = defaultEventTimestamps,
        eventMessageTexts = defaultEventMessageTexts,
        eventMessageTextsConfig = defaultEventMessageTextsConfig,  
        timeDelayNormal = 1,
        interfaceValue = OptionalUnsigned(unsigned = Unsigned(3)),
        numberOfStates = 5,
        stateText = ['AWS State 1', 'AWS State 2', 'AWS State 3', 'AWS State 4', 'AWS State 5'],
        alarmValues = [1,2,3,4,5],
        faultValues = [1,2,3,4,5]
    )
    return object

def createTrendLogObject(name, id):
    """ Create a writable Trend Log object with some default variables
    """
    object = WritableTrendLogObject(
        objectIdentifier = ("trendLog", id),
        objectName = name,
        description = name + " Description",
        statusFlags = [0, 0, 0, 0],
        eventState = 'normal',
        reliability = 'noFaultDetected',
        enable = False,
        startTime = current_date_time,
        stopTime = current_date_time,
        logDeviceObjectProperty=DeviceObjectPropertyReference(
                    objectIdentifier=("binaryValue", 1),
                    propertyIdentifier="presentValue",
                ),
        loggingType='cov',
        logInterval=0,
        alignIntervals=False,
        intervalOffset=0,
        trigger='False',
        stopWhenFull=False,
        bufferSize=1000,
        logBuffer=[log_record],
        recordCount=0,
        totalRecordCount=0,
        notificationThreshold=0,
        recordsSinceNotification=0,
        lastNotifyRecord=0,
        notificationClass=1,
        eventEnable = [1, 1, 1],
        ackedTransitions = [1, 1, 1],
        notifyType = 1,
        eventTimeStamps = defaultEventTimestamps,
        eventMessageTexts = defaultEventMessageTexts,
        eventMessageTextsConfig = defaultEventMessageTextsConfig,
        eventAlgorithmInhibitRef = ObjectPropertyReference(
                    objectIdentifier=("binaryValue", 1),
                    propertyIdentifier="presentValue",
                    ),
        eventAlgorithmInhibit = False,
        reliabilityEvaluationInhibit = False
    )
    return object

def createTrendLogMultipleObject(name, id):
    """ Create a writable Trend Log Multiple object with some default variables
    """
    object = WritableTrendLogMultipleObject(
        objectIdentifier = ("trendLogMultiple", id),
        objectName = name,
        description = name + " Description",
        statusFlags = [0, 0, 0, 0],
        eventState = 'normal',
        reliability = 'noFaultDetected',
        enable = False,
        startTime = current_date_time,
        stopTime = current_date_time,
        logDeviceObjectProperty=listOfLogDeviceObjectProperties,
        loggingType='cov',
        logInterval=0,
        alignIntervals=False,
        intervalOffset=0,
        trigger='False',
        stopWhenFull=False,
        bufferSize=1000,
        logBuffer=[log_record],
        recordCount=0,
        totalRecordCount=0,
        notificationThreshold=0,
        recordsSinceNotification=0,
        lastNotifyRecord=0,
        notificationClass=1,
        eventEnable = [1, 1, 1],
        ackedTransitions = [1, 1, 1],
        notifyType = 1,
        eventTimeStamps = defaultEventTimestamps,
        eventMessageTexts = defaultEventMessageTexts,
        eventMessageTextsConfig = defaultEventMessageTextsConfig,
        eventAlgorithmInhibitRef = ObjectPropertyReference(
                    objectIdentifier=("binaryValue", 1),
                    propertyIdentifier="presentValue",
                    ),
        eventAlgorithmInhibit = False,
        reliabilityEvaluationInhibit = False
    )
    return object

def createDateTimeValueObject(name, id):
    """ Create a writable Date Time Value object with some default variables
    """
    object = WritableDateTimeValueObject(
        objectIdentifier = ("datetimeValue", id),
        objectName = name,
        description = name + " Description",
        presentValue = date_time,
        statusFlags = [0, 0, 0, 0],
        eventState = 'normal',
        outOfService = False,
		isUTC = True,
        relinquishDefault = date_time,
        reliabilityEvaluationInhibit = False,
        eventDetectionEnable = True,
        reliability = 'noFaultDetected',
        notificationClass = 1,
        eventEnable = [1, 1, 1],
        ackedTransitions = [1, 1, 1],
        notifyType = 1,
        eventTimeStamps = defaultEventTimestamps,
        eventMessageTexts = defaultEventMessageTexts,
        eventMessageTextsConfig = defaultEventMessageTextsConfig,
        currentCommandPriority = 16,
        priorityArray = defaultPriorityArrayValues,
        #ValueSource = 
        #valueSourceArray = 
        #lastCommandTime = defaultCommandTime,
        #commandTimeArray = defaultCommandTimeArray,
        # auditablePriorityFilter =         
    )
    return object

def createDateTimePatternValueObject(name, id):
    """ Create a writable Date Time Pattern object with some default variables
    """
    object = WritableDateTimePatternValueObject(
        objectIdentifier = ("datetimePatternValue", id),
        objectName = name,
        description = name + " Description",
        presentValue = date_time,
        statusFlags = [0, 0, 0, 0],
        eventState = 'normal',
        outOfService = False,
		isUTC = True,
        relinquishDefault = date_time,
        reliabilityEvaluationInhibit = False,
        eventDetectionEnable = True,
        reliability = 'noFaultDetected',
        notificationClass = 1,
        eventEnable = [1, 1, 1],
        ackedTransitions = [1, 1, 1],
        notifyType = 1,
        eventTimeStamps = defaultEventTimestamps,
        eventMessageTexts = defaultEventMessageTexts,
        eventMessageTextsConfig = defaultEventMessageTextsConfig,
        currentCommandPriority = 16,
        priorityArray = defaultPriorityArrayValues,
        #ValueSource = 
        #valueSourceArray = 
        #lastCommandTime = defaultCommandTime,
        #commandTimeArray = defaultCommandTimeArray,
        # auditablePriorityFilter =         
    )
    return object
