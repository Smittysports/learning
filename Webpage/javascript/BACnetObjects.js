
/** This table contains all of the BACnet object types. The table is organized in the
 * following fashion:
 *
 * ID   Object type
 * --   ------------
 * 0    acked-transitions
 * 1    ack-required
 * ...
 * 
 * This is a template to use for a BACnet Property ID. This object can be created and
 * added to the BACnetPropertyIDs table:
 * 
 *   let BACnetObjectType = {
 *       "analog-input": 0,
 *       "analog-output": "1"
 *   }
 */
let BACnetObjectTypes = []

/** Helper method to add a new BACnetObjectType to the BACnetObjectTypes table
 */
function pushObjectTypeToTable(id, name, BACpypesName) {
    let BACnetObjectType = {
        "ID": id,
        "BACnet object name": name,
        "BACpypes object name": BACpypesName
    }
    BACnetObjectTypes.push(BACnetObjectType)
}

/** Get the BACnet object types from the server and display them in a table.
 *
 * TODO: The objects are currently hard coded and placed into a table, these should be
 * retrieved from a server to make sure they are accurate and the data is created
 * in one place.
 */
function getObjectTypes() {
    pushObjectTypeToTable(0, "analog-input", "analogInput")
    pushObjectTypeToTable(1, "analog-output", "analogOutput")
    pushObjectTypeToTable(2, "analog-value", "analogValue")
    pushObjectTypeToTable(3, "binary-input", "binaryInput")
    pushObjectTypeToTable(4, "binary-output", "binaryOutput")
    pushObjectTypeToTable(5, "binary-value", "binaryValue")
    pushObjectTypeToTable(6, "calendar", "calendar")
    pushObjectTypeToTable(7, "command", "command")
    pushObjectTypeToTable(8, "device", "device")
    pushObjectTypeToTable(9, "event-enrollment", "eventEnrollment")
    pushObjectTypeToTable(10, "file", "file")
    pushObjectTypeToTable(11, "group", "group")
    pushObjectTypeToTable(12, "loop", "loop")
    pushObjectTypeToTable(13, "multi-state-input", "multiStateInput")
    pushObjectTypeToTable(14, "multi-state-output", "multiStateOutput")
    pushObjectTypeToTable(15, "notification-class", "notificationClass")
    pushObjectTypeToTable(16, "program", "program")
    pushObjectTypeToTable(17, "schedule", "schedule")
    pushObjectTypeToTable(18, "averaging", "averaging")
    pushObjectTypeToTable(19, "multi-state-value", "multiStateValue")
    pushObjectTypeToTable(20, "trend-log", "trendLog")
    pushObjectTypeToTable(21, "life-safety-point", "lifeSafetyPoint")
    pushObjectTypeToTable(22, "life-safety-zone", "lifeSafetyZone")
    pushObjectTypeToTable(23, "accumulator", "accumulator")
    pushObjectTypeToTable(24, "pulse-converter", "pulseConverter")
    pushObjectTypeToTable(25, "event-log", "eventLog")
    pushObjectTypeToTable(26, "global-group", "globalGroup")
    pushObjectTypeToTable(27, "trend-log-multiple", "trendLogMultiple")
    pushObjectTypeToTable(28, "load-control", "loadControl")
    pushObjectTypeToTable(29, "structured-view", "structuredView")
    pushObjectTypeToTable(30, "access-door", "accessDoor")
    pushObjectTypeToTable(31, "timer", "timer")
    pushObjectTypeToTable(32, "access-credential", "accessCredential")
    pushObjectTypeToTable(33, "access-point", "accessPoint")
    pushObjectTypeToTable(34, "access-rights", "accessRights")
    pushObjectTypeToTable(35, "access-user", "accessUser")
    pushObjectTypeToTable(36, "access-zone", "accessZone")
    pushObjectTypeToTable(37, "credential-data-input", "credentialDataInput")
    pushObjectTypeToTable(39, "bitstring-value", "bitstringValue")
    pushObjectTypeToTable(40, "characterstring-value", "characterstringValue")
    pushObjectTypeToTable(41, "datepattern-value", "datePatternValue")
    pushObjectTypeToTable(42, "date-value", "dateValue")
    pushObjectTypeToTable(43, "datetimepattern-value", "datetimePatternValue")
    pushObjectTypeToTable(44, "datetime-value", "datetimeValue")
    pushObjectTypeToTable(45, "integer-value", "integerValue")
    pushObjectTypeToTable(46, "large-analog-value", "largeAnalogValue")
    pushObjectTypeToTable(47, "octetstring-value", "octetstringValue")
    pushObjectTypeToTable(48, "positive-integer-value", "positiveIntegerValue")
    pushObjectTypeToTable(49, "timepattern-value", "timePatternValue")
    pushObjectTypeToTable(50, "time-value", "timeValue")
    pushObjectTypeToTable(51, "notification-forwarder", "notificationForwarder")
    pushObjectTypeToTable(52, "alert-enrollment", "alertEnrollment")
    pushObjectTypeToTable(53, "channel", "channel")
    pushObjectTypeToTable(54, "lighting-output", "lightingOutput")
    pushObjectTypeToTable(55, "binary-lighting-output", "binaryLightingOutput")
    pushObjectTypeToTable(56, "network-port", "networkPort")
    pushObjectTypeToTable(57, "elevator-group", "elevatorGroup")
    pushObjectTypeToTable(58, "escalator", "escalator")
    pushObjectTypeToTable(59, "lift", "lift")
    pushObjectTypeToTable(60, "staging", "staging")
    pushObjectTypeToTable(61, "audit-log", "auditLog")
    pushObjectTypeToTable(62, "audit-reporter", "auditReporter")
}

/** Load the Property IDs in the BACnetPropertyIDs table into the HTML page.
 * 
 * @param table The HTML table to load the BACnetPropertyIDs table into
 * @param data The BACnetPropertyIDs table to load into the HTML table
 */
function loadBACnetObjectTypesIntoTable(table, data) {
    for (let element of data) {
        let row = table.insertRow();
        for (key in element) {
          let cell = row.insertCell();
          let text = document.createTextNode(element[key]);
          cell.appendChild(text);
        }
      }
}

/** Create a table header to add to the HTML table.
 *
 * For the BACnet Property IDs, the header names are obtained from the table
 * 'keys' of the BACnetPropertyIDs table.
 * 
 * @param table The HTML table to add a table header to
 * @param data  The header data to add to the HTML table
 */
function generateTableHead(table, data) {
    let thead = table.createTHead();
    let row = thead.insertRow();
    for (let key of data) {
      let th = document.createElement("th");
      let text = document.createTextNode(key);
      th.appendChild(text);
      row.appendChild(th);
    }
}

///////////// Code to run when this .js file is loaded in an html file
let htmlTable = document.querySelector("table")
getObjectTypes()
let headerData = Object.keys(BACnetObjectTypes[0]);
generateTableHead(htmlTable, headerData)
loadBACnetObjectTypesIntoTable(htmlTable, BACnetObjectTypes)

