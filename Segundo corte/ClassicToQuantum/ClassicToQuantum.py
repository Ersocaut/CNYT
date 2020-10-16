from ComplexVector import *
import matplotlib.pyplot as plot
import numpy as np


def sistemaProbabilistico(mat, vec, times):
    for i in range(times):
        vec = accion(mat, vec)
    return vec


def matrizFinal(mat):
    for i in range(len(mat)):
        new = []
        for j in range(len(mat[i])):
            new.append([modulo(mat[i][j]) ** 2, 0])
        mat[i] = new
    return mat


def sistemaProbabilisticoCuantico(mat, vec, times):
    cop = mat[:]
    for i in range(times):
        mat = productoMatrices(mat, cop)
    return matrizFinal(mat)


def accionBooleana(mat, vec):
    if len(vec) == len(mat[0]):
        new = [False for i in range(len(mat))]
        for i in range(len(mat)):
            And = True
            for j in range(len(mat[i])):
                And = mat[i][j] and vec[j]
                new[i] = new[i] or And
        return new


def experimento(mat, vec, times):
    for i in range(times):
        vec = accionBooleana(mat, vec)
    return vec


def multipleSlit(mat, vec, times):
    return sistemaProbabilistico(mat, vec, times)


def multipleSlitCuantico(mat, vec, times):
    return sistemaProbabilisticoCuantico(mat, vec, times)


def grafico(vec):
    data = len(vec)
    x = np.array([x for x in range(data)])
    y = np.array([round(vec[x][0] * 100, 2) for x in range(data)])

    plot.bar(x, y, color='g', align='center')
    plot.title('Probabilidades vector')
    plot.show()
