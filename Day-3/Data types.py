Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
b="bunny"
type(b)
<class 'str'>
Myvar=10
print(Myvar)
10
s="bunny"
id(s)
1831936881744
s.append(mini)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.append(mini)
AttributeError: 'str' object has no attribute 'append'
l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
l(id)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l(id)
TypeError: 'list' object is not callable
l=[1,2,3,4,5]
l(id)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l(id)
TypeError: 'list' object is not callable
l=[1,2,3,4,5]
id(l)
1831941843968
l.append(50)
l
[1, 2, 3, 4, 5, 50]
id(l)
1831941843968
s=bunny
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s=bunny
NameError: name 'bunny' is not defined
s="bunny"
s
'bunny'
s=s+mini
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s=s+mini
NameError: name 'mini' is not defined. Did you mean: 'min'?
>>> s=s+"mini"
>>> s
'bunnymini'
>>> c=2+9i
SyntaxError: invalid decimal literal
>>> c=3+7i
SyntaxError: invalid decimal literal
>>> c=5+7j
>>> c
(5+7j)
>>> type(c)
<class 'complex'>
>>> t=(1,2,3,4,5)
>>> type(t)
<class 'tuple'>
>>> t
(1, 2, 3, 4, 5)
>>> t.append(6)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t.append(6)
AttributeError: 'tuple' object has no attribute 'append'
>>> s1={1,2,3,4,5}
>>> type(s1)
<class 'set'>
>>> s1
{1, 2, 3, 4, 5}
>>> s2="bunny"
>>> len(s2)
5
>>> s1="bunny'
SyntaxError: unterminated string literal (detected at line 1)
>>> s1="bunny"
>>> s2="mini"
>>> s3=s1+' '+s2
>>> s3
'bunny mini'
>>> sum1=567
>>> sum2=786
>>> sum1_and_sum2=f'sum of {sum1} and {sum2} is {sum1+sum2}'
>>> sum1_and_sum2
'sum of 567 and 786 is 1353'
