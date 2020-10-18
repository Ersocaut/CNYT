import unittest
from QuantumTheory import *

sx = [[0, 1],
      [1, 0]]

sy = [[0, -1j],
      [1j, 0]]

sz = [[1, 0],
      [0, -1]]


def mostrarRespuesta4_3_1(observable):
    """PRE: ingresa uno de los  tres spin operators
       POST: retorna los posibles estados que el spin puede transitar despues de ser observado"""

    x, v = EigenValues(observable)
    answ = []
    for el in v:
        current = translateEightnVector(el)
        answ.append(current)
    return answ


def mostrarRespuesta4_3_2(observable):
    """PRE: ingresa uno de los  tres spin operators
       POST: retorna la media de la distribucion del spin ingresado"""

    shi = [[1, 0], [0, 0]]
    x, v = EigenValues(observable)

    meanValueDistribution = [0, 0]
    for i in range(len(x)):
        eigenValue = translateValues(x[i])
        eigenVector = translateEightnVector(v[:, i])

        prob = multComplexNumber(eigenValue, [Length([transicion(eigenVector, shi)]) ** 2, 0])

        meanValueDistribution = suma(meanValueDistribution, prob)
    return meanValueDistribution


class observableTest(unittest.TestCase):

    def testExercice4_3_1(self):
        # exercice4.4.1 of Quantum Computing for Computer Sci, para el ejericio solo se pedia para Sx , pero para nosotros era para los 3 spin operators

        self.assertEqual(mostrarRespuesta4_3_1(sx), [[[0.7071067811865475, 0.0], [-0.7071067811865475, 0.0]],
                                                     [[0.7071067811865475, 0.0], [0.7071067811865475, 0.0]]])
        self.assertEqual(mostrarRespuesta4_3_1(sy), [[[-0.0, -0.7071067811865474], [0.7071067811865475, 0.0]],
                                                     [[0.7071067811865476, 0.0], [0.0, -0.7071067811865475]]])
        self.assertEqual(mostrarRespuesta4_3_1(sz), [[[1.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [1.0, 0.0]]])

    def testExercice4_3_2(self):
        ## el estado inicial para el ejercicio 4.3.2 es UP luego shi = [1,0]
        self.assertEqual(mostrarRespuesta4_3_2(sx), [0.0, 0.0])
        self.assertEqual(mostrarRespuesta4_3_2(sy), [-2.7755575615628914e-16, 0.0])
        self.assertEqual(mostrarRespuesta4_3_2(sz), [1.0, 0.0])

    def testExercice4_4_1(self):
        raiz = math.sqrt(2) / 2
        u1 = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
        u2 = [[[raiz, 0], [raiz, 0]], [[raiz, 0], [-raiz, 0]]]

        self.assertEqual(isUnitary(u1), True)
        self.assertEqual(isUnitary(u2), True)

        self.assertEqual(isUnitary(multiplicaMat(u1, u2)), True)
        self.assertEqual(isUnitary(multiplicaMat(u1, u2)), True)

    def testExercice4_4_2(self):
        raiz = 1 / math.sqrt(2)
        vectIni = [[1, 0], [0, 0], [0, 0], [0, 0]]
        matrix = [[[0, 0], [raiz, 0], [raiz, 0], [0, 0]],
                  [[0, raiz], [0, 0], [0, 0], [raiz, 0]],
                  [[raiz, 0], [0, 0], [0, 0], [0, raiz]],
                  [[0, 0], [raiz, 0], [-raiz, 0], [0, 0]]]
        self.assertEqual(quantumProbabilisticSystem(matrix, vectIni, 3),
                         [[0.4999999999999996, 0.0, 0.0, 0.4999999999999996],
                          [0.0, 0.4999999999999996, 0.4999999999999996, 0.0],
                          [0.0, 0.4999999999999996, 0.4999999999999996, 0.0],
                          [0.4999999999999996, 0.0, 0.0, 0.4999999999999996]])


if __name__ == '__main__':
    unittest.main()