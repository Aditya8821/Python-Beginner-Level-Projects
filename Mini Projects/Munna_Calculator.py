def mul():
  mu=1
  for x in range(len(list)):
       mu=mu*list[x]
  return(mu)
def add():
    global temp
    temp=0
    for x in range(length):
         temp=temp+list[x]
    return(temp)
def sub():
    global x
    global y
    x,y=list
    return(x-y)
def division():
    x,y=list
    return(x/y)
def reminder():
    x,y=list
    return(x%y)
def SMALL():
    small=list[0]
    for x in range(1,length):
        if(small>list[x]):
            small=list[x]
    return(small)
def LARGE():
     large=list[0]
     for x in range(1,length):
         if(large<list[x]):
             large=list[x]
     return(large)
def HCF():
    for i in range(SMALL(),0,-1):
        for j in range(length):
            if(length-1==j):
                if(list[j]%i==0):
                    return(i)
                else:
                     break


            if(list[j]%i==0):
                pass
            else:
                break
def LCM():
    large=LARGE()
    for i in range(large,mul()+1,large):
        for j in range(length):
            if(length-1==j):
                if(i%list[j]==0):
                    return(i)
            if(i%list[j]==0):
                pass
            else:
                break

def FIBONACCI():
    previous=0
    next=1
    temp=0
    for i in range(list[0]):
        print(previous,end=' ')
        temp=previous
        previous=next
        next=temp+previous
def FACTORIAL():
    fact=1
    for i in range(list[0],1,-1):
        fact=fact*i
    return(fact)  
       
    
print('===Welcome To Smart Calculator===')
print('My name is Bablu...Lets Breakitzz')
i=1
while(i):
   list=[]
   str2=[]
   str1=input('\nPlease Give Any Task to Me:')
   for s in str1.split():
        if(s.isdigit()):
            list.append(eval(s))
   str2=str1.lower()
   length=len(list)
   if('calculate' in str2):
       print("\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLY\n4.DIVISION\n5.MODULO\n6.HCF\n7.LCM\n8.FIBONACCI\n9.FACTORIAL")
       str3=int(input("\nSelect the operation: "))
       if(str3==1):
         print('\nAddition is =',add())
       elif(str3==2):
         print(sub())
       elif(str3==3):
         print('\nMultiply is=',mul())
       elif(str3==4):
         print(division())
       elif(str3==5):
         print(reminder())
       elif(str3==6):
         print('hcf is =',HCF())
       elif(str3==7):
         print(LCM())
       elif(str3==8):
         FIBONACCI()
         print('')
       elif(str3==9):
         print(list[0],'factorial is =',FACTORIAL());
     
   elif('End' in str2 or 'khatam' in str2 or 'ruk' in str2):
       print("\nOk Bye...")               
       i=0
   elif('name' in str2 and 'boss' not in str2):
       print('\nMy name is Bablu')
   elif('add' in str2 or 'plus' in str2 or 'jodke' in str2 or 'jod' in str2):
       print('\nAddition is =',add())
   elif('sub' in str2 or 'ghata' in str2 or 'minus'in str2):
       print(sub())
   elif('mul' in str2 or 'guna' in str2):
       print('\nMultiply is=',mul())
   elif('divi' in str2):
       print(division())
   elif('modu' in str2):
       print(reminder())
   elif('hcf' in str2 or 'gcd' in str2):
          print('hcf is =',HCF())
   elif('lcm' in str2):
       print(LCM())
   elif('fibon' in str2):
       FIBONACCI()
       print('')
   elif('fact' in str2):
       print(list[0],'factorial is =',FACTORIAL());
   elif('boss' in str2 or "baap" in str2):
       if str2=="boss":
           print('\nMy Boss Name is Satyam Tripathi')
       else:
           print('\nMera Baap Satyam Tripathi Hai')
   else:
     print("Sorry :( I'm not able to understand what you are saying")
     
