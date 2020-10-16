from ClassicToQuantum import *
import numpy as np
from numpy import linalg as Alg

def dosDecimales(num, decimal):
    num = "{:.2f}".format(num)
    num = (num[:-1] if decimal else num)
    return float(num)

def Long(vec):
    acum = 0
    for i in range(len(vec)):
        acum += (modulo(vec[i]))**2
    return acum**(1/2)

def normalizar(vec):
    long = Long(vec)
    for i in range(len(vec)):
        vec[i] = [vec[i][0]/long,vec[i][1]/long]
    return vec

def bra(vec):
    return vectorAdjunto(vec)

def transicion(vec1, vec2):
    return productoInterno(vec1, vec2)

def probabilidad(vec, pos):
    long = Long(vec)
    if (0 <= pos < len(vec)):
        return dosDecimales(modulo(vec[pos])**2/long**2, False)
    else:
        return 0

def OmegaPsi(psi, omega):
    return productoInterno(accion(omega, psi), psi)[0]

def DeltaPsi(omega, esperado):
    return restaMatrices(omega, escalarPorMatriz(esperado, Identity(omega)))

def matrizPsi(mat, psi):
    vec = accion(mat, vectorAdjunto(psi))
    return dosDecimales(productoVectores(vec, vectorAdjunto(psi))[0],False)

def varianza(psi, omega):
    esperado = dosDecimales(OmegaPsi(psi, omega), True)
    deltaPsi = DeltaPsi(omega, [esperado, 0.0])
    matrizVarianza = productoMatrices(deltaPsi, deltaPsi)
    return matrizPsi(matrizVarianza, psi)

def describeObservable(psi, mat):
    if (isHermitian(mat)):
        me = dosDecimales(OmegaPsi(psi, mat), True)
        return [varianza(psi, mat), me]
    return None

def traduce(mat):
    new = [0,0]
    for i in range(len(mat)):
        act = []
        for j in range(len(mat[0])):
            actV = mat[i][j]
            act.append([actV.real, actV.imag])
        new.append(act)
    return new

def Eigen(omega):
    obs = np.array(omega)
    (values, vec) = Alg.eig(obs)
    return [[values[i].real, values[i].imag]for i in range(len(values))], traduce(vec)