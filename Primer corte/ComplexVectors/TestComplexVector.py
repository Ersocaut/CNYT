import unittest
from ComplexVector import *

class Test(unittest.TestCase):
    def testProductoInterno(self):
        a,b = [[1,0],[0,1],[1,-3]],[[2,1],[0,1],[2,0]]
        self.assertEqual(productoInterno(a,b),[5,7])

    def testNorma(self):
        v = [[6.5,2.7],[3.1,-3.8]]
        w = [[4.5,5.5],[2.7,-7.4]]
        self.assertEqual(float("%.2f" %norma(v)),5.49)
        self.assertEqual(float("%.2f" %norma(w)),7.58)

##    def testAccion(self):
##        a = [[[0,0],[0,2]],[[0,-2],[0,0]]]
##        b = [[0,1],[1,0]]
##        self.assertEqual(accion(a,b),-2)
if __name__ == "__main__":
    unittest.main()
