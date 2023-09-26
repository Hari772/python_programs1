# list  : list are used to stored multiple items in a single variable
# list are created using square brackets
# a=[1,2,3,4,5]
# print(a)

# list items or elements are ordered ,changeable and allow duplicate elements
# a=[1,2,3,4,5,2,4,6,8,5]
# print(a)
#how to find the list length
#len()
# a=[2,4,6,8,10,12,14,16,18]
# print(len(a))
#list-data items
'''x=[1,2,3,4]
y=[1.1,2.3,3.3,4.4,5.5]
z=["a","b","c","d"]
print(x)
print(y)
print(z)'''

#list  can contain different data types
'''a=[1,2,5.5,6.6,78.76565,"a","python","hari"]
print(a)'''


#how to check type--->type()
# a=[1,2,3,"a","python","3.14"]
# print(type(a))
#list constructor---->list()
# a="python"
# x=list(a)
# print(x)
# print(type(x))


# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# a=[2,4,6,8,10,12,14,16,18,20]
# print(a[-1])#20
# print(a[-2])#18
# a=[2,4,6,8,10,12,14,16,18,20]
# #[start:stop-1:end]
# print(a[:])
# print(a[0:5])
# a=[2,4,6,8,10,12,14,16,18,20]
# # changing item values
# a[0]=3
# a[-1]=19
# print(a)
# a=[1,2,3,4]
# #insert()
# a.insert(2,"Python")
# print(a)
# a=[1,2,3,4]
# #5
# # append()
# a.append("python")
# print(a)
# removing list items
#remove()
# a=[2,4,5,6,8,10]
# #5
# a.remove(5)
# print(a)
#pop() method in python
# pop()--> removes the specified index
# a=[2,4,5,6,8,10]
# a.pop(2)  
# print(a)
''' del keyword also removes the specified index'''
# a=[2,4,5,6,8,10]
# del a[2]
# print(a)
# # del keyword can also delete the list completely
# x=[1,2,3,4,5,6,7,8,9,10]
# del x
# print(x)

''' clear() 
--> this method empty the list

'''
# x=[1,2,3,4,5]
# x.clear()
# print(x)

''' loop through a list'''
# a=[2,4,6,8,10]
# # for i in a:
# #     print(i)

# for i in range(len(a)):
#     print(a[i])


''' list comprehension '''
""" 
syntax:
        new_variable=[expression for item in iterable if condition==True]
"""
# # x=[i for i in range(10)]
# # print(x)
# a=[i for i in range(11) if i%2==0]
# print(a)
x=[1,4,5,6,78,23,5,6,7,8]
#sort()
# x.sort()
# print(x)
# a=["python","hari","rama","sita"]
# a.sort()
# print(a)
#reverse()
# a=["python","hari","rama","sita"]
# a.reverse()
'''# print(a)
x=[1,2,3,4,5,6,7,8,9,10]
x.reverse()
print(x)'''
''' python copy list'''
# a=[2,4,6,8]
# b=a.copy()
# print(b)

''' join two lists'''
# a=[2,4,6,8,10]
# b=[1,3,5,7,9]
# c=a+b
# c.sort()
# print(c)
# a=[2,4,6,8,10]
# b=[1,3,5,7,9]
# for i  in b:
#     a.append(i)
# a.sort()
# print(a)

'''
append()
clear()
copy()
count()
index()
insert()
pop()
remove()
reverse()
sort()
extend()

'''
#count()
# a=[2,4,6,8,10,2,2,4,5,6,7]
# print(a.count(11111111))
# """ index()  """
# a=[1,2,3,4,5,6]
# print(a.index(6))
''' extend()  '''
x=[2,4,6,8,10]
y=[1,3,5,7,9]
x.extend(y)
x.sort()
print(x)