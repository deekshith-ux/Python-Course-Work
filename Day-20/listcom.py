
res1=[]
for i in range(1,11):
    res1.append(i)
print(res1)
res2=[i for i in range(1,11)]
print(res2)

res3=[i for i in range(3,31,3)]
print(res3)

res4=[i for i in range(1,51,2)]
print(res4)

res5=[i for i in range(10,101,10)]
print(res5)

res6=[]
for i in range(7,71,7):
    res6.append(i)
print(res6)


#string...

a='python programming'
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)

l1=[i for i in a if i in 'aeiouAEIOU']
print(l1)



a=[1,2,34,5,67,8,9,9,3,46,7,88]
l=[]
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
        
print(l)
    

l1=[i if i%2==0 else 0 for i in a]
print(l1)



l=[int(input(f'Enter the number-{i+1}:')) for i in range(10)]
print(l)
             
             
l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)

l1=[j for i in range(3) for j in range(1,4)]
print(l1)


l=[[j for j in range(1,4)] for i in range(3)]
print(l)