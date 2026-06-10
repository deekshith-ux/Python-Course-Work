'''
for var in seq:
    print(var)
    
    
s=input("Enter a String:")
for i in s:
    print(i)


l=['sugar','salt','rice','wheat']
for item in l:
    print(item)
    
    
d={'name':'john','batch':55,'course':'PFS','skills':['python','java','sql']}
for i in d:
    print(i,d[i])


i=10
for i in range(1,10,2):
    print(i)
    

n=5
for i in range(n):
    i=i**2
    print(i)

for i in range(20,1):
    print(i)
 
n=5
for i in range(1,n+1):
    print("*"*i)

s="looping statements"
for i in enumerate(s):
    print(i[0],i[1])


for i in range(10):
    if i==5:
        break
    print(i)


for i in range(10):
    if i==5:
        continue
    print(i)
    
for i in range(20):
    pass

s="Looping statements"
for i in s:
    if i in 'aeiouAEIOU':
        print(i)


l=[34,45,67,34,78,34,79,4,4,89,5,443,345,6,77,33,22,89]
for i in l:
    if i%2==0:
        print(i)
        
s=(25,66,84,75,29,19,37,28,51,47,67,86,28,16)
for i in s:
    if i%3==0:
        print(i)
        
d=d={'name':'john','batch':55,'course':'PFS','skills':['python','java','sql']}
for i in d:
    if d[i]:
        print(i)
        
t=(9,2,13,4,5,6)
for i in range(6):
    print(i*t[i])
    
'''



name={'subbu','naresh','bunny','mini','josh'}
for i in name:
    print(i[0].upper(),i[1])
        
      