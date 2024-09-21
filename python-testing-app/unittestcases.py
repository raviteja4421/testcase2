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

   def test_5(self):

     result = multiplication(-1,-1)

     self.assertEqual(result, 1)

if __name__ == '__main__'
    unittest.main()
