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

# Python Try Except

python try except handles errors in the code ,it controls when something goes wrong or works fine

- try: test the block of code that might cause error(error aaskta h ya nai aaskta)
- catch: runs if error happens
- else:runs if no error happens
- finally:runs in both cases if the error happens or not

## Exception Handling

jab error aata h ya exception(actual error happens in try) aati h q k hum ny exception ko call kia tha to python normally stop ho jay ge aor error messsage generate kry ge

- Exception means the actual error happens in try block
- exception will be handled in except block
- if try block raises an eror except block will run
- without try block the program will crash and raise error
- with try except block message will apear instaed of error
- bcz we are handling the error happens in try block
- to show multiple error msgs we can use as many exception blocks as we want
- python dont allow us to use multiple blank except blocks
- we need to use multiple exception types in seprate except blocks except with the last one

### NameError(exception type)

is a specific type of error in python it happens when we use variable,class or function that we nevr defined

### Exception as e

we can use in except block to chk what exct error is in try block

#### Note :

we can study more error types or built-in exceptions on w3 schools

## Else

if try block does not generate any error the else code block will run

## finally

- finally code block will msut run regardless of if the error happens or not
- sometimes we need to run a code in both casses if the error happens or not
- like the following cases
  - close the file
  - clear the resources
  - close DB connection
  - print final message

# More about file handling

## 1. Exception Handling with Files

         already done

## 2. File Paths — os and pathlib

- both work with any file type txt, csv, json, pdf, etc. They don't care about the file type, they just work with paths and folders.
- we already studeied os.remove() and os.path.exist() but we have much more
- os only manages file/folders(create,delte,rename,chk if paths exist etc)
- pathlib is a modern cleaner way to work with file paths instead of os
- pathlib do all what os do but os cant read/write files pathlib can
- pathlib read/write text/binary files without using open()

## 3. Working with CSV Files

- CSV- stands for comma seprated values
- they are the files we use to store data in rows and columns by seprating them using comma
- we can read them or write into them using
  - csv.reader(f) #read
  - csv.writer(f) #write
- both take file object as an argumnt
- reader() dont directly return data as normaly read() function do in txt

- instead reader will return an object
- it read the data row by row so we need to loop through it
- writer() also return an object instead we use .writerow() or writerows() function to write a row or rows in a file
- reader frst convert csv data into python list wich should must have comma seprated data,csv can have any seprator
- writer convert that list back to csv
- they alos works like json functions

## 4. Working with JSON Files

- json.load(f)
  - it necassirly take only one parameter ,file object the file which we open in read mode
    data=json.load(file)
  - we have content in the opened file wich is "file" and we are loading that opened file and storeing that in data
  - now we have content in "data"
  - read json file and convert it into python structure
  - it convert json->python and read the json file at the same time
- json.dump(data,f)
  - it necassirily take two arguments
    file object(the file wich we opend in write mode and the data object) & data object containing content
    json.dump(data,file)
  - it write into the file and convert that python file back into json structure
  - it convert and writes into json file at the same time
  - indent etc are optional for formatting

## 5. File Handling with shutil

- we import use this module to copy,move,archieve files
- frst we import this built-in modeule and then use its functions
- it also provide a function to dlete a non-empty folder bcz use it as alternatove of
  os.remove() bcz wo srf empty folders ko remove krta h

## 6. Reading/Writing Binary Files

we read/write the binary files same as we read/write txt files but they are for images

- data=fileobj.read() read should have no argument in both txt/binary cases
- fileobj.write(data) should must have data object the file wich is containing images/data as an argument
- fileobj.write()

## 7. File Seeking — seek() and tell()

- tell() - f.tell() tells us the current position of the cursor
- takes no argument
- by default 0 say start hota h
- seek()- f.seek(n) moves the cursor the position n
- if n is 10 it will move cursor from 0 to 10
- takes number of character as an argument where we want to move cursor
- cursor 0 sy n tak jump kry ga
- tell() and seek() both start counting from 0 not 1

## 8. Temporary Files

- we need to import built in module frst to create temp files
- module name is tempfile
- we dont need to open such files using open()
- instaed we use NamedTemporaryFile() modeule provided function this function open ,create and generate name and path of the temporary file automaticaly on our system
- temporary files wo files hoti hain jin main hum wo data write krty hain jo humy srf temporarily chaiy during the program
- we use them like a rough paper we solve our problem and then through them away
- yeh program close hony par automaticly dlete ho jati hain until hum ny tempfile.NamedTemporaryFile k argumnt main dlete=False nahi set kia
- in files main hum data bytes format main likhty hain like string sy phly "b"use krna hota h
- most of the time in files main write he kia jata h
- rare cases main read kia jata h in files ko
- temporary file srf or srf during the execution of program exist krti h us k forn baad delte ho jati h
- file exist kry ge jab tak "with"block run horha h incase delte=False kia hoa h
- delete=True case main hum us link pr jaa kr us ko vist krsty hain wo program execution k baad bhi exist kry ge

#### Note: write("txt") function returns the number of bytes written in the file if we wrint it it will print number of bytes

#### Note: 1 character = 1 bytes for normal english txt(count number of bytes in a string)
