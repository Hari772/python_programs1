Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
h=1,2,3,4,5,6,7,8,9
h
(1, 2, 3, 4, 5, 6, 7, 8, 9)
type(h)
<class 'tuple'>
h=12,3,4,8
h
(12, 3, 4, 8)
print(h)
(12, 3, 4, 8)
h=2,4,6,8
s=1,3,5,7
h
(2, 4, 6, 8)
s
(1, 3, 5, 7)
h+s
(2, 4, 6, 8, 1, 3, 5, 7)
h-s
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    h-s
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
 h=s
 
SyntaxError: unexpected indent
h=s

len(h)=len(s)
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?

len(h)==len(s)
True
h
(1, 3, 5, 7)
s
(1, 3, 5, 7)
s
(1, 3, 5, 7)
1 in s
True
25 in s
False
25 not in s# here in  and not in  are membership operators
True
h=2,4,6,8
s=1,3,5,7
h==s
False
h
(2, 4, 6, 8)
s
(1, 3, 5, 7)
w="HARIPRASAD"
tuple(w)#tuple function 
('H', 'A', 'R', 'I', 'P', 'R', 'A', 'S', 'A', 'D')
w="HARIPRASAD DUVVURU"
w
'HARIPRASAD DUVVURU'
list(w)# here using list function
['H', 'A', 'R', 'I', 'P', 'R', 'A', 'S', 'A', 'D', ' ', 'D', 'U', 'V', 'V', 'U', 'R', 'U']
tuple(w)
('H', 'A', 'R', 'I', 'P', 'R', 'A', 'S', 'A', 'D', ' ', 'D', 'U', 'V', 'V', 'U', 'R', 'U')
dict(w)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(w)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
h=10,20,30,40,50,60,70
h
(10, 20, 30, 40, 50, 60, 70)
h[5]
60
h[1]
20
20
20
h[2]
30
h[30]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    h[30]
IndexError: tuple index out of range
h[3]
40
h
(10, 20, 30, 40, 50, 60, 70)
h[::]
(10, 20, 30, 40, 50, 60, 70)
h[::-1]
(70, 60, 50, 40, 30, 20, 10)
h
(10, 20, 30, 40, 50, 60, 70)
s=h[::-1]
s
(70, 60, 50, 40, 30, 20, 10)
s==h
False
s
(70, 60, 50, 40, 30, 20, 10)
h
(10, 20, 30, 40, 50, 60, 70)
h[:6]
(10, 20, 30, 40, 50, 60)
h[:5]
(10, 20, 30, 40, 50)
h[::2]
(10, 30, 50, 70)
h
(10, 20, 30, 40, 50, 60, 70)
h[-1]
70
h[2]
30
h[-3]
50
h[-2]
60
h[-1:-8]
()
h[-1:]
(70,)
h[-1:-5]
()
h
(10, 20, 30, 40, 50, 60, 70)
h[-1:-3]
()
h
(10, 20, 30, 40, 50, 60, 70)
len(h)
7
sum(h)
280
s
(70, 60, 50, 40, 30, 20, 10)
h=sorted(s)
h
[10, 20, 30, 40, 50, 60, 70]
sum(h)+sum(s)
560
h
[10, 20, 30, 40, 50, 60, 70]
h.count(10)
1
\
h.count(10,20)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    h.count(10,20)
TypeError: list.count() takes exactly one argument (2 given)
h.count(20)
1
s=10,10,20,30,40,10,10,50,10,10,60,10
s.count(10)
7
s.count(20)
1
s.index(10)
0
h
[10, 20, 30, 40, 50, 60, 70]
h.count(20)
1
h.index(10)
0
h.poop()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    h.poop()
AttributeError: 'list' object has no attribute 'poop'. Did you mean: 'pop'?
h.pop()
70
h.pop([5])
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    h.pop([5])
TypeError: 'list' object cannot be interpreted as an integer
for i in h
SyntaxError: expected ':'
for i in h:
    print(i)

    
10
20
30
40
50
60
dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
x=1,2,3
y=23,4,5
z=zip(x,y)
list(z)
[(1, 23), (2, 4), (3, 5)]
