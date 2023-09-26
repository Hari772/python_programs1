# n=int(input("Enter the value of n:"))
# if (n%2!=0):
#     print("Weird")
# else:
#     if(n>=2 and n<=5) and n%2==0:
#         print("Not Weird")
#     if (n>=6 and n<=20) and n%2==0:
#         print("Weird")
#     if (n%2==0) and n>20:
#          print("Not Weird")
'''str1=list(map(str,input().strip().split(',')))
l=[]
for i in str1:
    for j in i:
        if j in'abcdefghijklmnopqrstuvwxyz'and j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and j in '0123456789' and j in '@#$':
            l.append(i)
print(l)'''
''''l1=list(map(str,input().strip().split(',')))
l2=list(map(str,input().strip().split(',')))
l=[]
n=''
m=''
l1.reverse()
l2.reverse()
#print(l1)
#print(l2)
for i in l1:
    n=n+i
for j in l2:
    m=m+j
s=int(n)+int(m)
p=list(str(s))
p.reverse()
#print(p)
for i in p:
    l.append(int(i))
print(l)'''
'''x=int(input())
n=x
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if x==rev:
    print("true")
else:
    print("false")'''
'''if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=max(arr)
    c=arr.count(a)
    for i in range(c):
        arr.remove(a)'''
n=int(input())
l=[]
for i in range(n):
    x=list(map(int,input().split(" ")))
    if x[0]>x[1]:
        l.append(x[0])
    elif x[0]<x[1]:
        l.append(x[1])
    elif x[0]==x[1]:
        l.append(x[0])
for i in l:
    print(i)
            


