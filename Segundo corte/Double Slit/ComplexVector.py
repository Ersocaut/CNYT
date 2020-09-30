from Complex import *

def sumaVectores(vec1,vec2):
    """
        Adición de vectores complejos.
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
        Inverso (aditivo) de un vector complejo.
        Param vec1: Vector a operar
        Return: Vector Inverso
    """
    for i in range(len(vec)):
        act = vec[i]
        vec[i] = conjugado(act)
        vec[i][0] = - act[0]
    return vec

def escalarPorVector(esc,vec):
    """
        Multiplicación de un escalar por un vector complejo.
        Param esc: Número a operar
        Param vec: Vector a operar
        Return: Vector resultante
    """
    for i in range(len(vec)):
        vec[i] = producto(esc,vec[i])
    return vec

def sumaMatrices(mat1,mat2):
    """
        Adición de matrices complejas.
        Param mat1: Primera matriz a operar
        Param mat2: Segundo vector a operar
        Return: Matriz resultante
    """
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat1[i][j] = suma(mat1[i][j],mat2[i][j])
    return mat1

def matrizInversa(mat):
    """
        Inversa (aditiva) de una matriz compleja.
        Param mat: Matriz a operar
        Return: Matriz resultante
    """
    for i in range(len(mat)):
        mat[i] = vectorInverso(mat[i])
    return mat

def escalarPorMatriz(esc,mat):
    """
        Multiplicación de un escalar por una matriz compleja.
        Param esc: Escalar a operar
        Param mat: Matriz a operar
        Return: Matriz resultante
    """
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j]  = producto(esc,mat[i][j])
    return mat

def transpuesta(mat):
    """
        Transpuesta de una matriz/vector
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
        Conjugada de una matriz/vector
        Param mat: Matriz a operar
        Return: Matriz Conjugada
    """
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = conjugado(mat[i][j])
    return mat

def matrizAdjunta(mat):
    """
        Adjunta (daga) de una matriz/vector
        Param mat: Matriz a operar
        Return: Matriz resultante
    """
    return matrizConjugada(transpuesta(mat))

def productoMatrices(mat1,mat2):
    """
        Producto de dos matrices (de tamaños compatibles)
        Consideramos:
            mat1 := A
            mat2 := B
            Por ende, el número de columnas de A debe de coincidir con el número de filas de B
        Param mat1: Primera matriz a operar
        Param mat2: Segunda matriz a operar
        Return: Matriz resultante
    """
    if (len(mat1[0]) == len(mat2)):
        new = [[[0,0]  for i in range(len(mat2[0]))] for j in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                piv = [0,0]
                for k in range(len(mat2)):
                    mul = producto(mat1[i][k],mat2[k][j])
                    piv = suma(mul,piv)
                new[i][j] = piv
        return new

def accion(mat,vec):
    """
        Función para calcular la "acción" de una matriz sobre un vector.
        Param mat: Matriz a operar
        Param vec: Vector a operar
        Return: Número resultante
    """
    if (len(vec) == len(mat[0])):
        new = [[0,0] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                piv = producto(mat[i][j],vec[j])
                new[i] = suma(new[i],piv)
        return new

def productoInterno(vec1,vec2):
    """
        Producto interno de dos vectores
        Param vec1: Primer vector a operar
        Param vec2: Segundo vector a operar
        Return: Complejo resultante
    """
    new = [0,0]
    for i in range(len(vec1)):
        new = suma(new,producto(vec1[i],vec2[i]))
    return new

"""
"""

def norma(vec):
    """
        Norma de un vector
        Param vec: Vector a operar
        Return: Numero entero
    """
    return abs(productoInterno(vec,vec)[0])**(1/2)

def distancia(vec1,vec2):
    """
        Distancia entre dos vectores
        Param vec1: Primer vector a operar
        Param vec2: Segundo vector a operar
        Return: Número complejo
    """
    return norma(restaVectores(vec1,vec2))

def Identity(mat):
    """
        Creacion de una matriz identidad
        Param mat: Matriz que indica el tamaño
        Return: Matriz identidad
    """
    iden = [[[0,0]for i in range(len(mat[0]))] for j in range(len(mat))]
    for i in range(len(iden)):
        for j in range(len(iden[0])):
            if i == j:
                iden[i][j] = [1,0]
    return iden

def isUnitary(mat):
    """
        Revisar si una matriz es unitaria
        Param mat: Matriz a evaluar
        Return: Boolean := True (Es unitaria), False (No es unitaria)
    """
    if (len(mat) != len(mat[0])):
        return False
    else:
        iden = Identity(mat)
        adj = matrizAdjunta(mat)
        if productoMatrices(mat,adj) == iden:
            return True
        return False
    
def isHermitian(mat):
    """
        Revisar si una matriz es Hermitiana
        Param mat: Matriz a evaluar
        Return: Boolean True (Es hermitiana), False (No es Hermitiana)
    """
    return mat == matrizAdjunta(mat)

def tensor(mat1,mat2):
    """
        Param mat1: Primera matriz a evaluar
        Param mat2: Segunda matriz a evaluar
        Return: Matriz resultante
    """
    tem = []
    if (type(mat1[0][0]) is int) and (type(mat2[0][0]) is int):
        for i in range(len(mat1)):
            for j in range(len(mat2)):
                tem.append(producto(mat1[i],mat2[j]))
        return tem
    elif (len(mat1) == len(mat1[0])) and (len(mat2) == len(mat2[0])):
        for i in range(len(mat1)):
            for j in range(len(mat2)):
                piv = []
                for k in range(len(mat1[0])):
                    piv += escalarPorVector(mat1[i][k][:],mat2[j][:])
                tem.append(piv)
        return tem
