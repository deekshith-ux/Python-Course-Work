'''
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

n=int(input("enter number:"))
for i in range(n):
    for sp in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print("*",end=' ')
    print()


n=int(input("enter number:"))
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=' ')
    print()
    
n=int(input("enter number:"))
for i in range(n):
    for j in range(i+1):
        print(i+j+1,end=' ')
    print()
    '''
n=int(input("enter number:"))
c=1
for i in range(n):
    for j in range(i+1):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()