str1=input()
n=int(input())
l=list(str1)
print(l)
m=""
l.pop(n)
print(l)
for i in l:
    m=m+i
print(m)
