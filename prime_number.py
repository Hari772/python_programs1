n=int(input("Enter the number:"))
'''for i in range(2,n):
    if n%i==0:
        print(f"{n} is not a prime number")
        break
    else:
        print(f"{n} is a prime number")
        break'''
for i in range(2,n):
    if n%i!=0:
        print(f"{n} is prime number")
        break
    else:
        print(f"{n} is not prime number")
        break
