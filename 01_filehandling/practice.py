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
#     file.write("\n now the file has more content")
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
import os
#remove file
# os.remove("newdemofile.txt")
#chk if it exist or not
if  (os.path.exists("newdemofile.txt")):
    os.remove("newdemofile.txt")
else:
    print("file does not exist")


 