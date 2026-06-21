total_users=int(input("how many total users you want to add : "))
#for example shopkeeper ny  ny 2 users add krny hain 
def add_bill(prices):
    return sum(prices)
def discount(total):
    return total-(total*0.10)
user_list=[]
items_list=[]
total_bill_list=[]
discount_bill_list=[]
for i in range(1,total_users+1):
    # print(f"user{i}")
    user_list.append(f"User {i}")
    
    items=input(f"enter multiple items for user {i} : ").split(",")
    items_list.append(items)
    price=input("enter price of each item : ").split(",")
    int_prices=list(map(int,price))
    print(int_prices)
    total_bill=add_bill(int_prices)
    print(total_bill)
    total_bill_list.append(total_bill)
    if(total_bill>1000):
      discount_bill=discount(total_bill)
      discount_bill_list.append(discount_bill)
      print("you got 10% discount ,after discount bill: ",discount_bill)
    else:
     discount_bill_list.append(total_bill)
     
#user_list,items,total_bill,discount_bill
summary=list(zip(user_list,items_list,total_bill_list,discount_bill_list))
print(summary)

for i in summary:
    print(f"user: {i[0]}") #User 1
    print(f"Items: {i[1]}") #user 1's items
    print(f"total_bill: {i[2]}") #user1's total bill
    print(f"bill after discount : {i[3]}") #user1's bill after discount