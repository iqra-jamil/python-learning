# Pandas - Cleaning Data

## Data Cleaning

- fixing the bad data we have in our data set
- bad data could be
  - duplicate data
  - wrong data
  - wrong format
  - empty cells

# Cleaning Empty Cells

- empty rows can give us wrong results
- we can deal with empty values in 2 ways
  - by removing entire row containing empty vaalues using dropna() methods
  - by filling empty cells with values using fillna() method

- By default, the dropna() method returns a new DataFrame, and will not change the original.
- if we want to apply dropna on orignal dataframe we need to use input=True argument
- fillna() method will replace all the null values bydefault
- so we can also specify the column name ,To only replace empty values for one column

## Replace Using Mean, Median, or Mode

- A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

- Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column
  - Mean = the average value (the sum of all values divided by number of values).
  - Median = the value in the middle, after we have sorted all values ascending.
  - Mode = the value that appears most frequently.

# Cleaning Data of Wrong Format

- Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

- To fix it, we have two options:
  - remove the rows using dropna()
  - convert all cells in the columns into the same format. for example pandas has a method to fix date format
    **to_datetime()**

# Fixing Wrong Data

- "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
- we still have two options
  - remove the rows using dropna()
  - or fix the wrong values by replacing them with something else

# Removing Duplicates

- to remove duplicate rows frst discover them using duplicated() method.
- The duplicated() method returns a Boolean values for each row
- Returns True for every row that is a duplicate, otherwise False
- To remove duplicates, use the drop_duplicates() method.
- The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

### Note: the pre-3.0 had no strict string dtype, pandas 3.0 enforces stricter type checks on the new string dtype that didn't exist before.

### dropna() only removes rows that have missing (NaN) values. so if we want to remove a row based on condition we will use drop() not dropna()
