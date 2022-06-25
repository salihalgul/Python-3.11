# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 09:51:44 2022

@author: salih
"""

class Calc(object):
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def add(self):
        return self.value1 + self.value2
        
    def multiply(self):
        return self.value1 * self.value2

    def divide(self):
        return self.value1 / self.value2

    
print("Choose add(1), multiply(2), divide(3) ")
selection = input("select 1,2 or 3")
    
v1 = float(input("first value : "))
v2 = float(input("second value : "))
c1 = Calc(v1,v2)

if selection == "1":
    add_result = c1.add()
    print("Add : {}".format(add_result))
elif selection == "2":
    multiply_result = c1.multiply()
    print("Multiply : {}".format(multiply_result))
elif selection == "3":
    divide_result = c1.divide()
    print("Divide : {}".format(divide_result))    


