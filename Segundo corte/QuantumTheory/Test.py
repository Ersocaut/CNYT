import unittest
from QuantumTheory import *

class Test(unittest.TestCase):
    def testLong(self):
        test = [[2, -3], [1, 2]]
        self.assertEqual(float("{0:.4f}".format(Long(test))), 4.2426)
    
if __name__ == '__main__':
    unittest.main()