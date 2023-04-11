import random

#Aaryan Sharma
#101230220

name = input("Please enter your name: ") #individual's name
company = input("Hi "+ name + " please enter your company name: ") #company name

print("\nLets set up a sales menu for",company+".")

item = 1

while item<4:
    
    item1_name = input("Enter item 1's name: ")

    
    item1_price = input("Item 1's unit price: ")
    
    #user inputs price + quanity + name of item 
    while item == 1:
        
        while (item1_price.isalpha()):  #checking if valid
            if (item1_price.isalpha()):
                    item1_price= (input("Price must be a number, please try again: "))
            else:
                break          

        while not item1_price.replace('.','',1).isdigit():  #checking if valid
            if not item1_price.replace('.','',1).isdigit():
                (item1_price) = (input("Price, must be a positive number, please try again:"))
            else: 
                break
    
        item1_quantity = input("Item 1's quantity: ")     
    
        while (item1_quantity.isalpha()):   #checking if valid
                if (item1_price.isalpha()):
                    item1_price= (input("Quanity must be a number, please try again: "))
                else:
                    break
        
        while not item1_quantity.isdigit(): #checking if valid
            if not item1_quantity.isdigit():
                (item1_quantity) = (input("Quanity, must be a positive integer, please try again:"))
            else: 
                break
        
        item+=1 #calls next while loop 
    


    print("")
    item2_name = input("Enter item 2's name: ")

    
    item2_price = input("Item 2's unit price: ")
    
    #user inputs price + quanity + name of item 
    while item == 2:
        
        while (item2_price.isalpha()):  #checking if valid
            if (item2_price.isalpha()):
                    item2_price= (input("Price must be a number, please try again: "))
            else:
                break          

        while not item2_price.replace('.','',1).isdigit():  #checking if valid
            if not item2_price.replace('.','',1).isdigit():
                (item2_price) = (input("Price, must be a positive number, please try again:"))
            else: 
                break
    
        item2_quantity = input("Item 2's quantity: ")     
    
        while (item2_quantity.isalpha()):   #checking if valid
                if (item2_price.isalpha()):
                    item2_price= (input("Quanity must be a number, please try again: "))
                else:
                    break
        
        while not item2_quantity.isdigit(): #checking if valid
            if not item2_quantity.isdigit():
                (item2_quantity) = (input("Quanity, must be a positive integer, please try again:"))
            else: 
                break
        
        item+=1 #calls next while loop 
    
    print("")
    item3_name = input("Enter item 3's name: ")

    
    item3_price = input("Item 3's unit price: ")
    
    #user inputs price + quanity + name of item 
    while item == 3:
        
        while (item3_price.isalpha()):  #checking if valid
            if (item3_price.isalpha()):
                    item3_price= (input("Price must be a number, please try again: "))
            else:
                break          

        while not item3_price.replace('.','',1).isdigit():  #checking if valid
            if not item3_price.replace('.','',1).isdigit():
                (item3_price) = (input("Price, must be a positive number, please try again:"))
            else: 
                break
    
        item3_quantity = input("Item 3's quantity: ")     
    
        while (item3_quantity.isalpha()):   #checking if valid
                if (item3_price.isalpha()):
                    item3_price= (input("Quanity must be a number, please try again: "))
                else:
                    break
        
        while not item3_quantity.isdigit(): #checking if valid 
            if not item3_quantity.isdigit():
                (item3_quantity) = (input("Quanity, must be a positive integer, please try again:"))
            else: 
                break
        
        item+=1 #breaks while loop

#prints all items with prices and quanities, to allow the user for reading towards next part, in which one can now begin to buy the items
print("\nGreat!" + "\nHere is the e-list for "+ company +" .\n")
print("------------------ Welcome ------------------\n=============================================")
print("Please select the item you want to buy from \nthe following menu: ")
print("1.",item1_name,"($"+item1_price+")", "each",item1_quantity, "available" )
print("2.",item2_name,"($"+item2_price+")", "each",item2_quantity, "available" )
print("3.",item3_name,"($"+item3_price +")", "each",item3_quantity, "available" )
print("Press 4 when you are done!")
print("=============================================")






#what user wants to buy
item_number = int(input("Select Product: "))

#final prices
Current_Total=0
total_item1_price= 0
total_item2_price = 0
total_item3_price = 0

#items bought if user inputs 4 right away
item1_bought = 0
item2_bought = 0
item3_bought = 0

#respective final number of items bought
total_item1_bought = 0
total_item2_bought = 0
total_item3_bought = 0

while item_number == 1 or 2 or 3 or 4: 
    
    if item_number == 1:  #checks if input is valid for the next 3 while statements
        item1_bought = input("You have selected "+ item1_name+". How many would you like to buy?: ")
        while (item1_bought.isalpha()):
            if (item1_bought.isalpha()):
                item1_bought=input("Quanitity must be a number. Please try again: ")
            else: 
                break

        while not (item1_bought.isdigit()):
            if not (item1_bought.isdigit()):
                item1_bought = input("Quantitiy must be a positive integer. Please try again: ")
            else:
                break
        
        while int(item1_bought) > int(item1_quantity):
            if int(item1_bought) > int(item1_quantity):
                item1_bought = input("Sorry, only "+ str(item1_quantity)+"(s) are available in in stock. Please try again: ")
            else: 
                break
        
        #number of items bought saved to variable for end
        total_item1_bought += int(item1_bought)

        
        #turning into floats to calculate
        #storing in variables to be used later
        item1_quantity = int(item1_quantity)-int(item1_bought)
        total_item1_price = float(total_item1_price) + (int(item1_bought)*float(item1_price))

        print(item1_bought, item1_name+"(s) have been selected.")
        print("")

        #print statement after buy
        Current_Total = Current_Total + (int(item1_bought) * float(item1_price))
        print("Current total is",str(Current_Total)+".")
        print("="*45)
        print("Please select the item you want to buy from \nthe following menu: ")
        print("1.",item1_name,"($"+item1_price+")", "each",str(item1_quantity), "available" )
        print("2.",item2_name,"($"+item2_price+")", "each",item2_quantity, "available" )
        print("3.",item3_name,"($"+item3_price +")", "each",item3_quantity, "available" )
        print("Press 4 when you are done!")
        print("="*45)

        
    
    elif item_number == 2:  #checks if input is valid for the next 3 while statements
        item2_bought= input("You have selected "+item2_name+". How many would you like to buy?: ")
        while (item2_bought.isalpha()):
            if (item2_bought.isalpha()):
                item2_bought=input("Quanitity must be a number. Please try again: ")
            else: 
                break

        while not (item2_bought.isdigit()):
            if not (item2_bought.isdigit()):
                item2_bought = input("Quantitiy must be a positive integer. Please try again: ")
            else:
                break
        
        while int(item2_bought) > int(item2_quantity):
            if int(item2_bought) > int(item2_quantity):
                item2_bought = input("Sorry, only "+ str(item2_quantity)+"(s) are available in in stock. Please try again: ")
            else: 
                break
    
        #number of items bought saved to variable for end
        total_item2_bought += int(item2_bought)
        
        #turning into floats to calculate
        #storing in variables to be used later
        item2_quantity = int(item2_quantity)-int(item2_bought)
        total_item2_price = total_item2_price + (int(item2_bought)*float(item2_price))

        print(item2_bought, item2_name+"(s) have been selected.")
        print("")

        Current_Total = Current_Total + (int(item2_bought) * float(item2_price))
        print("Current total is",str(Current_Total)+".")
        print("="*45)
        print("Please select the item you want to buy from \nthe following menu: ")
        print("1.",item1_name,"($"+item1_price+")", "each",str(item1_quantity), "available" )
        print("2.",item2_name,"($"+item2_price+")", "each",str(item2_quantity), "available" )
        print("3.",item3_name,"($"+item3_price +")", "each",str(item3_quantity), "available" )
        print("Press 4 when you are done!")
        print("="*45)
    
    elif item_number == 3: #checks if input is valid for the next 3 while statements
        item3_bought= input("You have selected "+item3_name+". How many would you like to buy?: ")
        while (item3_bought.isalpha()):
            if (item3_bought.isalpha()):
                item3_bought=input("Quanitity must be a number. Please try again: ")
            else: 
                break

        while not (item3_bought.isdigit()):
            if not (item3_bought.isdigit()):
                item3_bought = input("Quantitiy must be a positive integer. Please try again: ")
            else:
                break
        
        while int(item3_bought) > int(item3_quantity):
            if int(item3_bought) > int(item3_quantity):
                item3_bought = input("Sorry, only "+ str(item3_quantity)+"(s) are available in in stock. Please try again: ")
            else: 
                break
        print(item3_quantity)
        
        #number of items bought saved to variable for end
        total_item3_bought+=int(item3_bought)

        #turning into floats to calculate
        #storing in variables to be used later
        item3_quantity = int(item3_quantity)-int(item3_bought)
        total_item3_price = total_item3_price + (int(item3_bought)*float(item3_price))

        print(item3_bought, item3_name+"(s) have been selected.")
        print("")
        
        #prints the statement 
        Current_Total = Current_Total + (int(item3_bought) * float(item3_price))
        print("Current total is",str(Current_Total)+".")
        print("="*45)
        print("Please select the item you want to buy from \nthe following menu: ")
        print("1.",item1_name,"($"+item1_price+")", "each",str(item1_quantity), "available" )
        print("2.",item2_name,"($"+item2_price+")", "each",str(item2_quantity), "available" )
        print("3.",item3_name,"($"+item3_price +")", "each",str(item3_quantity), "available" )
        print("Press 4 when you are done!")
        print("="*45)
    
    if item_number == 4:
        break

    item_number = int(input("Select Product: "))

tax = Current_Total * 0.13
Final_Total = tax + Current_Total



#prints the final statement with all numbers accounted for
print("Thank you!")

print("\nHere is your invoice")
print("="*45)
print("1.",item1_name,"x",total_item1_bought,   total_item1_price) 
print("2.",item2_name,"x",total_item2_bought,   total_item2_price)   
print("3.",item3_name,"x",total_item3_bought,   total_item3_price)
print("-"*30)
print("Subtotal:",           f'{float(Current_Total):0.2f}')
print("Tax:",           f'{float(tax):0.2f}')
print("-"*30)
print("Total:",         f'{float(Final_Total):0.2f}')


discount = input("Do you want to continue and the see the invoice(i) or cancel the transaction(c)?: ")



if (discount.lower()) == "c":
    print("Thank you for trying our system. Bye!")
else:
    x = random.randint(1,10)
    if 1<=int(x)<=6: #checks if customer is lucky
        discounted_subtotal = Current_Total - (Current_Total*0.10)  #the next four lines calculate discounted prices
        discount= Current_Total*0.10
        discounted_tax = discounted_subtotal*.13
        discounted_total = discounted_tax + discounted_subtotal
        print("Congratulations! You are a truly a lucky customer and have been qualified for a discount of 10%")    #the final print statement
        print("\nHere is your final receipt!")
        print("="*45)
        print("1.",item1_name,"x",total_item1_bought,   total_item1_price) 
        print("2.",item2_name,"x",total_item2_bought,   total_item2_price)   
        print("3.",item3_name,"x",total_item3_bought,   total_item3_price)
        print("-"*30)
        print("Subtotal (old):",           f'{float(Current_Total):0.2f}')
        print("Subtotal (new):",           f'{float(discounted_subtotal):0.2f}')
        print("Discount:",           f'{float(discount):0.2f}')
        print("Tax:",           f'{float(discounted_tax):0.2f}')
        print("-"*30)
        print("Total:",         f'{float(discounted_total):0.2f}')
        print("="*30)
        print("\nThank you and have a great day!")
    elif 7<=int(x)<=9: #checks if customer is lucky
        discounted_subtotal = Current_Total - (Current_Total*0.25)  #the next four lines calculate discounted prices
        discount= Current_Total*0.25
        discounted_tax = discounted_subtotal*.13
        discounted_total = discounted_tax + discounted_subtotal
        print("Congratulations! You are a truly a lucky customer and have been qualified for a discount of 10%")    #the final print statement
        print("\nHere is your final receipt!")
        print("="*45)
        print("1.",item1_name,"x",total_item1_bought,   total_item1_price) 
        print("2.",item2_name,"x",total_item2_bought,   total_item2_price)   
        print("3.",item3_name,"x",total_item3_bought,   total_item3_price)
        print("-"*30)
        print("Subtotal (old):",           f'{float(Current_Total):0.2f}')
        print("Subtotal (new):",           f'{float(discounted_subtotal):0.2f}')
        print("Discount:",           f'{float(discount):0.2f}')
        print("Tax:",           f'{float(discounted_tax):0.2f}')
        print("-"*30)
        print("Total:",         f'{float(discounted_total):0.2f}')
        print("="*30)
        print("\nThank you and have a great day!")
    elif int(x)==10: #checks if customer is lucky
        discounted_subtotal = Current_Total - (Current_Total*0.5)   #the next four lines calculate discounted prices
        discount= Current_Total*0.5
        discounted_tax = discounted_subtotal*.13
        discounted_total = discounted_tax + discounted_subtotal
        print("Congratulations! You are a truly a lucky customer and have been qualified for a discount of 10%")    #the final print statement
        print("\nHere is your final receipt!")
        print("="*45)
        print("1.",item1_name,"x",total_item1_bought,   total_item1_price) 
        print("2.",item2_name,"x",total_item2_bought,   total_item2_price)   
        print("3.",item3_name,"x",total_item3_bought,   total_item3_price)
        print("-"*30)
        print("Subtotal (old):",           f'{float(Current_Total):0.2f}')
        print("Subtotal (new):",           f'{float(discounted_subtotal):0.2f}')
        print("Discount:",           f'{float(discount):0.2f}')
        print("Tax:",           f'{float(discounted_tax):0.2f}')
        print("-"*30)
        print("Total:",         f'{float(discounted_total):0.2f}')
        print("="*30)
        print("\nThank you and have a great day!")



