"""
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename and mode.
There are four different methods (modes) for opening a file

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

Syntax
    f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
    f = open("demofile.txt")

"""
import os
import datetime
# read a file
try:
    f = open("file.txt", "rt")
    print(f.read())
except Exception as e:
    print(f"{type(e)}: {e}")
finally:
   f.close()

# read part of a file
try:
    f = open("file.txt", "rt")
    for line in f:
        print(line[2:7])
except Exception as e:
    print(f"{type(e)}:{e}")
finally:
    f.close()


"""
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""
try:
    f = open("file.txt", "at")
    f.write(f"\n\nThis is is some additional content\n Written on: {datetime.date.today()}")
    f.close()
except:
    raise Exception("Problem writing to file")
else:
    f = open("file.txt", "rt")
    # print(f.read())
finally:
    f.close()


"""
Create a New File
To create a new file in Python, use the open() method, with one of the following 
parameters:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
"""
try:
    f1 = open("file2.txt", "wt")

    sth = "To construct a random narrative, we first imported the random module, then built sections of the stories in separate lists, then randomly picked portions of the lists. As a beginning, you are more interested in developing software applications, which is understandable. \n"

    f1.write(sth)
except:
    raise Exception("There was a problem creating your file")
else:
    # print(f1.read())
    print("Written successfully")
finally:
    f1.close()

# Delete a file
try:
    if os.path.exists("file2.txt"):
        os.remove("file2.txt")
    else:?!?jedi=0, ?!?    (*_**values: object*_*, sep: Optional[str]=..., end: Optional[str]=..., file: Optional[SupportsWrite[str]]=..., flush: bool=...) ?!?jedi?!?
        print("File already deleted!")
except:
    print("The file does not exist")

