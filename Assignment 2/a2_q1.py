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



