# =============================================================================
# Python commands
# =============================================================================

# To add a single line comment
Ctrl + 1 to 

# To add a multiline comment
Ctrl + 4
or you can use 3 quote to add a multiline comment e.g. """ some text """

# To remove the multiline comment
Ctrl + 5

# To clear the console
Ctrl + L

# To close a ta
Ctrl + W 

# To clear the environment 
import sys
sys.modules[__name__].__dict__.clear()

# to exit python from Command prompt
quit() or Ctrl + z 

# =============================================================================
# CMD commands
# =============================================================================

# to see what's inside a directory
dir

# to enter a folder. 
cd 'name of the folder'

# to get to the top of the directory tree
cd\ 

# to get one folder up/behind
cd..

# to get to another drive
d: # to get to D drive
e: # to get to E drive
f: # to get to F drive

# to change both drive and directory (use /d command) e.g.
cd /d C:\Windows

# NOTE: By typing only the drive letter you automatically move to your most 
# recent location on that drive. For instance, if you are on "D:" drive and 
# type "cd c:\windows" nothing seems to happen. However, if you type "c:" 
# then the working folder changes to "c:\windows," assuming that it was the
# last folder you worked with on your "C:" drive.

# to make a new folder
md 'name of the new folder'
# you can also type md 'the entire path to the desired folder' e.g. 
md E:\a_folder\another_folder

# to rename a folder (similar command for any file)
ren 'Folder' 'NewFolderName'

# to copy a file
copy 'location\filename.extension' 'newlocation\newname.extension'

# To copy a folder and its content from a location to another
# The "/s" parameter ensures that all the directories and subdirectories 
# are going to be copied, except the ones that are empty. 
# The "/i" creates a new directory if destination folder does not exist
xcopy /s /i 'the folder that is to be copied' 'where it will be sent'

# to remove a folder
RD 'name of the folder to be deleted'

# to remove a file
del 'location\filename.extension'

# to get help
help
# it shows all the available commands you can use. 

# If a particular command interests you, type help followed by the name of 
# that command. Another way to do the same thing is to type the command's 
# name followed by the "/?" parameter. To test it, use "help cd" or "cd/?" 
# to display information about the cd command. 

# to clear a screen
cls
