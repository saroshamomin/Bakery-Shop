#Author: Sarosha Momin
#Homework Number & Name: Inventory Management Final Project
#Due Date: December 10
#Program Description: Write a program to store and manage existing inventory, and allow customers to purchase or return bakery supplies.
# This file includes the transaction item class to store information about user transaction

class TransactionItem():
    def __init__(self):
        self.__id = 244
        self.__name = "Large Cake Pan"
        self.__quantity = 7
        self.__price = 19.99
    
    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        self.__id = new_id
        
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name 

    def get_qty(self):
        return self.__quantity
    
    def set_qty(self, new_qty):
        self.__quantity = new_qty
        
    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        self.__price = new_price 
    
    def calc_cost(self):
        return float(self.__price) * int(self.__quantity)
    
    def __str__(self):
        i_d = str(self.__id)
        name = self.__name
        qty = str(self.__quantity)
        price = str(self.__price)
        string = i_d.rjust(0, " ") + name.rjust(23, " ") + qty.rjust(12, " ") + "          $" + price.rjust(8, " ") 
        return string
