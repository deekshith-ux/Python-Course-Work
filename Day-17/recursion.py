'''
# seq of numbers
def func(num):
    if num==0:
        return 
    print(num,end=' ')
    func(num-1)
    print(num,end=' ')
func(5)

#sum of numbers
def sumofd(n):
    if n==0:
        return 0
    return n+sumofd(n-1)
    
print(sumofd(5))


#product of numbers
def sumofd(n):
    if n==0:
        return 1
    return n*sumofd(n-1)
    
print(sumofd(5))

#powers
def power(b,p):
    if p==0:
        return 1
    return b*power(b,p-1)
    
print(power(2,4))

'''

def reverseofstr(s,ind):
    if ind==0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)
l="Python Programmin"
print(reverseofstr(l,len(l)-1))