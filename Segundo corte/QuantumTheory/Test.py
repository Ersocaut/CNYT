import unittest
from QuantumTheory import *

class Test(unittest.TestCase):
    def testLong(self):
        test = [[2, -3], [1, 2]]
        self.assertEqual(float("{0:.4f}".format(Long(test))), 4.2426)

    def testNormalizar(self):
        vec = [[2, 1], [-1, 2], [0, 1], [1, 0], [3, -1], [2, 0], [0, -2], [-2, 1], [1, -3], [0, -1]]

        self.assertEqual(normalizar(vec), [[0.2948839123097942, 0.1474419561548971],
                                              [-0.1474419561548971, 0.2948839123097942],
                                              [0.0, 0.1474419561548971],
                                              [0.1474419561548971, 0.0],
                                              [0.44232586846469135, -0.1474419561548971],
                                              [0.2948839123097942, 0.0],
                                              [0.0, -0.2948839123097942],
                                              [-0.2948839123097942, 0.1474419561548971],
                                              [0.1474419561548971, -0.44232586846469135],
                                              [0.0, -0.1474419561548971]])

    def testBra(self):
        vec = [[2, 1], [-1, 2], [0, 1], [1, 0], [3, -1], [2, 0], [0, -2], [-2, 1], [1, -3], [0, -1]]
        adjointVec = [[2, -1], [-1, -2], [0, -1], [1, 0], [3, 1], [2, 0], [0, 2], [-2, -1], [1, 3], [0, 1]]

        self.assertEqual(adjointVec, vectorAdjunto(vec))


    def testTransicion(self):
        vec1 = normalizar([[2, 1], [-1, 2], [0, 1], [1, 0], [3, -1], [2, 0], [0, -2], [-2, 1], [1, -3], [0, -1]])
        vec2 = normalizar([[-1, -4], [2, -3], [-7, 6], [-1, 1], [-5, -3], [5, 0], [5, 8], [4, -4], [8, -7], [2, -7]])
        self.assertEqual([-0.02055662641731377, -0.13019196730965366], transicion(vec2, vec1))

    def testProbabilidad(self):
        prob = [[-3, -1], [0, -2], [0, 1], [2, 0]]
        self.assertEqual(probabilidad(prob, 2), 0.05)

    def testVarianza(self):
        psi = normalizar([[(2**(1/2))/2, 0], [0, (2**(1/2))/2]])
        omega = [[[1, 0], [0, -1]], [[0, 1], [2, 0]]]
        self.assertEqual(varianza(psi, omega), 4.25)

    def testDescribirObservable(self):
        raiz = (2**(1/2)) / 2;
        psi = normalizar([[raiz, 0], [0, raiz]]);
        omega = [[[1, 0], [0, -1]], [[0, 1], [2, 0]]];
        answ = describeObservable(psi, omega)
        self.assertEqual(answ[0], 4.25);
        self.assertEqual(answ[1], 2.5);
        self.assertEqual(describeObservable(psi, [[[1, -1], [1, -1]], [[1, -1], [1, -1]]]), None);

if __name__ == '__main__':
    unittest.main()