'''
syntax error is compiler
logical mistake is runtime error
value error,name error,key error,index error,


'''
'''
try:
    a=int(input("enter the age:"))
    #print(12/0)
    #print(b)
    #print(13+'14')
    d={1:1,2:2}
    #print(d[4])
    l=[1,2,3]
    #print(l[10])
except ValueError:
    print("Enter the age in a digit[0-9] format")
except ZeroDivisionError:
    print("Cant divide with zero")
except NameError:
    print("Define var first")
except TypeError:
    print("Add same data types")
except KeyError:
    print("key is not present")
except IndexError:
    print("Index is out of range")
else:
    print("Age:",a)
finally:
    print("Thankyou")
    
    
try:
    a=int(input("enter the age:"))
    #print(12/0)
    #print(b)
    #print(13+'14')
    d={1:1,2:2}
    #print(d[4])
    l=[1,2,3]
    #print(l[10])
except(ValueError,ZeroDivisionError,NameError,TypeError,KeyError,IndexError) as e:
    print("Error Occured",e)
else:
    print("No Error ocuured")
finally:
    print("Thankyou")
    
try:
    a=int(input("enter the age:"))
    #print(12/0)
    #print(b)
    #print(13+'14')
    d={1:1,2:2}
    #print(d[4])
    l=[1,2,3]
    #print(l[10])
except Exception as e:
    print("Error Occured",e)
else:
    print("No Error ocuured")
finally:
    print("Thankyou")
'''

try:
    amount=int(input("Enter amount to withdraw:"))
    if amount<0:
        raise Exception("Enter the amount greater than zero")
except Exception as e:
    print("Error Occured",e)
else:
    print("No Error ocuured")
finally:
    print("Thankyou")    