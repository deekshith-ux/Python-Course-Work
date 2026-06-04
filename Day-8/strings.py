Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='    hello    world     '
s
'    hello    world     '
s.strip()
'hello    world'
s.lstrip()
'hello    world     '
s.rstrip()
'    hello    world'
a="spiderbunny.py"
s
'    hello    world     '
a
'spiderbunny.py'
>>> a.startswith('bun')
False
>>> a.startswith('spi')
True
>>> a.endswith('py')
True
>>> 'jhbfviuagvbeyus'.isalpha()
True
>>> 'ksdhcu67387'.isalpha()
False
>>> '142567'.isalnum()
True
>>> 'kvjncyu&^*(&(HG'.isalnum()
False
>>> 'jchiugybgdcy'.islower()
True
>>> 'KJCDUBAIUYC'.isupper()
True
>>> ' '.isspace()
True
>>> 'hello    '.isspace()
False
>>> 'Ujj Nuj'.istitle()
True
>>> 'Jjhd hjjj'.istitle()
False
>>> 'a'.isidentifier()
True
>>> b.isidentifier()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b.isidentifier()
NameError: name 'b' is not defined
>>> 857.87.isdecimal()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    857.87.isdecimal()
AttributeError: 'float' object has no attribute 'isdecimal'
>>> l=[]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4,5]
>>> m=[6,7,8,9]
>>> l+m
[1, 2, 3, 4, 5, 6, 7, 8, 9]
