'''n=input("Enter the number/any string:")
x=n[::-1]
print("n=",n)
print("x=",x)
if x==n:
    print("palindrome")
else:
    print("Not  a palindrome")'''
n=int(input("Enter the number:"))
temp=n
print("given number :",n)
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reverse number:",rev)
if temp==rev:print("Palindrome number")
else:print("Not a palindrome number")
