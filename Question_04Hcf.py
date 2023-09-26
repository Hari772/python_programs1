a,b=map(int,input("Enter the numbers..\n").split(" "))
# print(a)
# print(b)
# a,b=input().split()
# print(a)
# print(b)
for num in range(1,(a*b)+1):
    if num%a==0 and num%b==0:
        break
lcm=num
hcf=int((a*b)/lcm)
print(f"Lcm of two numbers is {lcm}")
print(f"HCf of two numbers is {hcf}")