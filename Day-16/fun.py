#
def wish(name):
    print(f'welcome {name}')
wish('bunny')
wish('mini')


def isprime(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
num=int(input())
isprime(num)


def fac(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num=int(input("Enter number:"))
print("Factorial:",fac(num))


def iseven(num):
    if num%2==0:
        return f'{num} - Even Number'
    else:
        return f'{num} - odd Number'
print(iseven(12))
print(iseven(13))


def prime(num):
    for i in range(2,num//2):
        if num%2==0:
            return f'{num} - Not Prime Number'
    return f'{num} - Prime number'
num=int(input("enter number:"))
print(prime(num))



# position maping(arguments)
def display(n,e,p):
    print("Name:",n)
    print("email:",e)
    print("password:",p)
    
display('bunny','bunny@123','bxn')
display('mini@123','mini','ninid')


#keyword arguments.
def display(n,e,p):
    print("Name:",n)
    print("email:",e)
    print("password:",p)
    
display(n='bunny',e='bunny@123',p='bxn')
display(p='mini@123',n='mini',e='ninid')


#Default argument.
def display(*names):
    print("Names:",names)
    
    
display('bunny','mini','honey','karthi')
display('bunny','mini','honey',)
display('bunny','mini')
display('bunny')


#variable Argument

def display(**names):
    print("Names:",names)
    
display(k1='bunny',k2='mini',k3='honey',)
display(k1='bunny',k2='mini')
display(k1='bunny')




