print("Python RegEx")

import re
x="heloo i am iqra jamil"
#re.findall(pattren,string)
result=re.findall("[a-l]",x)
print(result)


y="hello 123"
# result=re.search(r"\s", y)
result=re.search("123", y)
print("pattren found at index",result.start())
if result:
    print("match found")
else:
    print("match not found")


text = "apple, banana; cherry | date";
print(text)
result=re.split("[,;]",text)  # we can add | into the set to split cherry | date too
print(result)
sub_result=re.sub("apple","mango",text)
print("sub result :",sub_result)