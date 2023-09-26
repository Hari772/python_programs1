'''
Python Logical Operators:
Logical operators are used to combine conditional statements 
  1.and 
  2.or
  3.not


and 	Returns True if both statements are true	a < 5 and  a < 10	
or	Returns True if one of the statements is true	a < 5 or a < 4	
not	Reverse the result, returns False if the result is true	 not(a < 5 and a < 10)

'''
# a=7
# print(a<5 and a<10)
# a=7
# print(a<5 or a<10)
# print(a<2 or a<5)
a=5
print(not(a<10))
print(not(a>7 and a<10))