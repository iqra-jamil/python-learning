# Python Iterators

- What is an iterator?
  - an object that returns values one by one

  - iterator has two methods : -**iter**():returns an iterator object
    - an iterator obj is python obj that remembers current position and gives us next value when we call **next**()
    - iter simply sets the starting point at the beginning.
    - **next**(): returns next values ,raises StopIteration when there is no more value in the sequence
    - use \_ befor and next to iter() and next()

- Iterators vs Loops
  - A loop is not an iterator
  - loop call iter and next behind the secne secretly
  - we use iterors when we want to pause and resume
  - a loop cant be pause in the middle like iterators
  - A loop is a tool/syntax, an iterator is an object
  - Loops use iterators behind the scenes automatically
- Why use iterators instead of loops?
  - When you need to pause and resume getting values
  - When data is huge → iterator gives one item at a time, saves memory
  - When data has no index → files, streams, generators can't be accessed by index
  - Indexing is slower, iterator just moves faster
- Countable number of values means:
  - Values come in order, one after another (1st, 2nd, 3rd...)
  - Does NOT mean you know the total count
  - Just means the sequence is ordered and defined

## Iterator vs Iterable

- Lists, tuples, dictionaries, and sets are all iterable objects.
- when we call iter() on an iterable container we get an iterator (we discussed iteratr before)
- Even strings are iterable objects, and can return an iterator
- hamary pass iterable object hoti hai us par hum iter() function call krty hain or wo humy iterator return krta h

## Looping Through an Iterator

we can also use loop to loop through an iterable objects (strings too)

### note: wo data jis main indexing nai hoti wo bhi iterable objects hoti hain like files,streams geneartors

### we use iter() function to call **iter**()(underscores) method, is the clean way to call it (same for next)

## Create an Iterator

- Normal methods we call manually by name, but **iter** and **next** are called automatically by Python when we use iter() and next()
- **iter** and **next** are just methods of a class like **init**
- python automaticaly calss init and next method when we use init() and next() functions on object
  - iter(obj) → calls obj.**iter**()
  - next(obj) → calls obj.**next**()
- we define them inside your class just like any normal method, Python handles the rest.
- we use iter to initialize values and to perform some actions and we can use next to perform operations

## StopIteration

- when there are no more values in a sequence (iterable object), it raises StopIteration
- or we oursleves can use To prevent the iteration from going on forever, we can use the StopIteration statement.in case we dont have defined sequence
- In the **next**() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times
- use raise keywrd with stopIteration else it will return none instaed of raising err

# Python Generators

- A generator is a function that uses yield instead of return , it produces values one at a time, pausing between each.
- Why use them? Memory efficiency — instead of building a whole list, values are created on demand.
- lazy evaluation. Use generators when your data is large or you only need one value at a time.

- generator is an iterator itself so we dont need to call iter on it
- we call iter when we need to convert something into iterator like a list into iterator

### Note : hasattr checks whether an object has a specific attribute or method.hasattr checks whether an object has a specific attribute or method.

### syntax :hasattr(obj, 'name') # returns True or False

### An object is only called an iterator if it has both **iter**() and **next**() methods defined inside it. That is called the iterator protocol.
