import os
import unittest

# testSuite = unittest.TestSuite()

testcase = unittest.TestLoader().discover(start_dir='../ShopTest/', pattern="Test*.py")

unittest.TextTestRunner().run(testcase)