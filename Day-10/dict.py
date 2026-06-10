Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dictionaries
d={}
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d[1]='int'
d
{'k1': 'v1', 'k2': 'v2', 1: 'int'}
d={}
d
{}
d[1]='int'
d
{1: 'int'}
d[2]='float'
d[3]='complex'
d
{1: 'int', 2: 'float', 3: 'complex'}
d[4]='str'
d
{1: 'int', 2: 'float', 3: 'complex', 4: 'str'}
d[5]='tuple'
d
{1: 'int', 2: 'float', 3: 'complex', 4: 'str', 5: 'tuple'}
d[{1,2,3}]='set'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d[{1,2,3}]='set'
TypeError: unhashable type: 'set'
d[(1,2,3)]='tuple'
d
{1: 'int', 2: 'float', 3: 'complex', 4: 'str', 5: 'tuple', (1, 2, 3): 'tuple'}
d[{}]='dict'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d[{}]='dict'
TypeError: unhashable type: 'dict'
d[1]=2
d[2]=2.3
d[3]=2+9j
d[4]=[1,2,3]
d[5]=(1,2,3)
d[6]={1,2,3}
d
{1: 2, 2: 2.3, 3: (2+9j), 4: [1, 2, 3], 5: (1, 2, 3), (1, 2, 3): 'tuple', 6: {1, 2, 3}}
d[7]=False
s
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s
NameError: name 's' is not defined
d
{1: 2, 2: 2.3, 3: (2+9j), 4: [1, 2, 3], 5: (1, 2, 3), (1, 2, 3): 'tuple', 6: {1, 2, 3}, 7: False}


d={'bunny':20,'honey':30,'vinny':40,'josh':50,'mini':60
   d
   
SyntaxError: '{' was never closed
d={'bunny':20,'honey':30,'vinny':40,'josh':50,'mini':60}
   
d
   
{'bunny': 20, 'honey': 30, 'vinny': 40, 'josh': 50, 'mini': 60}
d['bunny']
   
20
d.get('bunny','user not found')
   
20
d.get('karthi','user404error')
   
'user404error'
'bunny'in d
   
True
d.keys()
   
dict_keys(['bunny', 'honey', 'vinny', 'josh', 'mini'])
d.values()
   
dict_values([20, 30, 40, 50, 60])
d.items()
   
dict_items([('bunny', 20), ('honey', 30), ('vinny', 40), ('josh', 50), ('mini', 60)])
sorted(d)
   
['bunny', 'honey', 'josh', 'mini', 'vinny']
min(d)
   
'bunny'
max(d)
   
'vinny'
len(d)
   
5
>>> d
...    
{'bunny': 20, 'honey': 30, 'vinny': 40, 'josh': 50, 'mini': 60}
>>> d['bunny']=90
...    
>>> d
...    
{'bunny': 90, 'honey': 30, 'vinny': 40, 'josh': 50, 'mini': 60}
>>> d.update({'karthi':55,'singh':77})
...    
>>> d
...    
{'bunny': 90, 'honey': 30, 'vinny': 40, 'josh': 50, 'mini': 60, 'karthi': 55, 'singh': 77}
>>> d.pop('bunny')
...    
90
>>> d
...    
{'honey': 30, 'vinny': 40, 'josh': 50, 'mini': 60, 'karthi': 55, 'singh': 77}
>>> del d['mini']
...    
>>> d
...    
{'honey': 30, 'vinny': 40, 'josh': 50, 'karthi': 55, 'singh': 77}
>>> d.clear()
...    
>>> d
...    
{}
>>> d={'bunny': 90, 'honey': 30, 'vinny': 40, 'josh': 50, 'mini': 60}
...    
>>> d
...    
{'bunny': 90, 'honey': 30, 'vinny': 40, 'josh': 50, 'mini': 60}
>>> d.setdefault('karthi',90)
...    
90
>>> d
...    
{'bunny': 90, 'honey': 30, 'vinny': 40, 'josh': 50, 'mini': 60, 'karthi': 90}
>>> d.clear()
...    
>>> d
...    
{}
