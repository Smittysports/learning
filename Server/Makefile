# Main Makefile for BACnet server
APP				= server
OBJDIR			= obj
SOURCE_FILES	= Main.cpp
OBJECT_FILES    = $(SOURCE_FILES:%.cpp=$(OBJ)/%.o)
EXECUTABLE_DIR  = bin
OBJS    		= $(patsubst %.c,$(OBJDIR)/%.o,$(SRCS))

default: all

# This is the default target, which will be built when you invoke make
all: $(APP)

$(APP): $(SOURCE_FILES) $(OBJS)
	if not exist $(EXECUTABLE_DIR) mkdir $(EXECUTABLE_DIR)
	g++ $(OBJS) -o $(EXECUTABLE_DIR)/$(APP) $(SOURCE_FILES)

# This rule tells make to copy Main to the binaries subdirectory, creating it if necessary
#install:
#    mkdir -p binaries
#    cp -p Main binaries

# This rule tells make to delete the bin directory
clean: 
	rmdir /Q /S $(EXECUTABLE_DIR)

