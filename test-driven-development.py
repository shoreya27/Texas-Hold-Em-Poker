'''
TDD stands for test driven code which actually means that before writing any code , write test cases for that code
Usefull because it will let you know what should it do , whats shoulb I expect from given arguments
This Test driven dev approach is in best practice to develop any software
'''
#eg I will write a test case for my product function which I want to create
import unittest

def product(a, b):
    return a*b

class TestProduct(unittest.TestCase):
    def test_multiplication_of_two_numbers(self):
        self.assertEqual(product(3,5), 
                        15
                        )

unittest.main()
#NameError: name 'product' is not defined
#1>now I know that I have to define a product method
#roduct() takes 0 positional arguments but 2 were given
#Now i know that my product() metho takes in 2 arggumnet

#each error is a progress , as it tells me that my code is not working as expected
#
#AssertionError: None != 15
#I know that my function is not returning anything , so retrn the value

#Now it ran successfully now!!