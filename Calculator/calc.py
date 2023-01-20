print("Select Mode,Please")
print("1 for scientific mode")
print("2 for programming mode")

#Mode=input()
#if Mode=="1":  #Get in scientific mode
	print('Welcome in scientific mode')
	print('Enter the first number: ')
	num1=input()
	print('Enter the operation: ')
	operation=input()
	print('Enter the second number: ')
	num2=input()
	
	if operation=="+":
		print('The summation is {}'.format(float(num1)+float(num2)))
	elif operation=="-":
		print('The subtraction is {}'.format(float(num1)-float(num2)))
	elif operation=="*":
		print('The multiplication is {}'.format(float(num1)*float(num2)))
	elif operation=="/":
		print('The division is {}'.format(float(num1)/float(num2)))
	elif operation=="%":
		print('The remainder is {}'.format(float(num1)%float(num2)))
	elif operation=="//floor division":
		print('The sum is {}'.format(float(num1)//float(num2)))
	elif operation=="**":
		print('The exponential is {}'.format(float(num1)**float(num2)))
	else:
		print('Sorry, it is invaild operation')
			

	
	
elif Mode=="2":   #Get in programming mode
	print('Welcome in programming mode')
	print('Enter the type of the number')
	print('10 for decimal')
	print('2 for binary')
	print('8 for octal')
	print('16 for hexadecimal')
	
	type=input()
	
	print('Enter the number: ')
	number=input()
	
	if type=="10":
		print(bin(int(number)))
		print(oct(int(number)))
		print(hex(int(number)))
	
	
	elif type==2:
	#	print(int(number))
	#	print('Decimal: %d'%bin(number))
		print(oct(bin(number)))
		print(hex(bin(number)))
	
	elif type=="8":
		print('Decimal: %d'%number)
		print(bin(int(number)))
		print(hex(int(number)))
	
	elif type=="16":
		print(int(int(number)))
		print(bin(int(number)))
		print(oct(int(number)))
	

#print('Enter any number to convert: ')
#prog_num=input()
#prog_num=int(prog_num)
#print("Enter the conversion type")
#conversion_type=input()
## if conversion_type==("b->d"|1):
#	# print('The result is {}'.format(dec(prog_num)))
#if conversion_type==(2):
#    print('The result is {}'.format(hex(prog_num)))
	# elif conversion type==("b->o"||3)
	# elif conversion type==("d->b"||4)
	# elif conversion type==("d->h"||5)
	# elif conversion type==("d->o"||6)
	# elif conversion type==("h->b"||7)
	# elif conversion type==("h->d"||8)
	# elif conversion type==("h->o"||9)
	# elif conversion type==("o->b"||10)
	# elif conversion type==("o->d"||11)
	# elif conversion type==("o->x"||12)
	 
	 
	 
	 
else:
	print('Sorry, your request is not available')