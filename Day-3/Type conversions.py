Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
float(a)
10.0
b=1.2
int(a)
10
int
<class 'int'>
(
int(b)
1
complex(b)
(1.2+0j)
str(b)
'1.2'
tuple(b)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
list(b)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
m="bunny"
print(m[::1])
bunny
print(m[::2])
bny
print(m[::3])
bn
c=2+5j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+5j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
d="bunny"
int(d)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'bunny'
float(d)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    float(d)
ValueError: could not convert string to float: 'bunny'
complex(d)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    complex(d)
ValueError: complex() arg is a malformed string
str(d)
'bunny'
list(d)
['b', 'u', 'n', 'n', 'y']
tuple(d)
('b', 'u', 'n', 'n', 'y')
dict(d)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(d)
True
set(d)
{'u', 'n', 'y', 'b'}
e= (10, 20)
int(e)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(e)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(e)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(e)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(e)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    complex(e)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(e)
'(10, 20)'
list(e)
[10, 20]
set(e)
{10, 20}
dict(e)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(e)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(e)
True
n = {1, 2, 3}
int(n)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(n)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(n)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    float(n)
TypeError: float() argument must be a string or a real number, not 'set'
complex(n)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex(n)
TypeError: complex() first argument must be a string or a number, not 'set'
str(m)
'bunny'
str(n)
'{1, 2, 3}'
tuple(n)
(1, 2, 3)
list(n)
[1, 2, 3]
dict(n)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(n)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(n)
True
True
True
x = {
    "name": "Alice",
    "age": 21
}
int(x)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int(x)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(x)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    float(x)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> complex(x)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    complex(x)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(x)
"{'name': 'Alice', 'age': 21}"
>>> list(x)
['name', 'age']
>>> tuple(x)
('name', 'age')
>>> set(x)
{'name', 'age'}
>>> bool(x)
True
>>> v = True
>>> int(v)
1
>>> float(v)
1.0
>>> complex(v)
(1+0j)
>>> str(v)
'True'
>>> list(v)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    list(v)
TypeError: 'bool' object is not iterable
>>> tuple(v)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    tuple(v)
TypeError: 'bool' object is not iterable
>>> set(v)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    set(v)
TypeError: 'bool' object is not iterable
>>> dict(v)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dict(v)
TypeError: 'bool' object is not iterable
>>> bool(v)
True
