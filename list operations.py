Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=[1,2,34,5,6]
s
[1, 2, 34, 5, 6]
type(s)# defines the  type of the data types are used in this
<class 'list'>
1 in s
True
25 not in s
True
25 in s
False
h=[1,4,5,6,7]
h
[1, 4, 5, 6, 7]
s+h
[1, 2, 34, 5, 6, 1, 4, 5, 6, 7]
h*2
[1, 4, 5, 6, 7, 1, 4, 5, 6, 7]
s=h
s
[1, 4, 5, 6, 7]
name='HARIPRASAD DUVVURU'
list(name)
['H', 'A', 'R', 'I', 'P', 'R', 'A', 'S', 'A', 'D', ' ', 'D', 'U', 'V', 'V', 'U', 'R', 'U']
name
'HARIPRASAD DUVVURU'
x=name
x
'HARIPRASAD DUVVURU'
y=list(x)
y
['H', 'A', 'R', 'I', 'P', 'R', 'A', 'S', 'A', 'D', ' ', 'D', 'U', 'V', 'V', 'U', 'R', 'U']
y[6]='h'
y
['H', 'A', 'R', 'I', 'P', 'R', 'h', 'S', 'A', 'D', ' ', 'D', 'U', 'V', 'V', 'U', 'R', 'U']
v="HARIPRASAD"
x=list(v)
x
['H', 'A', 'R', 'I', 'P', 'R', 'A', 'S', 'A', 'D']
x[::]
['H', 'A', 'R', 'I', 'P', 'R', 'A', 'S', 'A', 'D']
x[::-1]
['D', 'A', 'S', 'A', 'R', 'P', 'I', 'R', 'A', 'H']
x[::2]
['H', 'R', 'P', 'A', 'A']
x[2::100]
['R']
x[:100:2]
['H', 'R', 'P', 'A', 'A']
y=[1,3,5,7,11,13,15,17,19]
len(y)# len() is a function used to find the length of the list
9
sotred(y)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    sotred(y)
NameError: name 'sotred' is not defined. Did you mean: 'sorted'?
sorted(y)# sorted() is function used to keep the data in sorted data
[1, 3, 5, 7, 11, 13, 15, 17, 19]
min(y)
1
max(y)
19
sum(y)
91
any(y)
True
all(y)
True
dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

===================================== RESTART: Shell =====================================
x=[20,19,18,17,16,15]
x
[20, 19, 18, 17, 16, 15]

x.sort()# sort is function
x
[15, 16, 17, 18, 19, 20]
xx.reverse()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    xx.reverse()
NameError: name 'xx' is not defined. Did you mean: 'x'?
x.reverse()# reverse() is a function which reversae the  list
x
[20, 19, 18, 17, 16, 15]
x.count(20)# count() is a function which counts no of elements are present
1
x
[20, 19, 18, 17, 16, 15]
x.append(14)# append() is afunction which add a data in list
x
[20, 19, 18, 17, 16, 15, 14]
x.index(15)# index() is a function which gives the position of the index
5
x.insert(3,13)# insert(index,item)=>synatax
x
[20, 19, 18, 13, 17, 16, 15, 14]
x.sort()
x
[13, 14, 15, 16, 17, 18, 19, 20]
x.remove(13)# remove() is function which remove a element from the list
x
[14, 15, 16, 17, 18, 19, 20]
x.pop()#pop() is a function which remove element from the list
20
x
[14, 15, 16, 17, 18, 19]
x.pop(18)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x.pop(18)
IndexError: pop index out of range
x.index(18)# index(parameter)=>which find the index of the element
4
x.pop(4)
18
x
[14, 15, 16, 17, 19]
x.reverse()
x
[19, 17, 16, 15, 14]
x
[19, 17, 16, 15, 14]
x
[19, 17, 16, 15, 14]
del x[1]# syntax is {del list_name[index]} or del list_name[start:step]
x
[19, 16, 15, 14]
del x[:2]
x
[15, 14]
del x[::]

x
[]
# now i am using nested list
h=[[1,1,1],[2,2,2],[3,3,3]]
len(h)
3
h[0]
[1, 1, 1]
h[1]
[2, 2, 2]
h[2]
[3, 3, 3]
h[0][2]
1
del h[0][0]
h
[[1, 1], [2, 2, 2], [3, 3, 3]]
