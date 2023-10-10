
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
function pushObjectTypeToTable(id, name) {
    let BACnetObjectType = {
        "ID": id,
        "PropertyName": name
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
    pushObjectTypeToTable(0, "analog-input")
    pushObjectTypeToTable(1, "analog-output")
    pushObjectTypeToTable(2, "analog-value")
    pushObjectTypeToTable(3, "binary-input")
    pushObjectTypeToTable(4, "binary-output")
    pushObjectTypeToTable(5, "binary-value")
    pushObjectTypeToTable(6, "calendar")
    pushObjectTypeToTable(7, "command")
    pushObjectTypeToTable(8, "device")
    pushObjectTypeToTable(9, "event-enrollment")
    pushObjectTypeToTable(10, "file")
    pushObjectTypeToTable(11, "group")
    pushObjectTypeToTable(12, "loop")
    pushObjectTypeToTable(13, "multi-state-input")
    pushObjectTypeToTable(14, "multi-state-output")
    pushObjectTypeToTable(15, "notification-class")
    pushObjectTypeToTable(16, "program")
    pushObjectTypeToTable(17, "schedule")
    pushObjectTypeToTable(18, "averaging")
    pushObjectTypeToTable(19, "multi-state-value")
    pushObjectTypeToTable(20, "trend-log")
    pushObjectTypeToTable(21, "life-safety-point")
    pushObjectTypeToTable(22, "life-safety-zone")
    pushObjectTypeToTable(23, "accumulator")
    pushObjectTypeToTable(24, "pulse-converter")
    pushObjectTypeToTable(25, "event-log")
    pushObjectTypeToTable(26, "global-group")
    pushObjectTypeToTable(27, "trend-log-multiple")
    pushObjectTypeToTable(28, "load-control")
    pushObjectTypeToTable(29, "structured-view")
    pushObjectTypeToTable(30, "access-door")
    pushObjectTypeToTable(31, "timer")
    pushObjectTypeToTable(32, "access-credential")
    pushObjectTypeToTable(33, "access-point")
    pushObjectTypeToTable(34, "access-rights")
    pushObjectTypeToTable(35, "access-user")
    pushObjectTypeToTable(36, "access-zone")
    pushObjectTypeToTable(37, "credential-data-input")
    pushObjectTypeToTable(39, "bitstring-value")
    pushObjectTypeToTable(40, "characterstring-value")
    pushObjectTypeToTable(41, "datepattern-value")
    pushObjectTypeToTable(42, "date-value")
    pushObjectTypeToTable(43, "datetimepattern-value")
    pushObjectTypeToTable(44, "datetime-value")
    pushObjectTypeToTable(45, "integer-value")
    pushObjectTypeToTable(46, "large-analog-value")
    pushObjectTypeToTable(47, "octetstring-value")
    pushObjectTypeToTable(48, "positive-integer-value")
    pushObjectTypeToTable(49, "timepattern-value")
    pushObjectTypeToTable(50, "time-value")
    pushObjectTypeToTable(51, "notification-forwarder")
    pushObjectTypeToTable(52, "alert-enrollment")
    pushObjectTypeToTable(53, "channel")
    pushObjectTypeToTable(54, "lighting-output")
    pushObjectTypeToTable(55, "binary-lighting-output")
    pushObjectTypeToTable(56, "network-port")
    pushObjectTypeToTable(57, "elevator-group")
    pushObjectTypeToTable(58, "escalator")
    pushObjectTypeToTable(59, "lift")
    pushObjectTypeToTable(60, "staging")
    pushObjectTypeToTable(61, "audit-log")
    pushObjectTypeToTable(62, "audit-reporter")
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

