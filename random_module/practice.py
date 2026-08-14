import random 
# including 0,10
print(random.randint(0,10))
# excluding 10 and also support steps
print(random.randrange(0,10))

#random.choice() → selects one random item, takes sequenec as an argumnt 
# random.choices() → selects multiple random items and can repeat items,takes sequence as an argumnt

# shuffle()	Takes a sequence and returns the sequence in a random order,takes a squence as a parameter
# random returns random float betwen 0 and 1 (takes no argumnt)


# consult https://www.w3schools.com/python/module_random.asp for more 

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print(random.choice(days))
# print(random.choices(days, k=5))
random.shuffle(days)
print(days)