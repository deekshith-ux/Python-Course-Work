'''
password='@bunny123'
for i in range(5):
    n=input("enter the password:")
    if n==password:
        print("welcome")
        break
    else:
        print("try again")

else:
    print("account locked try after 24hrs")



l=[2,3,4,5,8,10,34,12]
n=int(input("enter numner:"))
for i in l:
    if i==n:
        print(f'the number of {i} index is at {l.index(i)}')
        break
else:
    print("number not found")

 
n=input("Enter password:")
if len(n)>=8:
    s=set()
    for i in n:
        if i.isupper():
            s.add('u')
        elif i.lower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
    if len(n)==4:
        print("strong pass")
    else:
        print("weak pass")
else:
    print("weak pass")

    
'''


    
    

            



     