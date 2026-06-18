### Decorators + Context managers +Map + Filter + Zip + Dunder methods

# Decorators:

- Decorator is a function jo aik dusry function ko apny andr wrap krta h to add some extra functionality or behaviour without chainging its orignal code
- in simple way we can say that decorator function us extra functionality waly function ko apny andr as an argument ly rha hota h
- @ use kia jata h with decoratr function's name just before the definetion of secnd function(extra functionality wala func)

- jis function k andr extar functionality add krni h whi decoratr ho ga
- decorator function alwys needs to returns a new function bcz new functionality add hoe h
- so decoratr function k andr aik function bny ga us k andr he who extra feature wala function call ho ga or phir wohi return b ho ga
- hum decoratr function ko kbi b call nai karty @my_decoratr automatically yeh kaam krta h

# Context managers

- a context manager handles setup and cleanup of resources automatically using "with" statement
- resources like files,networks, locks or connections anything that need to be open and close
- without context manager humy resources like files ko manualy close krna parta h like f.close() use kr k lkn agr code block main error ajata h to file close nai ho ge
- context manager main with statemnt is ko handle krhi hoti h so code block main error aabhi jay file close ho jati h

# map()

- we use map to apply sepcific function on each item in an iterable (list,dict,tuple etc) without using for loop
- one line code
- map() itself returns a map obj instead of actual values
- so we wrap it into a list which force it to compute and show the actual values

# filter()

- filter keeps only the items of an iterable that met the specific condition
- filter func return True for the items , met the condition
- filter func return False for the items ,don't met the condition
- will keep the items with value True and drop the items with value False
- just like map filter() will also return filter obj instaed of actual values so we just need to wrap it into a list

### map and function takes two things as an argumnt function and iterable

# zip()

- zip() multple iterables ko combine krta h
- iterables k items ko same position par pair up kr k
- first item from frst iterable will pair up with frst item of the secnd iterable ,seond item from frst iterable will pair up with second item of the secnd iterable and so on
- agr iterbles ke length different h to zip() stops at the shortest one
- iterables ke type differnt ho skti h
- like we can combine items of a list with items of a tuple
- zip() will return zip() obj just like filter and map() so we need to wrap it in a list to see its actual values
- it will return a list of tuples when we wil apply list()

# zip() takes two iterables as an arg

### note we can use tuple(),set() too instaed of list() to view the results or even we can loop over results without using anyof them ,list() is jsut a common way to view results

# Dunder method

- Dunder is short for double underscore
- they are special methods start and end with dble underscore
- they are call automatically in specific condition , we dont need to call them manually
- some common methods like:
- **init** : runs when an object is created - **str** when we print an object
- **len** : run when we call len() function on an obj
- **eq** : when we compare two objects using ==
- **add** : runs when we use + one two objects
- they matter in classes/objects (OOp) only
- they wrok on objects not on plain variables
