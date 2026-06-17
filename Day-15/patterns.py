'''
n=int(input("enter number:"))
mid=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==mid or i==n-1 or j==0 or j==mid or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input("enter number:"))
mid=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==mid or  j==0 or j==i or j==n-1 or i+j==n-1 or j==mid:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input("enter number:"))
mid=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==mid:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
            '''