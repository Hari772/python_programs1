s=""
n=input()
l=list(n)
while True:
    s=s+min(l)
    l.remove(min(l))
    if l==[]:
        break
print(s.strip())