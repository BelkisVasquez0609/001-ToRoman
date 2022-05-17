import unittest
import main

#Test case of range
class MyTestCaseRange(unittest.TestCase):
    def test01(self):
        self.assertEqual("The number entered is out of range", main.Validator("6000"))  # add assertion here

    def test02(self):
        self.assertEqual("The Result is valid", main.Validator("600"))  # add assertion here

    def test03(self):
        self.assertEqual("The Result is valid", main.Validator("60.4"))  # add assertion here
#Test case to validate the test
class MyTestCaseText(unittest.TestCase):
    def test04(self):
        self.assertEqual("Invalid Input", main.Validator("Hello, My Name Is Yazmin"))  # add assertion here

    def test05(self):
        self.assertEqual("The Result is valid", main.Validator("33.0"))  # add assertion here

# Test case to validate empty entry
class MyTestCaseEmpty(unittest.TestCase):
    def test06(self):
        self.assertEqual("You must fill in the field to perform the conversion", main.Validator(""))  # add assertion here

# Test case to validate the entry of the method convertions
class MyTestCaseConvertions(unittest.TestCase):
    def test07(self):
        self.assertEqual("Invalid Entry", main.Convertions("65"))  # add assertion here

    def test08(self):
        self.assertEqual("You must fill in the field to perform the conversion", main.Convertions(""))  # add assertion here
    def test09(self):
        self.assertEqual("Valid Entry", main.Convertions("S"))  # add assertion here

#Method Main
if __name__ == '__main__':
    unittest.main()
