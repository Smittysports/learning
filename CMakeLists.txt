cmake_minimum_required(VERSION 3.10)
project(learning)

# here we specify the additional include directories for the project.
include_directories(${CMAKE_SOURCE_DIR})
include_directories(${CMAKE_SOURCE_DIR}/Templates)
include_directories(${CMAKE_SOURCE_DIR}/Threading)
include_directories(${CMAKE_SOURCE_DIR}/Examples)
include_directories(${CMAKE_SOURCE_DIR}/FactoryPattern/General)

# here we specify the additional library directories for the linker in the project. 
#link_directories("${CMAKE_SOURCE_DIR}/path")

# here we add definitions for any package if requred.
#add_definitions(${PCL_DEFINITIONS})

# The following line is very important.
# It specifies the executable name. Here the executable is the first parameter
# Followed by the executable name come all your source and header files.
# All cpp fles will be clubbed into source folder and all .h files will be added to header files folder of the project.
add_executable (learning Main.cpp 
    ${CMAKE_SOURCE_DIR}/Threading/ThreadPool.cpp 
    ${CMAKE_SOURCE_DIR}/Examples/Initialization.cpp 
    ${CMAKE_SOURCE_DIR}/Examples/MoveSemantics.cpp 
    ${CMAKE_SOURCE_DIR}/FactoryPattern/General/ShapeCreator.cpp)

# There may be some additional dependencies which you may have to specify for the project, which you may do as in following lines.
# Note that first parameter is the executable name.
#target_link_libraries (learning ${PCL_LIBRARIES} libeng.lib libmx.lib libmex.lib libmat.lib Aria.lib winmm.lib wsock32.lib)
# Add the required libraries for linking:
#TARGET_LINK_LIBRARIES(${sampleName}
#${MRPT_LIBS} # This is filled by FIND_PACKAGE(MRPT ...)

set_target_properties(learning 
    PROPERTIES
    OUTPUT_NAME "learning"
    CXX_STANDARD 20
    COMPILE_FLAGS "-g -Wall -Wextra"
)