var isSidebarOpen = 0

/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openSidebar() {
    var mySidebar = document.getElementById("mySidebar")
    var mainSection = document.getElementById("mainSection")
    var myButton = document.getElementById("toggleSidebarButton")

    mySidebar.style.display = "block"
    mySidebar.style.width = "20%"
    mainSection.style.width = "80%"
    myButton.innerHTML = '<img src="../img/RightArrow.png"/>'

  }
  
  /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
  function closeSidebar() {
    var mySidebar = document.getElementById("mySidebar")
    var mainSection = document.getElementById("mainSection")
    var myButton = document.getElementById("toggleSidebarButton")
    mySidebar.style.display = "none"
    mySidebar.style.width = "0%"
    mainSection.style.width = "100%"
    myButton.innerHTML = '<img src="../img/LeftArrow.png"/>'
  }

  function toggleSidebar(){
    if (isSidebarOpen)
        closeSidebar()
    else
        openSidebar()
    isSidebarOpen = !isSidebarOpen
  }