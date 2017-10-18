#!/usr/local/bin/python3
'''
    * Author: Taha Magdy
    * Date: 18th Oct, 2017


    * Task3
    =======
    * testing...
'''
import unittest
from lib import mystack


class TestMyStack(unittest.TestCase):

    def setUp(self):
        mystack.add_item(10)
        mystack.add_item(20)
        mystack.add_item(22, 33)

    def test_flow(self):
        print(self.assertEqual(mystack.pop_item(), 33))
        print(self.assertEqual(mystack.pop_item(), 22))
        print(self.assertEqual(mystack.count_items(), 2))
        while mystack.pop_item(): pass
        print(self.assertEqual(mystack.count_items(), 0))

    def assertEqual(self, num1, num2):
        return num1 == num2


test = TestMyStack()
test.setUp()
test.test_flow()
