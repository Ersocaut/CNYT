from Complex import *

def sumaVectores(vec1,vec2):
    """
        Param vec1: Primer vector a operar
        Param vec2: Segundo vector a operar
        Return: Vector resultante
    """
    if (len(vec1) == len(vec2)):
        for i in range(len(vec1)):
            vec1[i] = suma(vec1[i],vec2[i])
        return vec1

def restaVectores(vec1,vec2):
    """
        Param vec1: Primer vector a operar
        Param vec2: Segundo vector a operar
        Return: Vector resultante
    """
    if (len(vec1) == len(vec2)):
        for i in range(len(vec1)):
            vec1[i] = resta(vec1[i],vec2[i])
        return vec1

def vectorInverso(vec):
    """
        Param vec1: Vector a operar
        Return: Vector Inverso
    """
    for i in range(len(vec)):
        act = vec[i]
        vec[i] = conjugado(act)
        vec[i][0] = - act[0]
    return vec

def EscalarPorVector(esc,vec):
    """
        Param esc: (int,float) Escalar a operar 
        Param vec: Vector a operar
        Return: Vector resultante
    """
    mul = [esc,0]
    res = vec[::]
    for i in res:
        for j in i:
            j = producto(mul,j)
    return res

def sumaMatrices(mat1,mat2):
    """
        Param mat1: Primera matriz a operar
        Param mat2: Segundo vector a operar
        Return: Matriz resultante
    """
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat[i][j] = suma(mat1[i][j],mat2[i][j])
    return mat1

def matrizInversa(mat):
    """
        Param mat: Matriz a operar
        Return: Matriz resultante
    """
    for i in range(len(mat)):
        mat[i] = vectorInverso(mat[i])
    return mat

def escalarPorMatriz(esc,mat):
    """
        Param esc: (int,float) Escalar a operar
        Param mat: Matriz a operar
        Return: Matriz resultante
    """
    mult = [esc,0]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = producto(mult,mat[i][j])
    return mat

def transpuesta(mat):
    """
        Param mat: Matriz a operar
        Return: Matriz resultante
    """
    temp = [[0 for i in range(len(mat))]for j in range(len(mat[0]))]
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            temp[i][j] = mat[j][i]
    return temp

def matrizConjugada(mat):
    """
        Param mat: Matriz a operar
        Return: Matriz Conjugada
    """
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = conjugado(mat[i][j])
    return mat

def matrizAdjunta(mat):
    """
        Param mat: Matriz a operar
        Return: Matriz resultante
    """
    return matrizConjugada(transpuesta(mat))
