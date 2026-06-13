'''
s="python"
for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i],s[j],sep='',end=" ")


l=[[1,2,3],[4,5,6],[7,8,9]]
t=0

for i in l:
    for j in i:
         t+=j
print(t)

d={
    '1234':{'pin':4567,'balance':2300},
    '2345':{'pin':9867,'balance':5300},
    '3456':{'pin':5678,'balance':6300},
    '4567':{'pin':9876,'balance':7300}
}
for i in d:
    print("Account number:",i)
    print("pin number:",d[i]['pin'])


for row in range(5):
    for col in range(5):
        print(col,end=' ')
    print()

n=int(input("enter a nuber:"))
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()
    
n=int(input("enter the number"))
for row in range(n):
    for col in range(n):
       print(col%2,end=' ')
    print()


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()

n=int(input("enter number:"))
for i in range(n):
    for j in range(n-i):
        print("*",end=' ')
    print()
    
n=int(input("enter number:"))
for i in range(n):
    for sp in range(n-1-i):
        print(' ',end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
'''
n=int(input("enter number:"))
for i in range(n):
    for sp in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print("*",end=' ')
    print()