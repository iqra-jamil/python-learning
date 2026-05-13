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
#Try to open and write to a file that is not writable:(in file handling)
