#----------------------------------------#
#Question 5
#Level 1

#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class my_class:
    def __init__(self):
        self.my_string=""
    def getString(self):
        
        self.my_string=input("Enter a string : ")
      
    def printString(self):
        
        upper_case=self.my_string.upper()
        print(upper_case)
   

myObj=my_class()
myObj.getString()
myObj.printString()


#self refers to teh current object