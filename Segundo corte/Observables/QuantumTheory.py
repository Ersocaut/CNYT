from ClassicToQuantum import *
import numpy as np
from numpy import linalg as Alg


def onlyTwoDecimals(num, oneDecimal):
    num = "{:.2f}".format(num)
    num = (num[:-1] if oneDecimal else num)
    return float(num)


def Length(vect):
    """Calcula la longitud de un vector dado"""
    acu = 0
    for x in range(len(vect)):
        acu += (module(vect[x])) ** 2
    return math.sqrt(acu)


def normalizate(vect):
    """normaliza un vector dado """
    length = Length(vect)
    for x in range(len(vect)):
        vect[x] = [vect[x][0] / length, vect[x][1] / length]
    return vect


def bra(vect):
    """Devuelve el bra de un vector dado"""
    return adjointVector(vect)


def transicion(vect1, vect2):
    """Nos dice cuanto es la transicion de un vector a otro"""
    ##(rvs hc)  el bra a vect1
    return internalProduct(vect1, vect2)


def probability(vector, position):
    """Calcula la probabilidad de que un vector este en el estado dado( posicion )"""
    length = Length(vector)
    if (0 <= position < len(vector)):
        return onlyTwoDecimals(module(vector[position]) ** 2 / length ** 2, False);


def OmegaPsi(psi, omega):
    return internalProduct(actionMatrixOnVector(omega, psi), psi)[0]


def DeltaPsi(omega, expectedValue):
    return subMat(omega, multiEscalMat(expectedValue, identityMatrix(omega)))


def matrixPsi(matrix, psi):
    ## rvs pq al llmse 2 veces cmba
    actionMatrixOnVector(matrix, adjointVector(psi))
    vect = actionMatrixOnVector(matrix, adjointVector(psi))

    ##n dbra ser    (psi) adjoint sino psi.

    return onlyTwoDecimals(multVector(vect, adjointVector(psi))[0], False)


def variance(psi, omega):
    expectedValue = onlyTwoDecimals(OmegaPsi(psi, omega), True)
    deltaPsi = DeltaPsi(omega, [expectedValue, 0.0])
    matrixOfVariance = multiplicaMat(deltaPsi, deltaPsi)
    return matrixPsi(matrixOfVariance, psi)


def describeAnObservable(psi, matrix):
    if (isHermitan(matrix)):
        mean = onlyTwoDecimals(OmegaPsi(psi, matrix), True)

        return [variance(psi, matrix), mean]
    return None


def translateEightnVector(vector):
    """Traduce todos los valores propios de la libreria numpy a nuestra libreria"""
    answ = []
    for el in vector:
        answ.append([el.real, el.imag])
    return answ


def translateValues(val):
    """Traduce todos los valores propios de la libreria numpy a nuestra libreria"""
    return [val.real, val.imag]


def EigenValues(omega):
    # x Eigenvalor, v Eigenvector = Alg.eig(matrix), donde Alg es la libreria linalg
    observable = np.array(omega)
    x, v = np.linalg.eig(observable)

    return x, v