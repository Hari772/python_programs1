Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='single quotes'
type(s)
<class 'str'>
h="double quotes"
type(h)
<class 'str'>
l='''triple quotes'''
type(l)
<class 'str'>
x=1234567890
type(x)
<class 'int'>
y=str(x)
y
'1234567890'
x
1234567890
type(x,y)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    type(x,y)
TypeError: type() takes 1 or 3 arguments
type(y)
<class 'str'>
type(x)
<class 'int'>
n1='HARI'
n2='PRASAD'
n1+n2
'HARIPRASAD'
n1<=n2
True
n1==n2
False
n2>=n1
True
n=n1+n2
n
'HARIPRASAD'
len(n)
10
min(n)
'A'
max(n)
'S'
#strings are immutable
n
'HARIPRASAD'
n[0]
'H'
n[2]
'R'
n[1]
'A'
n[3]
'I'
n[4]
'P'
n[5]
'R'
n[6]
'A'
n[7]
'S'
n[8]
'A'
n[9]
'D'
n[10]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    n[10]
IndexError: string index out of range
n
'HARIPRASAD'
n[::]
'HARIPRASAD'
n[::2]
'HRPAA'
n[::3]
'HIAD'
n[1:8]
'ARIPRAS'

n[::-1]
'DASARPIRAH'
n[::-2]
'DSRIA'
m='hariprasad duvvuru'
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



m.upper()
'HARIPRASAD DUVVURU'
m
'hariprasad duvvuru'
x=m.upper()
x
'HARIPRASAD DUVVURU'
x.lower()
'hariprasad duvvuru'
m.title()
'Hariprasad Duvvuru'
m.islower()
True
m.isupper()
False
x.isidentifier()
False
m.isidentifier()
False
m.isdigit()
False
m.isdecimal()
False
m.isalpha()
False
m.capatalise()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    m.capatalise()
AttributeError: 'str' object has no attribute 'capatalise'. Did you mean: 'capitalize'?
m.capitalize()
'Hariprasad duvvuru'
m.title()
'Hariprasad Duvvuru'
m
'hariprasad duvvuru'
h="HARIPRASAD DUVVURU,SASIKUMAR DUVVURU"
h.split(",")
['HARIPRASAD DUVVURU', 'SASIKUMAR DUVVURU']
h="HARIPRASAD DUVVURU SASIKUMAR DUVVURU"
h.split()
['HARIPRASAD', 'DUVVURU', 'SASIKUMAR', 'DUVVURU']
h.split(5)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    h.split(5)
TypeError: must be str or None, not int
f="I AM HARIPRASAD DUVVURU"
f.split("AM")
['I ', ' HARIPRASAD DUVVURU']
f.split("10)
        
SyntaxError: unterminated string literal (detected at line 1)
s.split("10")
        
['single quotes']
numbers=123
        
character="army"
        
numbers="123"
        
password=numbers.join(character)
        
password
        
'a123r123m123y'
