#!/usr/bin/env python

"""
Re-usable variables that are useful for Object Properties
"""

from bacpypes.basetypes import DateTime, LogRecordLogDatum, StatusFlags, LogRecord, \
    TimeStamp, Date, Time, CharacterString, PriorityValue, PriorityArray, DeviceObjectPropertyReference
from bacpypes.constructeddata import ArrayOf, ListOf
from bacpypes.primitivedata import Null, Integer

current_date_time = DateTime(date=Date().now().value, time=Time().now().value)
log_record_datum = LogRecordLogDatum(booleanValue=False)
status_flags = StatusFlags([0, 0, 0, 0])
log_record = LogRecord(
    timestamp=current_date_time, logDatum=log_record_datum, statusFlags=status_flags
)
date_time = DateTime(date=(95, 1, 25, 3), time=(9, 0, 0, 0))
time_stamp1 = TimeStamp(dateTime=DateTime(date=(95, 1, 25, 3), time=(7, 0, 0, 0)))
time_stamp2 = TimeStamp(dateTime=DateTime(date=(95, 1, 25, 3), time=(8, 0, 0, 0)))
time_stamp3 = TimeStamp(dateTime=DateTime(date=(95, 1, 25, 3), time=(9, 0, 0, 0)))
defaultEventTimestamps = [0, time_stamp1, time_stamp2, time_stamp3]
defaultCommandTimeArray = [0, TimeStamp(dateTime=DateTime(date=Date(), time=Time())),
                        TimeStamp(dateTime=DateTime(date=Date(), time=Time())),
                        TimeStamp(dateTime=DateTime(date=Date(), time=Time()))
                        ]
defaultEventMessageTexts = ArrayOf(CharacterString)(['','',''])
defaultCommandTime = TimeStamp(dateTime=DateTime(date=Date(), time=Time()))
defaultEventMessageTextsConfig = ArrayOf(CharacterString)(['','',''])

#defaultPriorityArrayValues = [ PriorityValue(null = Null()) for i in range(16) ]
defaultPriorityArrayValues = [
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()), # 8
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    PriorityValue(null = Null()),
    ]

listOfLogDeviceObjectProperties = [DeviceObjectPropertyReference(
                objectIdentifier=("binaryValue", 1),
                propertyIdentifier="presentValue",
            ),
            DeviceObjectPropertyReference(
                objectIdentifier=("datetimePatternValue", 1),
                propertyIdentifier="presentValue",
            )]

singleLogDeviceObjectProperty = DeviceObjectPropertyReference(
                objectIdentifier=("binaryValue", 1),
                propertyIdentifier="presentValue",
            ),