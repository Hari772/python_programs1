str1=input()
old=input()
new=input()
l=list(str1)
print(l)
m=""
x=l.index(old)
l.remove(old)
l.insert(x,new)
print(l)
for i in l:
    m=m+i
print(m)
