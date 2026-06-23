
'''
#LAMBDA --->in single line
#add
add=lambda a,b:a+b
print(add(24,78))

#string
wish=lambda name:f'Welcome to python {name}'
print(wish('bunny'))

#multi
multi=lambda a,b:a*b
print(multi(23,7))


#gst
gst=lambda price:price+price*0.18
print(gst(500))


#even
even=lambda x:x%2==0
x=int(input())
print(even(x))

#greater than
g=lambda a,b:a if a>b else b
print(g(3,4))
    
#even check
iseven=lambda x: f'{x}-Even number' if x%2==0 else f'{x}-Odd Nmber'
print(iseven(5))


# charge 
bill=lambda charge:charge if charge>99 else charge+30
print(bill(89))
print(bill(105))

#login checking
status=lambda login,instock:("You can buy a product" if instock else "Product is out of stock") if login else "Login pls" 
login=input()
instock=input()
print(status(login,instock))

#MAP--->updating each element
l=[1,2,3,4,5,6,7]
r=list(map(lambda i:i+10,l))
print(r)

#
d={'sugar':40,'salt':20,'milk':50}
gst=list(map(lambda i:,d.items()))
print(gst)

#FILTER
l=[1,2,3,4,5,6,7,8]
r=list(filter(lambda i:i%2==0,l))
print(r)

#
l=[1,2,3,4,5,6,7,8]
r=list(filter(lambda i:i>5,l))
print(r)

#
l=[1,2,3,4,5,6,7,8]
r=list(filter(lambda i:i%3==0,l))
print(r)


#REDUCE --> combining

from functools import reduce
l=[1,2,3,4,5,6,7,8,9]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda prod,i:prod*i,l)
m=reduce(lambda sub,i:sub-1,l)
n=reduce(lambda max,i:max if max>i else i,l)
h=reduce(lambda min,i:min if min<i else i,l)
print(s,p,m,n,h)

'''
#sorted of dict
d={'bunny':90,'honey':60,'mini':70}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))