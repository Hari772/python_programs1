n=int(input("Enter the number:...."))
x=n
rev=0
while x>0:
    r=x%10
    rev=rev*10+r
    x=x//10
print(f"Reverse of a given number is...{rev}")
if rev==n:
    print(f"{n} is  Palindrone->{n}")
else:
    print(f"{n} is not Palindrone")

