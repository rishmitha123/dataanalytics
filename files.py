file=open('text.txt','r')
# content=file.read()
# print(content)
content1=file.readline()
content2=file.readlines()
file.close()

file=open('test.txt','w')
file.write("hello\n")
file.write("welcome")
file.close()

file=open('text.txt','a')
file.write("new content")
file.close()

import os
if os.path.exists("text.txt"):
    with open('text.txt','r')as file:
        content=file.read()
        print(content)
else:
    print("file doesnot exists")
    
    
import os
try:
    with open('text.txt','r')as file:
        content=file.read()
    with open("test.txt",'w') as filewrite:
        filewrite.write(content)
    print("file copied successfully")
except IOError as e:
    print("io exception")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print("unexpected error")
        
        
f=open("example.txt",'x')#create new file
f.write("revature")

f.close()