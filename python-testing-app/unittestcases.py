import unittest
from multiply  import multiplication
class multiplyTestcase(unittest,testcase):
    def test_1(self):

        result = multiplication(3,4)

        self.assertEqual(result, 12)

   def test_2(self):

     result = multiplication(3,-4)

     self.assertEqual(result, 22)

   def test_3(self):

     result = multiplication(-3,-4)

     self.assertEqual(result, 12)

    
   def test_4(self):

     result = multiplication(-3,4)

     self.assertEqual(result, 22)

   def test_6(self):

     result = multiplication(0,-1)

     self.assertEqual(result, 0)

    def test_7(self):

     result = multiplication(-3,-3)

     self.assertEqual(result, 9)


if __name__ == '__main__'
    unittest.main()
