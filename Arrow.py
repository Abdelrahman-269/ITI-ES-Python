lines=5
spaces=lines

for n in range(1, lines,1):
    print(" ",(str)spaces+""*n)
    spaces-=1
print(" ",lines*2)

for n in range(lines,0,-1):
    print(" ",spaces+""*n)
    spaces+=1
sleep(0.5)
os.system('cls')
for n in range(1,int(lines),1):
    print(" ",((int)(lines)-1) + ""*n)
	
print ("",lines*2)
for n in range(lines-1,1,-1):
    print(" ",((int)(lines)-1) + ""*n)
sleep(0.5)
os.system('cls')