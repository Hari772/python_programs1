N=int(input())
s=str(N)
l=list(s)
for i in l:
    if l.index(i)=='0':
        l.pop(i)
l.sort()
l.reverse()
m=''
for i in l:
    m=m+i
print(int(m))