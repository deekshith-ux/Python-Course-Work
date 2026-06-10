data={
    'bunny':{'status':True,'python':98,'mysql':95,'flask':94},
    'mini':{'status':True,'python':78,'mysql':65,'flask':84},
    'honey':{'status':False,'python':None,'mysql':None,'flask':None},
    'karthi':{'status':True,'python':68,'mysql':55,'flask':64},
    'josh':{'status':True,'python':33,'mysql':25,'flask':34},
    }
name=input("enter your name:")
if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=total/3
        if avg>=90:
            print(f'congrats {name} , you are first')
        elif avg>=70:
            print(f'Good {name},keep it up')
        elif avg>=35:
            print(f'{name}, better luck next time')
        else:
            print(f'{name}, u have faild my boy')
    else:
        print(f'{name},Didnt write exam')
else:

    print(f'{name}s ,data didnt find')
    
