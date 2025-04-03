# list functions

l1=[2,5,"anu"]
l2=[4,5,6]
l3=[2.5,6.3]
l1.append("geetha")
l1.append(l2)
l1.extend(l3)
print(l1)
l1.pop()
l1.insert(1,2+4j)
l1.remove(2.5)
print(l1)




l4=[4,8,3,7,9,1,2,6,3]
count=l4.count(3)
print(count)
l5=l4.copy()
l4.sort()
l4.pop(2)#index
print(l4)
l4.sort(reverse=True)
print(l4)
print(l5)
l5.clear()
print(l5)