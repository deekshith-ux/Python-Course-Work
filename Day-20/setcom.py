
s=set()
for i in range(1,11):
    s.add(i)
print(s)

s1={i for i in range(1,11)}
print(s1)



d={}
for i in range(1,11):
    d[i]=i*i
print(d)


d1={i:i*i for i in range(1,11)}
print(d1)



d={}
for i in range(5):
    n=input("enter name:")
    m=int(input("enter number"))
    d[(input("enter name:"))]==d[int(input("enter number"))]
print(d)
    
res={input("enter name:"):int(input("enter number")) for i in range(5)}
print(res)
