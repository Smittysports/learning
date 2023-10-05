# Main Makefile for BACnet server
APP				= server
OBJDIR			= obj
SOURCE_FILES	= Main.cpp src/Networking.cpp
INCLUDES		= -Iinclude
OBJECT_FILES    = $(SOURCE_FILES:%.cpp=$(OBJ)/%.o)
EXECUTABLE_DIR  = bin
OBJS    		= $(patsubst %.c,$(OBJDIR)/%.o,$(SOURCE_FILES)) # Used for putting the objects in another directory
CXXFLAGS		= /std:c++20 /EHsc -Wall /wd4668 /wd4100
CC				= cl
default: all

# This is the default target, which will be built when you invoke make
all: $(APP)

$(APP): $(SOURCE_FILES)
	@if not exist $(EXECUTABLE_DIR) mkdir $(EXECUTABLE_DIR)
	$(CC) -o $(EXECUTABLE_DIR)/$(APP) $(SOURCE_FILES) $(CXXFLAGS) $(INCLUDES)

# This works with Windows cl	
#$(CC) $(SOURCE_FILES) $(CXXFLAGS)
# Old way, doesn't work withh C++20 yet
#g++ $(OBJS) -o $(EXECUTABLE_DIR)/$(APP) $(SOURCE_FILES)

# This rule tells make to copy Main to the binaries subdirectory, creating it if necessary
#install:
#    mkdir -p binaries
#    cp -p Main binaries

# This rule tells make to delete the bin directory
clean: 
	rmdir /Q /S $(EXECUTABLE_DIR)

run: server
	./bin/server.exe

