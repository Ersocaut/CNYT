import unittest
from Complex import *

class Test(unittest.TestCase):
    def testSuma(self):
        a,b = [5,5],[5,6]
        c,d = [1,10],[5,8]
        self.assertEqual(suma(a,b),[10,11])
        self.assertEqual(suma(c,d),[6,18])

    def testMult(self):
        a,b = [5,5],[5,6]
        c,d = [1,10],[5,8]
        self.assertEqual(producto(a,b),[-5,55])
        self.assertEqual(producto(c,d),[-75,58])

    def testResta(self):
        a,b = [5,5],[5,6]
        c,d = [1,10],[5,8]
        self.assertEqual(resta(a,b),[0,-1])
        self.assertEqual(resta(c,d),[-4,2])

    def testDiv(self):
        a,b = [8,9],[2,1]
        c,d = [3,2],[-1,2]
        self.assertEqual(division(a,b),[5,2 ])
        self.assertEqual(division(c,d),[0.2,-1.6])

    def testMod(self):
        a = [5,5]
        c = [1,10]
        self.assertEqual(modulo(a),7.0710678118654755)
        self.assertEqual(modulo(c),10.04987562112089)

    def testConjugado(self):
        a = [5,5]
        c = [1,10]
        self.assertEqual(conjugado(a),[5,-5])
        self.assertEqual(conjugado(c),[1,-10])

    def testPolarACartesiano(self):
        a = [8.48528137423857, 0.7853981633974483]
        b = [11.180339887498949, 1.1071487177940904]
        self.assertEqual(polarACartesiano(a),[6,5.999999999999999])
        self.assertEqual(polarACartesiano(b),[5.000000000000002,10])
        
    
    def testCartesianoAPolar(self):
        a = [6,6]
        b = [5,10]
        self.assertEqual(cartesianoAPolar(a),([8.48528137423857, 0.7853981633974483]))
        self.assertEqual(cartesianoAPolar(b),[11.180339887498949, 1.1071487177940904])

        
if __name__ == "__main__":
    unittest.main()
