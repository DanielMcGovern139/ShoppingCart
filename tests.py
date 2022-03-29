#from typing_extensions import Self
from pyexpat import model
import unittest
from wsgiref.validate import validator

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing

class ShoppingCartTest(unittest.TestCase):

    #validator function to assist with testing 
    def validator( item_type: str, number: int, price: int, lists1 = [], lists2 = [], lists3 = [], lists4 = []):
        lists1.append(item_type)  
        lists2.append(number)
        lists3.append(price)
        lists4.append(number*price) 


    
    def test_print_receipt(self):
        sc = ShoppingCartConcreteCreator().operation()
        lists1 = []
        lists2 = []
        lists3 = []
        lists4 = []
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        sc.add_item("apple", 2)
        sc.add_item("fruit", 2)
        sc.add_item("carrot", 2)
        sc.add_item("Choco", 3)

        ShoppingCartTest.validator("banana", 5, 200, lists1, lists2, lists3, lists4)
        ShoppingCartTest.validator("pear", 5, 200, lists1, lists2, lists3, lists4)
        ShoppingCartTest.validator("apple", 2, 100, lists1, lists2, lists3, lists4)
        ShoppingCartTest.validator("fruit", 2, 100, lists1, lists2, lists3, lists4)
        ShoppingCartTest.validator("carrot", 2, 300, lists1, lists2, lists3, lists4)
        
        paid = sc.Pay_Amount()
        method = sc.Pay_method()
        total = sc.calculations()
        change = paid - total
        if method == 1:
           methoddd = 'cash'
        else:
           methoddd = 'card'
        print("Your receipt is as follows:")
        
        with Capturing() as output:
            sc.print_receipt(method,paid)
        print(output)
        
        i = 0
        for i in range(4):
            self.assertEqual(f"{lists1[i]} - {lists2[i]} @ {lists3[i]} - {lists4[i]}", output[i])
        
        self.assertEqual(f"Total: {total}", output[6])
        if methoddd == 'cash':
         self.assertEqual(f"Paid by cash  {paid}", output[7])
        else:
         self.assertEqual("Paid by card", output[7])
        self.assertEqual(f"Change: {change}", output[8])

   
    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        #lists1 = []
        #lists2 = []
        #lists3 = []
        #lists4 = []
        #sc.add_item("banana", 5)
        #sc.add_item("pear", 5)
        
        #ShoppingCartTest.validator("banana", 5, 200)
        #ShoppingCartTest.validator("pear", 5, 200)
        
        #paid = sc.Pay_Amount()
        #method = sc.Pay_method()
        #total = sc.calculations()
        #change = paid - total
        #if method == 1:
         #  methoddd = 'cash'
        #else:
         #  methoddd = 'card'
        #print("Your receipt is as follows:")
        
       # with Capturing() as output:
          #  sc.print_receipt(method,paid)
       # print(output)
        
       # i = 0
       # for i in range(4):
        #    self.assertEqual(f"{lists1[i]} - {lists2[i]} @ {lists3[i]} - {lists4[i]}", output[i])
        
        #self.assertEqual(f"Total: {total}", output[6])
        #if methoddd == 'cash':
         #self.assertEqual(f"Paid by cash  {paid}", output[7])
        #else:
         #self.assertEqual("Paid by card", output[7])
        #self.assertEqual(f"Change: {change}", output[8])


unittest.main(exit=False)


