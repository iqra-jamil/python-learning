#Question 17
#Level 2
#Question:
#Write a program that computes the net amount of a bank account based a transaction log from console input.
#The transaction log format is shown as following:
#D 100
#W 200
#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:
#D 300
#D 300
#W 200
#D 100
#Then, the output should be:
#500


my_balance=0
while True:
    user_input=input("Enter D or W with amount : ")
    if not user_input:
        break
    mode,amount=user_input.split(" ")
    int_amount=int(amount)
    if(mode=="D"):
      my_balance+=int_amount
    if(mode=="W"):
     my_balance-=int_amount
print(my_balance)

 
  















########################### README.md################################

#1.Take two inputs from user aik he single input main ya to D amount ya to W amount 
#2.D ho ga to us k sath ke amount add to balance ho ge 
#3.W ho ga to us k sath k amount subtract from balance ho ge
#4. End py balance print ho ga 
#5.Agr hum emptiness ko chk karny say phlyt split use kren gy to wo humy emty string dy ga or hamri loop kabi b exit ya break nai ho ge 
#6.So we will split input after cheking emptiness and jab input split ho jati h to we can have two variables for that single input statmnt
# we will use while True instead of for loop cz we have no clue when the user will stop entring
  