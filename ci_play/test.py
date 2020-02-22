import unittest

import sample

class TestMyFunc(unittest.TestCase):

    def setUp(self):
        pass

    def test_multiply_by_five_1(self):
        self.assertEqual( sample.multiply_by_five(-2), -10)
   
    def test_multiply_by_five_2(self):
        self.assertEqual( sample.multiply_by_five(7), 35)

    def test_add_five_1(self):
        self.assertEqual( sample.add_five(0), 5)
        
    def test_add_five_2(self):
        self.assertEqual( sample.add_five(-8), -3)
        
    def test_string_length_1(self):
        self.assertEqual( sample.string_length("Hello"), 5)
    
    def test_string_length_2(self):
        self.assertEqual( sample.string_length("world !"), 7)               

if __name__ == '__main__':
    unittest.main()
