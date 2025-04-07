import json
x='{"name":"rishmi","age":22}'
z=json.loads(x)
print(z["name"])
print(z["age"])

import json
y={
    "name":"geetha",
    "age":24
    
}
z=json.dumps(y)
print(z)

import re
x="the rain is spain"
y=re.search("^the.*spain$",x)
if y:
    print("pattern matches")
else:
    print("pattern not matches")
    
import re
x="the rain is spain"
z=re.findall("ai",x)
y=re.search("\s",x)#search the white space here /s represents the white space
k=re.split("\s",x)#split the white space
r=re.sub("\s","$",x)

print(z)
print(y)
print(k)
print(r)

import re
pattern=r"\d+"#this pattern matches one or more digits
text="there are 123 apples"
match=re.search(pattern,text)
if match:
    print("match found",match.group())
    
import re
pattern=r"(\d+)-(\d+)-(\d+)"
text="the event is on 2024-03-23"
match=re.search(pattern,text)
if match:
    print("year :",match.group(1))
    print("month :",match.group(2))
    print("day :",match.group(3))
    
import re
email=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text="please contact at example@revature.com"
match=re.search(email,text)
if match:
    print("email found :",match.group())