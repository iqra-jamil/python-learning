python has saveral functions for
creating,reading,update,deleting the files

# File Handling

- the key function we use while working with files is open() function

- open() function takes two parameters
  (filename,mode)

- there are 4 diffrent methods or modes to open a file
  - read : (r)default value,agr hum aik aisi file ko read krny ke koshish krty hain jo exist he nai krti to it will give an error
  - write:(w)agr aap file ko write krny k liy open krty ho or wo file exist he nai krti to wo file create ho jay ge
  - append:(a)same for append
  - create:(x) agr hum aik aisi file ko create krny ke koshish krty hain jo alredy exist (same name k sath) krti hai to it will give an error

### note:

we will be covering delte later also the details of these methods

we can also specify k hamri file ko binary mode main hona chaiy ya text mode main

- t -text mode (default value)
- b -binary mode (for images)

# Syntax

- to open a file for reading its enough to specify onlt the file names bcz
- r is the defalut value
- same for text t is also defalut value if yu want to open a file in text format
- in python we can write the file name in single or double quote both will work

# Python File Open

## Open a File on the Server

- to open a file simply use open function
- open function does not directly give us th file content
- instead open function will give us a tool (object file)
- and then object file will have a read() method to read the file

### file path and location:

- if the file we are handling is in the same folder as of python we can simple give file name with extension
- but if its in diffrent location from that then we will have to specify full path

# Using the with statement

- we can also use 'with statement' with open function so that we dont have to close the file after working with it with satement take care of that.

### Close Files

- its a good practice to close the files after working in them
- if we are not using with sattemnt we will ahve to use close() to close the file
- once we closed the file using close we cant read it now

#### Note: You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.

## Read Only Parts of the File

read() entire file ko read ya entire file cintent ko return krta h but hum kuch number of characters bhi read(8) main specify kr skty hain

## Read Lines

- we can return or read one line by using readline() method
- we can read two lines by calling it 2 times
- if we want to return/read a documnt line by line instaed of as a whole through the file line by line

# Python File Write

## Write to an Existing File

writing to an existing file includes
append and write to a file

- write (w)- will override existing content
- append (a)- will append to the end of file

## Create a New File

to create a file use open() with one of the following parameter

- x will create file and give error if the specified file alredy exist
- a will craete a file if the specified file does not exist
- w same as above

# Python Delete File

## Delete a File

- to delet a file we need to import os module
- then using os.remove("filepath") we can dlt it
- we can also chk if the file exist or not using os.path.exists("filepath")

## Delete Folder

- we can delete a folder using os.rmdir()
- we can only remove the empty folder
- if we will not chk the path then we will try to remove the file wich dont exist it will give an error
