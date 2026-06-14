# Python RegEx

RegEx is a sequence of characters (or just a way) use to form a search pattren
or we can say that its a set of rules that is used to write a set of rules to search a specific string in a doucment

## RegEx Module

- python has a built in module "re" to work with regular expressions
- start by importing re

## RegEx Functions

- re.findall: returns a list containing all the matches
- re.search : returns the Match object which contain that specific serached word
- split: it cuts your entir sting into pieces,wherever the pattren is found ,gives you the pieces as a list
  - For example you have the sentence "one1two2three" and you say split wherever there is a number("/d") it cuts at 1 and 2 and gives you ["one", "two", "three"].
- re.sub : replaces one or many matches with a string
  - for eaxmple aap space search kar k us ko kisi specific string k sath replace kr skty ho puri string ko ya kisi speacific poistion ko

## Metacharacters

- metacharcters are the characters with the special meanings
- we use them bcz we cant always search for an exact word
- sometimes we want to search an email,number or any space without knowing the exact value
- Meta characters like \d or \w are shortcuts that mean "anything that looks like this" so we don't have to write every possibility manually.
- can consult https://www.w3schools.com/python/python_regex.asp for details

## Flags:

- we can also add flags to the pattren
- Flags change how the search behaves.

- For example : normally RegEx is case sensitive so `"cat"` won't find `"CAT"`. we add the flag `re.IGNORECASE` and now it finds both. Flags just give us extra control over the search.
- like re.ASCII: Returns only ASCII matches
- re.DEBUG:returns debug information
- can consult https://www.w3schools.com/python/python_regex.asp for details

## Special Sequences

- A special sequence is a \ followed by a character, and has special meaning
- For example instead of writing `[0-9]` to find a number, we just write `\d` — same result, less typing.
- That's all special sequences are, short codes for patterns we use often.
- can consult https://www.w3schools.com/python/python_regex.asp for details
  Sets
- set is a set of characters inside a pair of square brackets [] with a special meanings
- [a-n] Returns a match for any lower case character, alphabetically between a and n
- - can consult https://www.w3schools.com/python/python_regex.asp for details

## The findall() Function

- this function returns a list containing all the matches
- syntax : findall(pattren,string)
- findall(rule according to which we want to search , string,document in which we want to srch)

## The search() Function

- we use re.search() when we want to know if the specific pattren exist in the specific string or not
- syntax : search(pattren,string)
- search(rule according to which we want to search , string,document in which we want to srch)
- we use .start to find the position where specific pattren found
- If no matches are found, the value None is returned

## The split() Function

- we use split() when we want to braek a string on the basis of a specific pattren
- For example if we have messy data like "name,age;city" and want to separate each word we split on , or ; and get a clean list ["name", "age", "city"].
- we can control the number of occurrences by specifying the maxsplit parameter
- syntax : search(pattren,string,maxsplit(1 or 2...))

## The sub() Function

- we use this function when we want to replace something in a string with somethingelse
- we can control the number of replacements by specifying the count parameter
- syntax: re.sub(pattern, replacement, string,count)

- For example replace all numbers with # so "call 123" becomes "call ###".

## Match Object

- MAtch object is something(object) pythin returns when search() finds something
- It contains 3 useful things:
  - .span() : gives us the start and end position of the match
  - .string : gives us back the original string we searched in
  - .group() — gives us the actual word that was matched

### Note: Important rule if nothing is found, Python returns None instead of a match object, so always check first
