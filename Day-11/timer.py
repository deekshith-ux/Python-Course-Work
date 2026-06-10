hrs,mins=list(map(int,input("enter the time:").split(':')))
if 0<=hrs<=23 and 0<=mins<=59:
    if 4<=hrs<=11:
         print("Gummoringg!!")
    elif 12<=hrs<=16:
        print("Gud afternoon")
    elif17<=hrs<=19:
        print("Good eveningg")
    elif 20<=hrs<=23:
        print("Good nytt")
    elif 0<=hrs<=3:
        print("Its mid nytt")

else:
    print("invalid time")
    
