'''Rules for Python variables:
* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric 
   characters and underscores (A-z, 0-9, and _ )

* A variable names are case-sensitive 
   (age, Age and AGE are three different variables)
* A variable name cannot be any of the Python keywords.'''

'''myvar="xyz"
My_rrr="xyz"
_my="xyz"
myvar_123="xyz"
my_var_2="xyz"
print(myvar)
print(My_rrr)
print(_my)
print(myvar_123)
print(my_var_2)'''

'''2my_name="hari"
print(2_my_name)'''

'''#camel case
myName="Hari"
print(myName)

#pascal case
MyName="Hari"
print(MyName)

#snake case
my_name_is_what="Hari"
print(my_name_is_what)'''

# how to assign multiple values
'''x=5
y=6
z=7
print(x)
print(y)
print(z)'''
'''x,y,z=5,6,7
print(x)
print(y)
print(z)'''

'''#one value to multiple variables
x=y=z=6
print(x)
print(y)
print(z)'''
#output variables
#x="python is easy"
#print(x)

'''x="python"
y="is"
z="easy"
print(x+" "+y+" "+z)'''
#print(x,y,z)
'''x=5
y=6
print(x+y)'''

'''x=5
y="hari"
#print(x+y)
print(x,y)'''


#global variable
x="hari"
def name():
       #global x
       x="python"
       print(x)
name()
print("x=",x)

