# string functions
s1="We are training on data analytics course"
s2="revature"
s3="rishmi123"
print(s1.upper())
print(s1.lower())
print(s1.capitalize())
print(s1.title())
print(s1.istitle())
print(s1.center(100))
print(s1.isupper())
print(s2.islower())
print(s2.isalpha())
print(s3.isalnum())
print(s2.isdigit())
print(s1.index("data"))
print(s1.rindex("e")) #gives the last index of element if element not found it gives error
print(s2.find("e"))
print(s2.rfind("e"))# same as rindex if elememt not found it returns -1
print(s1.split())
print(s1.rsplit("-",2))
print(s1.swapcase())
print(s2.join(s3))
print(s2.replace('e','p'))
print(s2.startswith("reva"))
print(s2.endswith("ure"))
print(s2.count("e"))
print(s2.count("e",0,4))
print(s2.isprintable())
print(s2.isidentifier())
print(s1.splitlines())
print(s1.splitlines(True))#if any breaks are there they would be in the output