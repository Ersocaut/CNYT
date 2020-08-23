import unittest
from ComplexVector import *
a,b = [1,3],[2,4]
c,d = [6,5],[4,9]
class Test(unittest.TestCase):

    def testSuma(self):
        self.assertEqual(sumaVectores([a,b],[a,b]),[[2,6],[4,8]])
        self.assertEqual(sumaVectores([a,c],[c,b]),[[7,8],[8,9]])

    def testVectorInverso(self):
        self.assertEqual(vectorInverso([a,c]),[[-1,-3],[-6,-5]])
        self.assertEqual(vectorInverso([b,a]),[[-2,-4],[-1,-3]])

    def testEscalVect(self):
        self.assertEqual(escalarPorVector(b,[a,b]),[[-10,10],[-12,16]])
        self.assertEqual(escalarPorVector(c,[b,c]),[[-8,34],[11,60]])

    def testSumaMatriz(self):
        self.assertEqual(sumaMatrices([[a,a],[b,b]],[[b,a],[a,b]]),[[[3,7],[2,6]],[[3,7],[4,8]]])
        self.assertEqual(sumaMatrices([[c,a],[a,b]],[[b,c],[b,b]]),[[[8,9],[7,8]],[[3,7],[4,8]]])

    def testInversaMatriz(self):
        self.assertEqual(matrizInversa([[a],[b],[c]]),[[[-1,-3]],[[-2,-4]],[[-6,-5]]])
        self.assertEqual(matrizInversa([[a,a,c],[c,b,a],[d,c,b]]),[[[-1,-3],[-1,-3],[-6,-5]],[[-6,-5],[-2,-4],[-1,-3]],[[-4,-9],[-6,-5],[-2,-4]]])

    def testEscalMatriz(self):
        self.assertEqual(escalarPorMatriz(d,[[c,a],[a,d]]),[[[-21,74],[-23,21]],[[-23,21],[-65,72]]])
        self.assertEqual(escalarPorMatriz(c,[[a,a],[b,b]]),[[[-9,23],[-9,23]],[[-8,34],[-8,34]]])

    def testTranspuesta(self):
        self.assertEqual(transpuesta([[b,a,a],[a,b,a]]),[[[2,4],[1,3]],[[1,3],[2,4]],[[1,3],[1,3]]])

    def testMatrizConjugada(self):
        self.assertEqual(matrizConjugada([[b,a,c],[c,b,d]]),[[[2,-4],[1,-3],[6,-5]],[[6,-5],[2,-4],[4,-9]]])

    def testMatrizAdjunta(self):
        self.assertEqual(matrizAdjunta([[b,a,a],[a,b,a]]),[[[2, -4], [1, -3]], [[1, -3], [2, -4]], [[1, -3], [1, -3]]])
    def testMultiplicaMatrices(self):
        self.assertEqual(productoMatrices([[a,a],[b,b]],[[b,a],[a,b]]),[[[-18,16],[-18,16]],[[-22,26],[-22,26]]])
    def testAccion(self):
        a,b,c,d,e = [1,4],[4,0],[7,-1],[0,1],[5,6]
        self.assertEqual(accion([[a,c,d],[b,c,d],[d,b,e]],[e,d,c]),[[-17,40],[49,27],[35,46]])
if __name__ == "__main__":
    unittest.main()
