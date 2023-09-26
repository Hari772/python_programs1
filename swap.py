#swapping  of two numbers program in python
'''print("Before swapping of two numbers:")
a,b=eval(input("Enter a=")),eval(input("Enter b="))
a,b=b,a
print("After swapping of two numbers:")
print("a=",a)
print("b=",b)'''
print("Before swapping of two numbers:")
a,b=eval(input("Enter a=")),eval(input("Enter b="))#a=5 b=6
a=a+b #5+6=11 now a=11
b=a-b #b=11-6 b=5
a=a-b #a=11-5 a=6
print("After swapping of two numbers:")
print("a=",a)
print("b=",b)



