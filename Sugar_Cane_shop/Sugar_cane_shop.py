import json as data

#def suger_cane_shop():
		#get into (try)to load the file if it existing
		#if not existing go into (except)
		#to initialize dectionary including all data	
try:
	with open("suger_cane_shop.json", 'r') as internal_file:
		#open the file where the sales stored 
		stored_data = data.load(internal_file)
		
except:
	stored_data = {
	"Large" : 0,
	"Medium": 0,	
	"Small" : 0,
	"Total" : 0,
	"Sales" :[]
	}
	
while True:
	print("Hello we wish you are fine\n")
	print("What is the drink size you want ?\n")
	print("Large cost 10, medium cost 5, Small cost 3\n")
	print("For large  press 1")
	print("For Medium press 2")
	print("For Small  press 3")
	print("To  Exit   press Esc")
	
	size =input()   #Storing the variable
	
	if size =='1':
		stored_data["Large"] +=1   #saving that you sold one large 
		stored_data["Total"] +=10  #saving that you have the cost of one large 
		stored_data["Sales"].append("Large") #inmport that you bought large
		print("You ordered large size")
		print("Enjoy your time")
		
	
	elif size =='2':
		stored_data["Medium"] +=1   #saving that you sold one Medium 
		stored_data["Total"] +=5    #saving that you have the cost of one Medium 
		stored_data["Sales"].append("Medium") #inmport that you bought Medium
		print("You ordered Medium size")
		print("Enjoy your time")
		
		
	elif size =='3':
		stored_data["Small"] +=1   #saving that you sold one Small 
		stored_data["Total"] +=3   #saving that you have the cost of one Small 
		stored_data["Sales"].append("Small") #inmport that you bought small 
		print("You ordered Small size")	
		print("Enjoy your time")
		
		
	elif size=='Esc':
		print("Enjoy your time")
		with open("suger_cane_shop.json", 'w')as internal_file:
			data.dump(stored_data, internal_file)	
		#return
		break
	
		
	
#suger_cane_shop()		
	