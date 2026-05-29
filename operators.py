Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
__________
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __________
NameError: name '__________' is not defined


-----------------
SyntaxError: invalid syntax
#arthimatic
a=10
b=20
a+b
30
a-b
-10
a*b
200
a/b
0.5
a//b
0
a%b
10
a**b
100000000000000000000
2**b
1048576


____
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ____
NameError: name '____' is not defined
#assignment
m=5
n=9
m=n
a<b
True
a>b
False
a<=b
True
a>=b
False
a==b
False
a!=b
True
a+=b
#assigment
a
30
a-=b
a
10
a*=b
a
200
a/=b
a
10.0
a//=b
a
0.0
a%=b
a
0.0
a**=3
a
0.0
a
0.0
y=5
y
5
y**=2
y
25
#logical
k=4
l=8
k and l
8
k or l
4
k not l
SyntaxError: invalid syntax
a= True
b= False
a and b
False
a or b
True
a not b
SyntaxError: invalid syntax
s=12
s//=5
s
2
g=20
f=10
g%20==0 and f%20==0 and a>b
False
g%20==0 or f%20==0 or a>b
True
a>b
True
not a>b
False
#membership
a="python programming"
a

a
'python programming'
'a' in a
True

'a' not in a
False
'a' is a
False
#identify
x=[1,2,3,4,5]
z=[1,2,3,4,5]
x==z
True
x=b
b
False
b=x
b
False
c=x
c
False
x ix z
SyntaxError: invalid syntax
x is z
False
15 & 2
2
15 | 2
15
~12
-13
15 ^ 2
13
15 >> 2
3
15 << 2
60
~-1
0
>>> a=python
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a=python
NameError: name 'python' is not defined
>>> a="python"
>>> b=12.3
>>> c=2
>>> print(a,b,c)
python 12.3 2
>>> print("a",a,"b",b,"c",c,spe,end='Mini')
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    print("a",a,"b",b,"c",c,spe,end='Mini')
NameError: name 'spe' is not defined
>>> print("a",a,"b",b,"c",c,sep,end='Mini')
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    print("a",a,"b",b,"c",c,sep,end='Mini')
NameError: name 'sep' is not defined. Did you mean: 'set'?
>>> print("a=",a,"b=",b,"c=",c,spe,end='Mini')
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    print("a=",a,"b=",b,"c=",c,spe,end='Mini')
NameError: name 'spe' is not defined
>>> print("a=",a,"b=",b,"c=",c,sep,end='Mini')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    print("a=",a,"b=",b,"c=",c,sep,end='Mini')
NameError: name 'sep' is not defined. Did you mean: 'set'?
>>> print("a=",a,"b=",b,"c=",c,sep='',end='Mini')
a=pythonb=12.3c=2Mini
>>> print(f'a=
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a={a} b={b} c={c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a={a} b={b} c={c})
...       
... print(f'a={a} b={b} c={c}')
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a={a} b={b} c={c}')
...       
a=python b=12.3 c=2
