#lcm of two numbers
'''
2
3
lcm of 2 and 3 is 6 
'''
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
for i in range(1,(a*b)+1):
    if i%a==0 and i%b==0:
        print(f"LCM of {a} and {b} is {i}")






        
        
