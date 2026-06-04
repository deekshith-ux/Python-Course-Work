Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
h=(6,7,8)
t+h
(1, 2, 3, 4, 5, 6, 7, 8)
t*5
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
r=(t+h)
r
(1, 2, 3, 4, 5, 6, 7, 8)
r=(t+h)*2
r
(1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8)
(1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8)
(1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8)

t[1]
2
t[::]
(1, 2, 3, 4, 5)
t[::-1]
(5, 4, 3, 2, 1)
6 in t
False
5 not in t
False
4 in t
True
t
(1, 2, 3, 4, 5)
6 in t
False
6 not in t
True
t
(1, 2, 3, 4, 5)
len(t)
5
sorted(t)
[1, 2, 3, 4, 5]
min(t)
1
max(t)
5
t.count(t)
0
t.index(10)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t.index(10)
ValueError: tuple.index(x): x not in tuple
t.index(5)
4
t.count(3)
1
.a=1,2,3
SyntaxError: invalid syntax
q
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    q
NameError: name 'q' is not defined
a
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=1,2,3
a
(1, 2, 3)
x,y,z=a
x
1
y
2
z
3
t=(1,2,3,[4,5,6],7,8)
t[3]
[4, 5, 6]
t.append(20)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    t.append(20)
AttributeError: 'tuple' object has no attribute 'append'
t[3].append(9)

t
(1, 2, 3, [4, 5, 6, 9], 7, 8)
t[3].append(9)
t
(1, 2, 3, [4, 5, 6, 9, 9], 7, 8)
s=set()
s
set()
s=(467,982,213,578,293,238,458)
s
(467, 982, 213, 578, 293, 238, 458)
s=(467,982,213,578,293,238,458)
s={467,982,213,578,293,238,458}
SyntaxError: multiple statements found while compiling a single statement
s={467,982,213,578,293,238,458}
s
{578, 467, 293, 213, 982, 458, 238}
s=set()
s
set()
s.add(2)
s
{2}
s.add(78.8)
s
{2, 78.8}
s.add("bunny")
s
{2, 78.8, 'bunny'}
s.add([1,2,3,])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.add([1,2,3,])
TypeError: unhashable type: 'list'
s.add((1,2,3))
s
{2, (1, 2, 3), 78.8, 'bunny'}
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.add({1,2,3})
TypeError: unhashable type: 'set'
s.add({a:1,b:2})
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.add({a:1,b:2})
NameError: name 'b' is not defined
s.add(True)
s
{True, 2, (1, 2, 3), 78.8, 'bunny'}
s.add(False)
s
{False, True, 2, (1, 2, 3), 78.8, 'bunny'}
a={1,2,3,4,5}
b={4,5,6,7,8}
a | b
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a & b
{4, 5}
>>> a ^ b
{1, 2, 3, 6, 7, 8}
>>> a - b
{1, 2, 3}
>>> a
{1, 2, 3, 4, 5}
>>> a <= {1}
False
>>> a >= {1}
True
>>> a <= {1,2}
False
>>> a >= {1,2}
True
>>> a
{1, 2, 3, 4, 5}
>>> b
{4, 5, 6, 7, 8}
>>> a.isdisjoint(b)
False
>>> a.isdisjoint({66,88})
True
>>> a
{1, 2, 3, 4, 5}
>>> a.add(6)
>>> a
{1, 2, 3, 4, 5, 6}
>>> a.update({7,8,9})
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> a.remove(7)
>>> a
{1, 2, 3, 4, 5, 6, 8, 9}
>>> a.discard(7)
>>> a
{1, 2, 3, 4, 5, 6, 8, 9}
>>> a.remove(7)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.remove(7)
KeyError: 7
>>> a.clear()
>>> a
set()
