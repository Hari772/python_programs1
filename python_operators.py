Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.



x=3
x
3
X=3
X
3
Y=3
y
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    y
NameError: name 'y' is not defined. Did you mean: 'Y'?
8+2
10
x=2
print(x)
2
x=8+2
print(x)
10
hari_prasad=546
print(hari_prasaad)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(hari_prasaad)
NameError: name 'hari_prasaad' is not defined. Did you mean: 'hari_prasad'?
print(hariprasad)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(hariprasad)
NameError: name 'hariprasad' is not defined. Did you mean: 'hari_prasad'?
print(hari_prasad)
546
x='546'
print(x)
546
x='546'
y='547'
x+y
'546547'
print(x+y)
546547
x
'546'
y
'547'
a=b=c=1
a,b,c=c,b,a
print(a)
1
print(b)
1
print(c)
1
x=10
y=5
x+y
15
x+y #Addition
15
x-y #subtraction
5
x*y #muitiplication
50
x/y #division
2.0
int(x/y)
2

x%y # modulus operator
0
x**y
100000
# above ** operator performs expoentional
x//y # floor division
2
'''Assinnment operstors'''
'Assinnment operstors'
x=10
y=5
z=x+y
z
15
x+=5
x
15
x=10
x+=5 # it means x=x+5
x
15
x-=5
print(x)
10
x
10
x*=2
x
20

x*=2 # it means x=x*2
x
40
x-30
10
x
40
x-=30 # it means x=x-30
x
10
x=4
x/=2
x
2.0
x=4
x**=2
x
16
x**=2 # it means x=x**2
x
256
x=10
x
10
10=10
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
10==10
True
10==5
False
10!=5
True
10>5
True
10<5
False
10>=6
True
6<=6
True
True and True
True
True or True
True
Not True
SyntaxError: invalid syntax. Perhaps you forgot a comma?
Not ,True
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    Not ,True
NameError: name 'Not' is not defined
not True
False
bin(8)
'0b1000'
bin(10)
'0b1010'
int x=5
SyntaxError: invalid syntax. Perhaps you forgot a comma?
x=5
x
5
y=5.6
y
5.6
x=5+7j
x
(5+7j)
x=5+7j # this is complex representstion
x
(5+7j)
bool true
SyntaxError: invalid syntax. Perhaps you forgot a comma?
bool True
SyntaxError: invalid syntax. Perhaps you forgot a comma?
x=None
y=5
z=x+y
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    z=x+y
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
s="Hariprasad duvvuru"
s
'Hariprasad duvvuru'
print(s)
Hariprasad duvvuru
x='''HARIPRASAD DUVVURU'''
print(x)
HARIPRASAD DUVVURU
x=int(input("Enter the value"))
Enter the value76
y=int(input("Entetr the value "))
Entetr the value 45
x+y
121
print('''Hello world''')
Hello world
name='''HARI'''
print(f"your name is {name}")
your name is HARI
print("your name is ",name)
your name is  HARI
# type conversions are
perc=95.55
perc
95.55
int(perc)
95

x='hari'
int(x)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: 'hari'
x=int("1")
x
1
x=int("1")# casting is srting to int
x
1
x=98
float(x)
98.0
x=8
str(x)
'8'
x=9866909418
y=str(x)
y
'9866909418'
char(65)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    char(65)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(65)
'A'
chr(66)
'B'
chr('c')
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    chr('c')
TypeError: 'str' object cannot be interpreted as an integer
chr(35)
'#'
chr(70)
'F'
chr(72)
'H'
ord('A')
65
ord("/")
47
oct(255)
'0o377'
hex(10010)
'0x271a'
x=65
type(x)
<class 'int'>
y=76.6
type(y)
<class 'float'>
type(x=77)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    type(x=77)
TypeError: type() takes 1 or 3 arguments
type("A")
<class 'str'>
type("True")
<class 'str'>
type(True)
<class 'bool'>
type(False)
<class 'bool'>
x=55
y=56
x is y
False
x not is y
SyntaxError: invalid syntax
x is not y
True
x==y
False
