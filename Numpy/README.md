# Introduction to NumPy Library in Python

- Numpy stands for numerical python
- basic use of numpy is working with arrays
- we use it to convert raw data into useful insights
- for scientific computing,data anlysis,numerical compputing tasks,ML
- for example in ML we use it to convert raw dataset in to useful dataset
- use package manager/installer to install it like other libraries
- ### array is the most fundamental object in numpy
- we store data in multidimenstiosal arrays ndarray like 1d array,2d array,3d array
- we can perform mathematical operations on data through arrays
- arrays main ## contigious memory ## allocation hoti h
  like in 1d array [1,2,3,4,5]
  lets say every elemnt is of 2 byte in this array
  if frst item will get 100 location the nxt item will get 101 and nxt wil get 102 upto so on
  or 100,102,104,106....
- in 2d arrays rows are called height and columns are width
- 3d arrays main height, width ,depth aaty hain
- array main hum structuctured data bhi store krskty hain jesy DBMS main table ke form main data store hota h
- we can store float ,int etc too not only arrays in numpy
- arrays support homogeneous data (entire data should have same dataype)
- in case we want to store data of diffrent dataypes we will use lists in py

# List vs Arrays in Python

- Arrays - all the elements should have same data type ex:[1,2,3]
  lists- elements can have different datatypes ex:[1,2.4,"hello"]
  #### how elements are stored in memory
- Arrays - contigious memory allocation example:100,101,102...
  - List - non-contigious memory allocation ex: 101,500,102...
- Arrays - searching can be easy but insertion or deletion can be difficult
  - Lists - searching can be bit complex but insertion deletion can be easy
- ARrays - are static cant be resize
  - Lists - can be resized and modified
- when you know the exact size of data go for arrays
  - when you think the size of data can be increase later go for lists
- Array - is the core concept of numpy
  - List - is the core concept of python
- arrray - support elemt wise operation ( when yu want to perform operation on each elemnt)
  - List- it dont support elemnt wise operations it perform operations on an entire list at once
- Numpy arrays take less memory cz they store same datatype
  - Lists take more memory cz they store different datatypes

### searching in numpy arrays is easy as compared to lists why eventhough both have indexing??

- Python Lists use pointers: The list itself doesn't actually hold your data. It just holds a list of memory addresses (pointers) that point to where the real data is hiding somewhere else in your computer's memory.
  like one house being at address 1024 and the next at 8592
- NumPy Arrays don't use pointers for elements: The array holds the actual raw data values right inside it, packed tightly together in one solid block.
  In a NumPy array, the memory addresses are in a strict, back-to-back sequence (like houses 100, 104, 108)
  Because Python lists have to jump from the pointer to the actual data every time you look something up, it takes extra work for your CPU. NumPy avoids that completely

### so the pointers in list are in sequnec but the addresses are not

### A pointer is simply a variable that stores the specific memory address of where another piece of data is located, rather than storing the actual data itself.

# Rule simple hai:

Next address = current address + size of element
Na = 100+1=102

# EXTRA POINTS (methods of numpy)

- list main different types ka data store kia jaa skta h arrays main aik he type ka data hona chaiy so jab hum list ko numpy array main convert krty hain to jis type ka data list main daala hain wo sara array usi type main convert ho jay ga like
- int ke list h us main string or float b daal den to array k saary elmnts string main convert ho jain gy kion k integer aor float string ho skty hain lkn jo string wala data ho ga wo int ya float nai ho skta
- kion k array hmesha homogenious he rhy ga
- hum data type explicitly b set kr skty hain
- we can create an arary using **arange( )** too,instead of craeting list frst
- we can also create the shape of matrix using **.reshape(rows,col)**
- jitni values **arange( )** ko de hain us hisaab sy reshape ko rows columns k numbers deny hain
- we can alos use **.zeros( )** and **.ones( )** to generate 0 matrix or identity matrix
- bydefault dodno 0s aor 1s float main dety hain so use dtype for a specific data type
- we can also reshape both .zeros( ) and ones( )

# 2d array

- 2d arrays main rows or columns hoty hain to list ko 2d ararys main convert krny k liy nested lists use hn ge like list k andr lists

### 1D Array: Elements ki ek single line ya list hoti hai.(single row hoti h columns multiple ho skty hain)

### 2D Array: Elements multiple rows aur multiple columns ki form mein arrange hote hain. for example 2 rows 3 columns

### 3D array mein multiple 2D arrays stacked hoti hain.

# difference between range() and arange()

- range() is python's built-in function
- arange() is numpy's function
- arange accept float values too (as parametrs) range accept only integer values

# Attributes of Numpy array

properties that describe how the arrays will be stored and strctured (their datatype , their size,shape etc)

- **ndim** : jo arary hum ny bnaia us ke dimension kia h 1d h ya 2d ya 3d h
- **shape** :agr lets suppose 2 rows 3 col hain to 2 by 3 array ho gia this is shape - matlab number of rows aor number of columns btata h
  - 3d array main (number of layers,row,coulmns) btata h
- **size** : number of elemnts in an array jesy 2 by 3 main 6 elemnts hn gy
- **dtype** : array k andr elmnts ke datatype
- **itemsize** : array k har elemnt ka memory size bytes main btata h

# Indexing in Numpy Arrays

arr[-1] means indexing will start from end of an array like :
[1,3,5,6]
-4,-3,-2,-1

## array indexing in 2d arrays

- aik array k andr age 3 row (1d arrays) hain 3no ko in the form of matrix likh kar positioning kar k like row,col us say acess kr lo
- arr[1,:] number of row 1 h column main : dia hoa h to yani frst row puri utha lo yaani 3no columns
- arr[:,2] pura second column utha low number of row nai dia hoa
- number of rows aor number of columns k mid main comma use hota h aik he sq bracket use hoti h

# Slicing in Numpy Arrays

- slicing main : hota h
- slicing means accessing collection of elemnts from an array at the same time
- slicing main hum range dety hain yaani yaahan say ly kar wahan tak k elemnts acess krna
- **[start: stop :step]**
- step matlab aik aik kar k aagy chlna h yaa 2,2 kar k
- start waly index say start kren gy and stop waly index ko exclude kren gy kion k indexing 0 sy hoti h

## slicing in 1d array

- arr[1:3] stop main elmnt to thrd he h lkn indexing 0 say start ko rahi h to 3 indexes len gy 3rd index say pichly pr ruk jain gy

## slicng in 2d arrays

just practice
syntax :print(twod_arr[row_start:row_end,col_start:col_end])

# Arithmetic Operations on Numpy Array

- Addition(+)
- subtraction(-)
- multiplication(\*)
- matrix multiplication(@) 1st row _ 1st col ,1strow _ 2nd column ,2nd row _ 1st col ,2nd row _ 2nd col (then apply addaition on res of each)
- division (/) - will return ansers in float
- Floor Divison(//) will return only interger part(before point)
- exponentation(\*\*) X raise to power y X^y work same as +,- etc
- Modulo(%) find remainders wrks same as \*,-,+
- transpose chainging rows into columns and vice versa arr_name.transpose()

# Sorting 1D Numpy Array

- np.sort() - it will return sorted copy of an array (ascending order)
- for decending order use [::-1] with np.sort()
- np.argsort()- will return indexes of sorted array elmnts  
  orignal arry jo tha us main sorted elmnts kis kis index par pry hoy thy
- arr_name.sort()- user array name so apply sorting directly on orignal array(in palce sorting)

# Sorting 2D Numpy Array

- 2D arr main sorting by default row wise hoti h yani axis=1 hota h agr humy sorting column wise krni h to axis=0

# most commonly used Statistical operations on 1D Array

### syntax: np.opr(arr_name)

1. max() - maximum number in an array
2. min() - minimum number in an arry
3. sum()- sum of entore array
4. mean() -sum of all elemnts/total number of elmnts
5. median()- sort the array then find the mid vaue in case of even number of elmnts add both middle numbers and divide them on 2
6. prod() (product)- product of entire array
7. var() (varience) -mean kominus kren gy har aik elmnt of array say us ka square lena h sab ko add krna h divide krna h total number of elmnts par
8. std()(standard deviation) jo varience ka anser aya us ka sq root kr do wo std deviation ho ga
