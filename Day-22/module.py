
import sys

print(sys.argv)
print(sys.path)
print(sys.version)
print("Before Exit")
sys.exit()
print("After Exit")


#Platform
import platform
print(platform.system(),platform.release(),platform.processor())


#MATH
#sqrt
import math
print(math.sqrt(5))
#pow
print(math.pow(2,5))
#ciel
print(math.ceil(5.2))
#floor
print(math.floor(5.9))
print(round(39.9))
#absolute
print(math.fabs(-2))
#fact
print(math.factorial(5))
#gcd
print(math.gcd(8,28))
#LOG,SIN,COS,TAN
print(math.log(10,10))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))
#degrees,radians
print(math.degrees(20))
print(math.radians(20))

#random value-->generating random numbers
import random
random.seed(2)#---->to show op in same for many times
print(random.random()) #--->any random number
print(random.randint(1,6))#--->integer
print(random.uniform(1,6))#--->float
l=['python','java','c++','c','html']
print(random.choice(l)) #---->any one in the list
print(random.choices(l,k=2))#--->consider on k value
s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)

#collections
import collections
s='python programming language'
print(collections.Counter(s))

s='python programming language'
d=collections.defaultdict(int)
for i in s:
    d[i]+=1
print(d)

import collections
l=collections.deque()
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
print(l)

import itertools
print(list(itertools.combinations('abcd',2)))
print(list(itertools.permutations('abcd',2)))


import itertools
a=(list(itertools.combinations('abcd',2)))
b=(list(itertools.permutations('abcd',2)))
r=[''.join(i) for i in a]
r1=[''.join(j) for j in b]
print(r,r1)


