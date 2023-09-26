Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
+
SyntaxError: invalid syntax
h={1,2,3,4,5,6,7,,8,9}# set is created by  using curly brases{item1,item2,item3}
SyntaxError: invalid syntax
h={1,2,3,4,5,6,7}
h# set will not print duplicated values,set is a mutable
{1, 2, 3, 4, 5, 6, 7}
type(h)
<class 'set'>
a={2,3,4,6,8,10}
b={1,3,5,7,9,11}
a.union(b)# syntax=> set1.union(set2)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
a.intersection(b)# syntax => set1.intersection(set2)
{3}
a.isubset(b)# checking for sub set or not,syntax => set1.issubset(set2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.isubset(b)
AttributeError: 'set' object has no attribute 'isubset'. Did you mean: 'issubset'?
a.issubset(b)
False
a.isdisjoint(b)#  checking whather it is a joint or dis joint syntax is
# set1.isdisjoint(set2)
False
a.difference(b)'''syntax=> set1.difference(set2)'''
{2, 4, 6, 8, 10}
b.pop()# here if ur useing pop function, here first item will be pooped out
1
b
{3, 5, 7, 9, 11}
a.pop()
2
a.remove(3)# syntax=> set_name.remove(parameter)
a
{4, 6, 8, 10}
a.symmetric_difference(b)
{3, 4, 5, 6, 7, 8, 9, 10, 11}
a
{4, 6, 8, 10}
b
{3, 5, 7, 9, 11}
a.update(b)# if u want to  merge two sets then syntax=> set1.update(set2)
a
{3, 4, 5, 6, 7, 8, 9, 10, 11}
a.clear()# syntax=>set1.clear(),it means  whole set will be cleared(empty)
a
set()
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
b.discard(5)#syntax=>set_name.discard(parameter),it will remove particular element
b
{3, 7, 9, 11}
b.discard(5)
b
{3, 7, 9, 11}
b.discard(5)
b
{3, 7, 9, 11}
h={1,2,3,4,5,6,7,,8,9}
SyntaxError: invalid syntax
a={2,3,4,6,8,10}
a
{2, 3, 4, 6, 8, 10}
len(a)
6
sorted(a)
[2, 3, 4, 6, 8, 10]
sorted(a)
[2, 3, 4, 6, 8, 10]
a
{2, 3, 4, 6, 8, 10}
KeyboardInterrupt
a
{2, 3, 4, 6, 8, 10}
