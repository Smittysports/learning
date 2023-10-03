var isSidebarOpen = 0

/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openSidebar() {
    var mySidebar = document.getElementById("mySidebar")
    mySidebar.style.display = "block"
    mySidebar.style.width = "25%"
    document.getElementById("mainSection").style.width = "75%"
    document.getElementById("toggleSidebarButton").value="Close sidebar";

  }
  
  /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
  function closeSidebar() {
    var mySidebar = document.getElementById("mySidebar")
    mySidebar.style.display = "none"
    mySidebar.style.width = "0%"
    document.getElementById("mainSection").style.width = "100%"
    document.getElementById("toggleSidebarButton").value="Open sidebar";
  }

  function toggleSidebar(){
    if (isSidebarOpen)
        closeSidebar()
    else
        openSidebar()
        isSidebarOpen = !isSidebarOpen
  }