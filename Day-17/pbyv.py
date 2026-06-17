'''
def update(n):
    n+=10
    print("Inside:",n)
n=10
update(n)
print("Outside:",n)

def update(n):
    n+=10
    print("Inside:",n)
n=10.4
update(n)
print("Outside:",n)

def update(n):
    n+=10
    print("Inside:",n)
n=10+4j
update(n)
print("Outside:",n)


def update(n):
    n+='mini'
    print("Inside:",n)
n='bunny'
update(n)
print("Outside:",n)

'''
def update(n):
    n+=(6,)
    print("Inside:",n)
n=(1,2,3,4,5)
update(n)
print("Outside:",n)
