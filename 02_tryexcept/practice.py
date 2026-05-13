#print("try except")

x=9;
try:
 print(x)
except NameError:
 print("x is not defined")
except:
 print("something else went wrong")
else:
 print("nothing went wrong")
finally:
 print("close the file")
#Try to open and write to a file that is not writable(never opened in write mode its in read mode only ):(to practice try,except,finally)

try:
 f=open("demofile.txt")
 try:
  f.write("add content")
 except:
  print("something went wrong")
 else:
  print("evrthing went fine")
 finally:
  f.close()
  #bcz open call it self failed so f was never assigned that is why finaly will throw eror so we need to handle that error too(open call failed not bcz file was not writeable but bcz file didnt exist at  that time so file was not opening in the read mode ) so that is why it was executing outer except
except:
 print("something else went wrong")
#this will only control the error it will not close the file bcz nothing was opened as f was nevr assigned 

# try:
#  f=open("demofile.txt")
#  try:
#   f.write("add content")
#  except Exception as e:
#   print(e)
#  else:
#   print("all well")
#  finally:
#   f.close()
# except:
#  print("something else went wrong")
# else:
#  print("all well")
try:
   f=open("demofile.txt")
   f.write("add content")
except Exception as e:
   print(e)
finally:
  f.close()
