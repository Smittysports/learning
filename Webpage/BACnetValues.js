
/** This table contains all of the BACnet Property IDs. The table is organized in the
 * following fashion:
 *
 * ID   PropertyName
 * --   ------------
 * 0    acked-transitions
 * 1    ack-required
 * ...
 * 
 * This is a template to use for a BACnet Property ID. This object can be created and
 * added to the BACnetPropertyIDs table:
 * 
 *   let BACnetPropertyID = {
 *       "ID": 0,
 *       "PropertyName": "acked-transitions"
 *   }
 */
let BACnetPropertyIDs = []

/** Helper method to add a new BACnetPropertyID to the BACnetPropertyIDs table
 */
function pushPropertyToTable(id, name) {
    let BACnetPropertyID = {
        "ID": id,
        "PropertyName": name
    }
    BACnetPropertyIDs.push(BACnetPropertyID)
}

/** Get the BACnet Property IDs from the server and display them in a table.
 *
 * TODO: The IDs are currently hard coded and placed into a table, these should be
 * retrieved from a server to make sure they are accurate and the data is created
 * in one place.
 */
function getPropertIDs() {
    pushPropertyToTable(0, "acked-transitions")
    pushPropertyToTable(1, "ack-required")
}

/** Load the Property IDs in the BACnetPropertyIDs table into the HTML page.
 * 
 * @param table The HTML table to load the BACnetPropertyIDs table into
 * @param data The BACnetPropertyIDs table to load into the HTML table
 */
function loadPropertIDsIntoTable(table, data) {
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
getPropertIDs()
let headerData = Object.keys(BACnetPropertyIDs[0]);
generateTableHead(htmlTable, headerData)
loadPropertIDsIntoTable(htmlTable, BACnetPropertyIDs)

