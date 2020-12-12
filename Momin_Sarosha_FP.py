#Author: Sarosha Momin
#Homework Number & Name: Inventory Management Final Project
#Due Date: December 10
#Program Description: Write a program to store and manage existing inventory, and allow customers to purchase or return bakery supplies.

import inventory, transactionitem

def main():
    # create lists to store the data from txt.file 
    inventory_list = []
    transaction_list = []
    id_list = []
    name_list = []
    stock_list = []
    price_list =[]
    
    createinventory(id_list, name_list, stock_list, price_list, inventory_list)  #creates instances of Inventory class
    print_menu(inventory_list) # prints the inventory information
    
    # create a loop for the user transaction
    cont = True
    while cont:
        purch_id = get_id()
        if int(purch_id) == 0:        # let's the user exit 
            cont = False
        elif purch_id in id_list:
            x = id_list.index(purch_id)
            qty = input("How many items would you like to purchase? Enter negative number for returns. ")
            while int(qty) == 0:      # loop until valid quantity entered
                print("That is not a valid quantity. Please try again. ")
                qty = input("How many items would you like to purchase? Enter negative number for returns. ")
            if int(qty) > 0:     # if purchasing, updates the inventory and creates a transaction object with info
                if inventory_list[x].purchase(qty) == True:
                    trans_obj = transactionitem.TransactionItem()
                    trans_obj.set_id(purch_id)
                    trans_obj.set_name(inventory_list[x].get_name())
                    trans_obj.set_qty(qty)
                    trans_obj.set_price(inventory_list[x].get_price())
                    transaction_list.append(trans_obj)
                    print_menu(inventory_list)
                else:
                    print("There is not enough inventory to purchase this amount. Please try again. ")
            elif int(qty) < 0:       # if returning, updates the inventory to restock and creates a transaction object with info
                inventory_list[x].restock(qty)
                trans_obj = transactionitem.TransactionItem()
                trans_obj.set_id(purch_id)
                trans_obj.set_name(inventory_list[x].get_name())
                trans_obj.set_qty(qty)
                trans_obj.set_price(inventory_list[x].get_price())
                transaction_list.append(trans_obj)
                print_menu(inventory_list)
        else:
            print("Invalid product ID. Please try again. ")
    if not transaction_list:  # if the user returns or purchases nothing
        print("Thanks for visiting our store! ")
    else: 
        print_invoice(transaction_list) 
    update_file(inventory_list)

# method to read through the inventory.txt file 
def createinventory(id_list, name_list, stock_list, price_list, inventory_list):
    inventory_file = open("Inventory.txt", "r")
    prod_id = inventory_file.readline().rstrip("\n")
    while prod_id != '':
        id_list.append(prod_id)     # make lists for each attribute of the item
        name_list.append(str(inventory_file.readline().rstrip('\n')))
        stock_list.append(float(inventory_file.readline().rstrip('\n')))
        price_list.append(float(inventory_file.readline().rstrip('\n'))) 
        prod_id = inventory_file.readline().rstrip('\n')
    inventory_file.close()
    
    # create a list of objects of the inventory class using the lists with the attributes above
    for x in range(len(id_list)):
        product = inventory.Inventory(id_list[x], name_list[x], stock_list[x], price_list[x])
        inventory_list.append(product)

# prints a menu with all attributes of each object in the inventory class
def print_menu(inventory_list):
    print("\nID:                  Name:        Price:     Quantity Available: ")
    for x in range(len(inventory_list)):
        print(inventory_list[x])

# get the id from user
def get_id():
        purch_id = input("Which product ID would you like to purchase? Enter 0 to exit. ")
        return purch_id

# print the invoice of the transaction    
def print_invoice(transaction_list):
    subtotal = 0
    items = 0
    print("\nOrder complete. See invoice below: ")
    print("ID:                  Name:    Quantity:            Price:       Total Price: ")
    
    # calculate the total cost, total items, tax and subtotal of the transaction 
    # loop through the list of transaction objects to get attrbute information
    for x in range(len(transaction_list)):
        cost = transaction_list[x].calc_cost()
        items += int(transaction_list[x].get_qty())
        print(transaction_list[x], end = '')
        print("        $   ", format(cost, '.2f'))
        subtotal += cost
    tax = subtotal * .085
    total = tax + subtotal
    print("\nTotal Items: ", items)          #print out the information calculated 
    print("Subtotal: $", format(subtotal, '.2f'), sep = '')
    print("Sales Tax: $", format(tax, '.2f'), sep = '')
    print("Grand Total: $", format(total, '.2f'), sep = '')

# use the inventory list to create a new updated file of the inventory    
def update_file(inventory_list):
    update_file = open("UpdatedInventory.txt", 'w')
    for x in range(len(inventory_list)):
        update_file.write(str(inventory_list[x].get_id()) + '\n') 
        update_file.write(str(inventory_list[x].get_name())  + '\n')
        update_file.write(str(inventory_list[x].get_stock())  + '\n')
        update_file.write(str(inventory_list[x].get_price())  + '\n') 
    update_file.close()
    
main()

            
        
            
            
            