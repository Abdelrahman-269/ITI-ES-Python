import os
from time import sleep

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
    
lines=10
#The Rotating Arrow
while (1):
    #North
    for n in range(1,lines*2,2):          
            print(('*'*n).center(lines*2-1))
    for n in range(1,lines,2):
            print(('*').center(lines*2-1))
    sleep(0.05)
    os.system('cls')
#POINT RIGHT
    for n in range(1,int(lines),1):
        print(" "*((int)(lines)-1) + "*"*n)
    print ("*"*lines*2)
    for n in range(lines-1,1,-1):
        print(" "*((int)(lines)-1) + "*"*n)
    sleep(0.05)
    os.system('cls')
#print SOUTH
    for n in range(1,lines,2):
            print(('*').center(lines*2-1))
    for n in range(lines*2,1,-2):          
            print(('*'*n).center(lines*2-1))
    sleep(0.05)
    os.system('cls')
#pointing LEFT
    spaces=lines
    for n in range(1, lines,1):
        print(" "*spaces+"*"*n)
        spaces-=1
    print("*"*lines*2)
    
    for n in range(lines,0,-1):
        print(" "*spaces+"*"*n)
        spaces+=1
    sleep(0.05)
    os.system('cls')
   