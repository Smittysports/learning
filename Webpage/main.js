var isLeftSidebarOpen = 0
var isRightSidebarOpen = 0
 
  function openLeftSidebar() {
    var mySidebar = document.getElementById("leftSidebar")
    var mainSection = document.getElementById("mainSection")
    var myButton = document.getElementById("toggleLeftSidebarButton")

    mySidebar.style.display = "block"
    mySidebar.style.width = "20%"
    mainSection.style.width = "100%"
    myButton.innerHTML = '<img src="../img/LeftArrow.png"/>'

  }
  
  function closeLeftSidebar() {
    var mySidebar = document.getElementById("leftSidebar")
    var mainSection = document.getElementById("mainSection")
    var myButton = document.getElementById("toggleLeftSidebarButton")
    mySidebar.style.display = "none"
    mySidebar.style.width = "0%"
    mainSection.style.width = "100%"
    myButton.innerHTML = '<img src="../img/RightArrow.png"/>'
  }

  function toggleLeftSidebar(){
    if (isLeftSidebarOpen)
        closeLeftSidebar()
    else
        openLeftSidebar()
    isLeftSidebarOpen = !isLeftSidebarOpen
  }

  function openRightSidebar() {
    var mySidebar = document.getElementById("rightSidebar")
    var mainSection = document.getElementById("mainSection")
    var myButton = document.getElementById("toggleRightSidebarButton")

    mySidebar.style.display = "block"
    mySidebar.style.width = "20%"
    mainSection.style.width = "100%"
    myButton.innerHTML = '<img src="../img/RightArrow.png"/>'

  }
  
  function closeRightSidebar() {
    var mySidebar = document.getElementById("rightSidebar")
    var mainSection = document.getElementById("mainSection")
    var myButton = document.getElementById("toggleRightSidebarButton")
    mySidebar.style.display = "none"
    mySidebar.style.width = "0%"
    mainSection.style.width = "100%"
    myButton.innerHTML = '<img src="../img/LeftArrow.png"/>'
  }

  function toggleRightSidebar(){
    if (isRightSidebarOpen)
        closeRightSidebar()
    else
        openRightSidebar()
    isRightSidebarOpen = !isRightSidebarOpen
  }
