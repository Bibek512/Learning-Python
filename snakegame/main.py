import random
youdict={"w":0,'s':1,'g':2}

computer=random.choice([0,1,2])
youchose=input('Enter your choice: ')

if youchose not in youdict:   
        print("Something went wrong:")
        exit()

you=youdict[youchose]
    

revdict={0:'Water',1:'Snake',2:'Gun'}

print(f'You choose {revdict[you]} and Computer choose {revdict[computer]}')


if(you==computer):
    print('Draw!!!')

else:
    if(computer==0 and you==1 or computer==1 and you==2 or computer==2 and you==0): 
        print('You Win')
    else:
        print('Computer Win')
    # if(computer==0 and you==1): 
    #     print('You Win')
    # elif(computer==0 and you==2): 
    #     print('Computer Win')
    # elif(computer==1 and you==0): 
    #     print('Computer Win')
    # elif(computer==1 and you==2): 
    #     print('You Win')
    # elif(computer==2 and you==0): 
    #     print('You Win')
    # elif(computer==2 and you==1): 
    #     print('Computer Win')
    
     