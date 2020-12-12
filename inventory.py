#Author: Sarosha Momin
#Homework Number & Name: Inventory Management Final Project
#Due Date: December 10
#Program Description: Write a program to store and manage existing inventory, and allow customers to purchase or return bakery supplies.
# This file includes the inventory class to store information about the inventory and update it


class Inventory():
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
 
    def get_stock(self):
        return self.__stock
    
    def get_price(self):
        return self.__price
    
    def restock(self, new_stock):
        if int(new_stock) < 0:
            self.__stock -= int(new_stock)
            return True
        else:
            return False
        
    def purchase(self, purch_qty):
        if self.__stock >= int(purch_qty):
            purch_qty = int(purch_qty)
            self.__stock -= purch_qty
            return True
        else:
            return False
        
    def __str__(self):
        i_d = str(self.__id)
        name = self.__name
        stock = str(int(self.__stock))
        price = str(self.__price)
        string = i_d.rjust(0, " ") + name.rjust(23, " ") + "    $" + price.rjust(9, " ") + stock.rjust(23, " ")
        return string

