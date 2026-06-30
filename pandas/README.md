# Pandas Introduction

## What is Pandas?

- pandas aik python library h jo k datasets k sath kaam krny k liy use hoti hai
- is libraray k functions datsets ko explore,manipulate, aor clean ya analyze krny k liy usee hoty hain
- Pandas comes from two terms panel data and python data analysis

## Why Use Pandas?

- we use pandas to analyze big datasets
- we can use pandas to draw conclusions on the basis of statistical theories
- we can also use pandas to clean the messy datasets, to make the datasets relevent and readable

## What Can Pandas Do?

- pandas gives the ansers about the data like:
  - Is there a correlation between two or more columns?
  - What is average value?
  - Max value?
  - Min value?
- pandas can delete the irrelevent rows from our data, delete wrong values, or delete empty or NULL value
  this is called cleaning the data.

# Pandas Getting Started

## Checking Pandas Version

- we can instal and import it liek other libraries
- we can chek the version of pandas by using pandas.**version**(under_scores on both sides (dunder method))

# Pandas Series

## What is a Series?

- Pandas series is like a column in a table
- it is one - d array holding data of any type
- it print useful info automatically about the data stored in an array when we print arary like dtype,indexes

## Labels

- labels are the names or identifiers we use ti acess values from an array
- like here we have 0,1,2.... are the lebels (also called index)

## Create Labels

- Instead of default numeric labels, we can also have custom labels like "a", "b", and "c".
- with the index argument we can name our own labels

## Key/Value Objects as Series

- we can also use a key/value object like dict when creating a series
- we dont have indexing in key value objects so we use keys to acess specific value as labels
- Use the index argument to choose which dictionary items we want in the Series.(multiple items not all or not single for single we can use key name with dict name as we usually do)

### NOte: for 1 dimensional data use Series and for multidimensional data use Dataframes

### series is liek a single column and Dataframe is like an entore table

## DataFrames

- Data sets in pandas are uslly multi-dimensional tables ,called Dataframes
- it is 2d data structure or a 2d table with rows and columns
- Pandas use the loc attribute to return one or more specified row(s) using its label(index number)

### Note we can chk properties & methods of dataFrame() object on https://www.w3schools.com/python/pandas/pandas_ref_dataframe.asp

### Note: This example returns a Pandas Series.

- use a list of indexes to acess multiple items use dble [[]]

## Named Indexes

- we can have named indexes just like series

## Locate Named Indexes

and we can locate them too using loc attribute

# Pandas Read CSV

- A simple way to store big data sets is to use CSV files (comma separated files).
- CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
- use to_string() to print the entire DataFrame. else it will shortend rows (data) using (...)
- we can use read_csv() to read/load csv file into dataframe

## max_rows

- we can check our system's maximum rows with the pd.options.display.max_rows statement
- it will print only maximum rows without shortning if we ar not using to_string() after max_rows number it will use ... and will shortend the data
- few from top and few from bottom

# Pandas Read JSON

## Read JSON

- we can use read_json() to load json file into dataframe
- Big data sets are often stored, or extracted as JSON.

- JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

## Dictionary as JSON

- JSON = Python Dictionary

- JSON objects have the same format as Python dictionaries.
- If our JSON code is not in a file, but in a Python Dictionary, we can load it into a DataFrame directly using pandas.DataFrame(dict_name)

# Pandas - Analyzing DataFrames

- we can use head() and tail() methods to view rows
- we can specify numbers of row we want to view like head(10)
- it will return top 5 rows with headers if we dont specify number of rows
- tail() will return 5 rows from bottom

## Info About the Data

-info() gives a quick summary of a DataFrame.

- It shows the number of rows and columns, column names, data types, and whether columns contain missing values.

## Null Values

- Non-Null are fine but we need to delete null values and that were data cleaning starts

# Data Correlations

The corr() method calculates the relationship between each column in our data set.

# Pandas - Plotting

- Pandas uses the plot() method to create diagrams.
- We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
- we can specify different kinds

# Filtering:

- It means selecting only the rows that match a condition.
- For filtering, we mainly use:
  - Boolean conditions
  - []
  - .loc[]
  - Comparison operators: ==, !=, >, <, >=, <=
  - Logical operators: & (and), | (or), ~ (not)
  - .isin()
  - .between()
  - .str.contains() (for text)
  - Pandas .filter() = It filters labels (rows or columns by name), not rows based on conditions like python's built-in filter()

# Groupby:

- It means grouping rows based on a common value, then performing operations like sum, average, count, minimum, or maximum on each group using **.groupby()**
- After groupby() we usually apply an aggregation method such as sum(),mean(),median etc
