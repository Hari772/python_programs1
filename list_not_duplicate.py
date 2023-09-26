n=int(input())
l=[]
for i in range(0,n):
    m=int(input())
    l.append(m)
print(l)
d=[]
for i in l:
    if l.count(i)==n1:
        if l[i] not in d:
            d.append(l[i])
print(d)
count=0
for i in d:
    count=count+1
print(count)
        
