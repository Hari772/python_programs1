'''x=input("Enter any number or string:")#121 121
y=x[::-1]
print("before reversing=",x)
print(" after reversing=",y)'''
x=int(input("Enter any number:"))
n=x
rev=0
while x!=0:
    digit=x%10
    rev=rev*10+digit
    x=x//10
print("before reversing a number",n)
print("After reversed number:",rev)
