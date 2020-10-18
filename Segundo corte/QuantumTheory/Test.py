import unittest
from QuantumTheory import *


class quantumTheoryTest(unittest.TestCase):

    def testLength(self):
        test = [[2, -3], [1, 2]]
        self.assertEqual(float("{0:.4f}".format(Length(test))), 4.2426)

    def testNormalizate(self):
        vect1 = [[2, 1], [-1, 2], [0, 1], [1, 0], [3, -1], [2, 0], [0, -2], [-2, 1], [1, -3], [0, -1]]

        self.assertEqual(normalizate(vect1), [[0.2948839123097942, 0.1474419561548971],
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
        vect1 = [[2, 1], [-1, 2], [0, 1], [1, 0], [3, -1], [2, 0], [0, -2], [-2, 1], [1, -3], [0, -1]]
        adjointVect1 = [[2, -1], [-1, -2], [0, -1], [1, 0], [3, 1], [2, 0], [0, 2], [-2, -1], [1, 3], [0, 1]]

        self.assertEqual(adjointVect1, adjointVector(vect1))

    def testTransition(self):
        vect1 = normalizate([[2, 1], [-1, 2], [0, 1], [1, 0], [3, -1], [2, 0], [0, -2], [-2, 1], [1, -3], [0, -1]])
        vect2 = normalizate([[-1, -4], [2, -3], [-7, 6], [-1, 1], [-5, -3], [5, 0], [5, 8], [4, -4], [8, -7], [2, -7]])

        self.assertEqual([-0.02055662641731377, -0.13019196730965366], transicion(vect2, vect1))

    def testProbability(self):
        prob = [[-3, -1], [0, -2], [0, 1], [2, 0]]
        self.assertEqual(probability(prob, 2), 0.05)

    def testVariance(self):
        raiz = math.sqrt(2) / 2
        psi = normalizate([[raiz, 0], [0, raiz]])
        omega = [[[1, 0], [0, -1]], [[0, 1], [2, 0]]]
        self.assertEqual(variance(psi, omega), 0.25)

    def testDescribeAnObservable(self):
        raiz = math.sqrt(2) / 2
        psi = normalizate([[raiz, 0], [0, raiz]])
        omega = [[[1, 0], [0, -1]], [[0, 1], [2, 0]]]
        answ = describeAnObservable(psi, omega)

        self.assertEqual(answ[0], 0.25)
        self.assertEqual(answ[1], 2.5)

        self.assertEqual(describeAnObservable(psi, [[[1, -1], [1, -1]], [[1, -1], [1, -1]]]), None)



if __name__ == '__main__':
    unittest.main()