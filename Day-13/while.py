'''
i=1
while i<11:
    print(i)
    i+=1
   
    
i=2
while i<21:
    print(i)
    i+=2

    
i=20
while i>0:
    print(i)
    i-=1
    
    


l='python programming'
i=0
while i>0:
    i+=1
'''
moves=30
while moves>1:
    s=input("[W] in or [c]ontime:").upper()
    if s=='W':
        print("You won the name ")
        break
    moves-=1
    print(f'{moves} moves are left')
else:
    print("Game over")