from abc import ABC, abstractmethod
from tokenize import String
from typing import Dict

from shopping_cart_interface import IShoppingCart
from pricer import Pricer


class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer):
        self.pricer = pricer
        self._contents: Dict[str,int] = {}

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        if item_type not in self._contents:
            self._contents[item_type] = number
    
        else:
            self._contents[item_type] = self._contents[item_type] + number

    #helper function to return total price without print statements   
    def calculations(self):
        total = 0
        for key, number in self._contents.items():
            price = self.pricer.get_price(key)
            p = number*price  
            total = total + p
        
        return total  
       
    #prompt the customer to enter how much they will pay
    def Pay_Amount(self):
        total = ShoppingCart.calculations(self)
        print("Total amount due:", total)
        while True:
          paid = int(input("\nPlease enter an amount to pay:"))
          if paid < total:
            print("\nMust be greater than total amount")
          else:
            #change = paid - total 
            return paid

    #prompt the user to enter there payment method  
    def Pay_method(self):
      while True:
        method = int(input("\nHow would you like to pay: Please enter 1 for cash or 2 for card: "))
        if method == 1:
           return 1
        elif method == 2:
           return 2
        else: 
           print("\nPlease enter a correct payment method")

    
    def print_receipt(self,method,paid):
        if method == 1:
           methoddd = 'cash'
        else:
           methoddd = 'card'
        total = 0
        for key, number in self._contents.items():
            price = self.pricer.get_price(key)
            p = number*price #e.g p = price of 5 bananas, price = 1 banana 
            total = total + p
            print(f"{key} - {number} @ {price} - {p}") 
        print("Total:", total)
        if methoddd == 'card':
            print(f"Paid by card")
        else:
            print(f"Paid by {methoddd}  {paid}")
        print("Change:", paid - total)
   
    
    #function printing with price first which I have not included in the testing but is here to check
    def print_receipt_1(self):
        total = 0
        for key, number in self._contents.items():
            price = self.pricer.get_price(key)
            p = number*price #e.g p = price of 5 bananas, price = 1 banana 
            total = total + p
            print(f"{p} - {key} - {number}")
        print("Total:", total)

    
    
      
    
    

class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """
    @abstractmethod
    def factory_method(self) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method()

class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """
    def factory_method(self) -> ShoppingCart:
        # returns ShoppingCart object
        return ShoppingCart(Pricer())
