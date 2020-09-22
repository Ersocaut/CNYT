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
        A,V = [[[0,0],[0,-2]],[[0,2],[0,0]]],[[0,1],[1,0]]
        self.assertEqual(accion([[a,c,d],[b,c,b],[d,b,e]],[e,d,c]),[[-17,40],[49,27],[35,46]])

    def testNorma(self):
        a,b = [3,0],[-6,0]
        c = [2,0]
        N = [[6.5,2.7],[3.1,-3.8]]
        self.assertEqual(norma([a,b,c]),(49)**(1/2))
        self.assertEqual(norma(N),5.489080068645383)

    def testProductoInterno(self):
        a,b = [3,0],[-6,0]
        c = [2,0]
        self.assertEqual(productoInterno([a,b,c],[a,b,c]),[49,0])

    def testDistancia(self):
        a,b = [3,0],[1,0]
        c,d = [2,0],[-1,0]
        self.assertEqual(distancia([a,b,c],[c,c,d]),11**(1/2))

    def testIsUnitary(self):
        a,b = [1,0],[0,0]
        c = [0,1]
        self.assertTrue(isUnitary([[c,b],[b,c]]))
        self.assertTrue(isUnitary([[a,b],[b,a]]))
        self.assertFalse(isUnitary([[a,d],[b,a]]))

    def testHermitian(self):
        a,b = [7,0],[6,5]
        c,d = [6,-5],[-3,0]
        e,f = [1,0],[0,0]
        self.assertTrue(isHermitian([[a,b],[c,d]]))
        self.assertFalse(isHermitian([[f,f],[e,e]]))

    def testTensor(self):
        A = [[[1, 0], [2, 0]], [[0, 0], [1, 0]]]
        B = [[[3, 0], [2, 0]], [[-1, 0], [0, 0]]]
        C = [[[6, 0], [5, 0]], [[3, 0], [2, 0]]]

        aXb = tensor(A, B)
        bXc = tensor(B, C)

        self.assertEqual(tensor(A, bXc),
                         [[[18, 0], [15, 0], [12, 0], [10, 0], [36, 0], [30, 0], [24, 0], [20, 0]],
                          [[9, 0], [6, 0], [6, 0], [4, 0], [18, 0], [12, 0], [12, 0], [8, 0]],
                          [[-6, 0], [-5, 0], [0, 0], [0, 0], [-12, 0], [-10, 0], [0, 0], [0, 0]],
                          [[-3, 0], [-2, 0], [0, 0], [0, 0], [-6, 0], [-4, 0], [0, 0], [0, 0]],
                          [[0, 0], [0, 0], [0, 0], [0, 0], [18, 0], [15, 0], [12, 0], [10, 0]],
                          [[0, 0], [0, 0], [0, 0], [0, 0], [9, 0], [6, 0], [6, 0], [4, 0]],
                          [[0, 0], [0, 0], [0, 0], [0, 0], [-6, 0], [-5, 0], [0, 0], [0, 0]],
                          [[0, 0], [0, 0], [0, 0], [0, 0], [-3, 0], [-2, 0], [0, 0], [0, 0]]])


if __name__ == "__main__":
    unittest.main()
