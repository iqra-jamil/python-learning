print("file handling")
#-Syantax of open function
#f=open('demofile.txt','r')
#or
#f=open("demofile.txt","rt")
#both are same 
#-with with statemnt
# with open("demofile.txt","rt") as f:
#-without with statemnt
#f=open("demofile.txt","rt")
#print(f.read(5))
#print(f.readline())
#print(f.readline())
#f.close()
#print(f.read()) #error 
#-reading entire doc line by line 

# with open("demofile.txt","rt") as file :
#     for x in file:
#         print(x)

#open and append(will add new content at the end)
# with open("demofile.txt","a") as file:
#     print(file.write("\n now the file has more content"))
# #open & read the updated file
# with open("demofile.txt") as file:
#     print(file.read())
#open & write (will overide the existing content)
# with open("demofile.txt","w") as file:
#     file.write("overrided existing content")
# with open("demofile.txt") as file:
#     print(file.read())
#- craeting new file and adding some content and reading that content
# with open("newdemofile.txt","x") as file:
#     print(file)
# with open ("newdemofile.txt","wt") as file:
#     file.write("adding some content in the newly craeted file")
# with open("newdemofile.txt","rt") as f:
#    print(f.read())
# import os
# #remove file
# # os.remove("newdemofile.txt")
# #chk if it exist or not
# if  (os.path.exists("newdemofile.txt")):
#     os.remove("newdemofile.txt")
# else:
#     print("file does not exist")
## file seeking (to figure out whre the cursor is)
# with open("demofile.txt" ,"rt") as f :
#  print(f.tell())
#  print(f.read(5))
#  print(f.seek(10))
#  print(f.read(8))
#  print(f.tell())
## temporary files
# import tempfile
## temporary files
# with tempfile.NamedTemporaryFile(delete=False) as tmp:
#     print(tmp.write(b"MY temporary file"))
#     print(tmp.name)

## working with shutill
# import shutil
# #will take 2 argumnts the file we want to copy and the dest file/folder where we want to paste it
# shutil.copy("src","dest")
# # same as above
# shutil.move("src","dst") 
# #take only folder path as argumnt we want to dlete
# shutil.rmtree("folderpath") 
# #will take zip file name ,format like zip/tar(use in mac/linux) , and the folder we want to zip
# shutil.make_archive("basname","zip","root_dir")
## csv- comma seprated vallues
#import csv

# with open("data.csv","r" ) as f:
#   reader=csv.reader(f)

#   for row in reader:
#     print(row)
# with open("data.csv","a"  ,newline="") as f:
#      writer=csv.writer(f)
#      #writer.writerow(["iquu", 24, "khewra"]) 
#      writer.writerows([["ii",68,"lhr"],["list2",5,"jjsj"]])

## os- operating system
# import os
# print(os.getcwd()) #returns current folder
# #join folder and files names into proper path safety
# print(os.path.join("python-learning","01_filehandling","demofile.txt")) 
# #foldername ,subfoldername,subfile
# #extract just the file name from the full path shoudn't write only file name 
# print(os.path.basename(r"C:\Users\decent\OneDrive\Desktop\python-learning\01_filehandling\data.csv"))
# #will return a folder before a folder like :C:/Users/decent
# print(os.path.dirname("C:/Users/decent/01_filehandling"))
# #returns all a list of all the folder and  files inside a folder
# print(os.listdir(r"C:\Users\decent\OneDrive\Desktop\python-learning\01_filehandling"))
# #os.makedirs("a/b/c") craeted nested folders all at once a inside b and c inside b
# os.makedirs("a/b/c") 

## pathlib
from pathlib import path
# creates a path object from the given path string
p=path("path")
#it chks if the file/folder exist or not return True/False
p.exists()
#reads and returns the file content as string
p.read_text() #read txt files
#writes the given string to the file

p.write_text("data likho") #write into txt files
#chks folder name of the file (jo hum ny path() main dia hoa h)
p.parent
#returns file extension like .txt
p.suffix 
#to read/write binary files like imagesand PDfs we can use :
p.read_bytes()
p.write_bytes()


