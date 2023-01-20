print('Welcome to ITI shop')

print('if you are a customer press 1')
print('if you are an owner press 2')
print('To exit press 0')

products ={
		"Banana": [30,15],  #[quantity(kg),price(L.E/kg)]
		"Apple": [20,30],
		"Orange": [25,20]
		}
		
		
mode=int(input())

if mode==1:
		
		print('Banana cost 15L.E/KG')
		print('Apple  cost 30L.E/KG')
		print('Orange cost 20L.E/KG')
#print('TO show our products press 1')
		print('To buy our products press 1')
		fruit=input('Enter the product you want to buy')
		
		weight=input('Enter the quantity')

		print('You want', weight, 'kilo of ' +str(fruit))

elif mode==2:
		print('To add new product and its price press 1')
		print('To show the current products press 2')
		print('To change price of product press 3')
		
		update=int(input())
		if update==1:
			product=input('Enter new product')
			price=input('Enter the price')
			print("The new product is"+str(product) +" and its price is "+str(price))
		
		elif update==2:
			print(products) 
			
		elif update==3:
			product=input('Enter the product which you want to change its price')
			price=input('Enter the new price')
			print("The product is"+str(product) +" and its new price is "+str(price))
			
		
elif mode==0:
		print('You exited the app')	

else:
	    print('Invalid number')		
		
			
		