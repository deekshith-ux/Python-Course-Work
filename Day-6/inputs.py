Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

name=input("enter your name")
enter your namebunny
name
'bunny'
age=int(input("enter your age:"))
enter your age:21
age
21
gpa=float(input("enter gpa:")
        )
enter gpa:7.7
gpa
7.7
class
SyntaxError: invalid syntax
class(age)
SyntaxError: invalid syntax
'bunny mini honey karthi sing'.split('')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    'bunny mini honey karthi sing'.split('')
ValueError: empty separator
'bunny mini honey karthi sing'
'bunny mini honey karthi sing'
'bunny mini honey karthi sing'.split('')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    'bunny mini honey karthi sing'.split('')
ValueError: empty separator
KeyboardInterrupt
KeyboardInterrupt
'bunny mini honey karthi sing'.split(' ')
['bunny', 'mini', 'honey', 'karthi', 'sing']
'bunny/mini/honey/karthi/singh'.split('/')
['bunny', 'mini', 'honey', 'karthi', 'singh']
prices=tuple(int,input("enter prices"))
enter prices1 2 3 4 5 66
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    prices=tuple(int,input("enter prices"))
TypeError: tuple expected at most 1 argument, got 2
prices=tuple(int,input("enter prices")).split()
enter prices1 2 3 4 5 6
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    prices=tuple(int,input("enter prices")).split()
TypeError: tuple expected at most 1 argument, got 2
prices=tuple(map(int,input("enter prices:"))).split
enter prices:11 23 34 45 56 67
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    prices=tuple(map(int,input("enter prices:"))).split
ValueError: invalid literal for int() with base 10: ' '
prices=tuple(map(int,input("enter prices:"))).split()
enter prices:12 23 34 45 56 
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    prices=tuple(map(int,input("enter prices:"))).split()
ValueError: invalid literal for int() with base 10: ' '
prices=tuple(map(int,input("enter prices:").split()))
enter prices:12 23 34 56 67
prices
(12, 23, 34, 56, 67)
rating=set(map(int,input("enter rating:").split()))
enter rating:1 2 4 56 7
rating
{1, 2, 4, 7, 56}
rat=set(map(float,input("enter rating:").split()))
enter rating:1.2 2.3 4.3 5.6
rat
{1.2, 2.3, 4.3, 5.6}
rat=tuple(map(float,input("enter rating:").split()))
enter rating:1.2 2.3 4.3 5.6
rat
(1.2, 2.3, 4.3, 5.6)
rat1=list(map(float,input("enter rating:").split()))
enter rating:1.2 2.3 4.3 5.6
rat1
[1.2, 2.3, 4.3, 5.6]
username,password=input("enter username & pass:").split()
enter username & pass:codegnan,c@124
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    username,password=input("enter username & pass:").split()
ValueError: not enough values to unpack (expected 2, got 1)
KeyboardInterrupt
username,password=input("enter username & pass:").split()
enter username & pass:codegnan x@123
username
'codegnan'
pass
password
'x@123'
a,b,c,d=list(map(int,input("enter sides:").split()))
enter sides:2 3 4 5
a
2
s
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s
NameError: name 's' is not defined
b
3
c
4
d
5
prices,discounts=set(map(float,input("enter price and discounts:").split()))
enter price and discounts:23.3 54.9
prices
54.9
discounts
23.3
a=eval(input())
a
234
234
a
2
b=eval(input())
435.7
b
435.7
type(b)
<class 'float'>
#string operations
a=bunnylo
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a=bunnylo
NameError: name 'bunnylo' is not defined
a="bunny"
b="mini"
a+b
'bunnymini'
>>> (a+b)*3
'bunnyminibunnyminibunnymini'
>>> type(a)
<class 'str'>
>>> rep(a)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    rep(a)
NameError: name 'rep' is not defined. Did you mean: 'repr'?
>>> a="bunny""
SyntaxError: unterminated string literal (detected at line 1)
>>> a="bunnY"
>>> a[1]
'u'
>>> a[::-1]
'Ynnub'
>>> a[::1]
'bunnY'
>>> a[1:]
'unnY'
>>> a[:-1]
'bunn'
>>> a[3:]
'nY'
>>> 'nY'
'nY'
>>> a="bunny","mini","honey"
>>> a
('bunny', 'mini', 'honey')
>>> a[1]
'mini'
>>> a[1:2:1]
('mini',)
>>> 
>>> len(a)
3
>>> a.upper()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.upper()
AttributeError: 'tuple' object has no attribute 'upper'
>>> a.lower()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.lower()
AttributeError: 'tuple' object has no attribute 'lower'
