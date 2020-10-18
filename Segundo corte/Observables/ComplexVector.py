from Complex import *
import math

def subVect(vect1, vect2):
    length = len(vect1)

    if (length == len(vect2)):

        for x in range(length):
            vect1[x] = sub(vect1[x], vect2[x])

        return vect1


def sumVect(vect1, vect2):
    length = len(vect1)

    if (length == len(vect2)):

        for x in range(length):
            vect1[x] = suma(vect1[x], vect2[x])

        return vect1


def multVector(vect1, vect2):
    acu = [0, 0]
    for c in range(len(vect1)):
        acu = suma(acu, multComplexNumber(vect1[c], vect2[c]))
    return acu


def adjointVector(vector):
    for x in range(len(vector)):
        vector[x] = conjugated(vector[x])
    return vector


def inverseVect(vect):
    length = len(vect)
    for x in range(length):
        current = vect[x]
        vect[x] = conjugated(current)
        vect[x][0] = - current[0]

    return vect


def escalVect(vect, complexNumber):
    length = len(vect)

    for x in range(length):
        vect[x] = multComplexNumber(complexNumber, vect[x])

    return vect


def sumMat(mat1, mat2):
    row, colum = len(mat1), len(mat1[0])
    for i in range(row):
        for j in range(colum):
            mat1[i][j] = suma(mat1[i][j], mat2[i][j])

    return mat1


def subMat(mat1, mat2):
    row, colum = len(mat1), len(mat1[0])

    for i in range(row):
        mat1[i] = subVect(mat1[i], mat2[i])
    return mat1


def inverseMat(mat):
    row, colum = len(mat), len(mat[0])

    for i in range(row):
        mat[i] = inverseVect(mat[i])

    return mat


def multiEscalMat(complexNumber, mat):
    row, column = len(mat), len(mat[0])

    for i in range(row):
        for j in range(column):
            mat[i][j] = multComplexNumber(complexNumber, mat[i][j])

    return mat


def transpMatrix(matrix):
    row, col = len(matrix), len(matrix[0])

    if (type(matrix[0][0]) is int):
        return matrix

    answ = [[0 for x in range(row)] for t in range(col)]

    for i in range(col):
        for j in range(row):
            answ[i][j] = matrix[j][i]

    return answ


def conjugatedMatrix(matrix):
    row, col = len(matrix), len(matrix[0])

    if (type(matrix[0][0]) is int):
        for x in range(row):
            matrix[x] = conjugated(matrix[x])
        return matrix

    for i in range(row):
        for j in range(col):
            matrix[i][j] = conjugated(matrix[i][j])

    return matrix


def adjointMatrix(matrix):
    answ = conjugatedMatrix(transpMatrix(matrix))
    return answ


def multiplicaMat(mat1, mat2):
    row1, col1 = len(mat1), len(mat1[0])
    row2, col2 = len(mat2), len(mat2[0])

    if (col1 == row2):

        answ = [[(0, 0) for t in range(col2)] for x in range(row1)]

        for i in range(row1):
            for j in range(col2):

                current = (0, 0)

                for k in range(row2):
                    mult = multComplexNumber(mat1[i][k], mat2[k][j])

                    current = suma(current, mult)

                answ[i][j] = current

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")


def actionBoolMatrixOnVector(matrix, vector):
    row, col = len(matrix), len(matrix[0])
    length = len(vector)

    if (col == length):
        answ = [False for c in range(row)]

        for i in range(row):
            And = True

            for j in range(col):
                And = matrix[i][j] and vector[j]
                answ[i] = answ[i] or And

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")


def actionMatrixOnVector(matrix, vector):
    row, col = len(matrix), len(matrix[0])
    length = len(vector)

    if (col == length):
        answ = [[0, 0] for x in range(row)]

        for i in range(row):
            for j in range(col):
                mult = multComplexNumber(matrix[i][j], vector[j])
                answ[i] = suma(answ[i], mult)

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")


def internalProduct(vector1, vector2):
    return multVector(adjointVector(vector1), vector2)


def normVector(vector):
    answ = math.sqrt(abs(internalProduct(vector, vector)[0]))

    return answ


def distVector(vector1, vector2):
    answ = normVector(subVect(vector1, vector2))

    return answ


def identityMatrix(matrix):
    row, column = len(matrix), len(matrix[0])

    matrix = [[[] for i in range(column)] for j in range(row)]

    for i in range(row):
        for j in range(column):
            if i == j:
                matrix[i][j] = [1, 0]
            else:
                matrix[i][j] = [0, 0]
    return matrix


def isUnitary(matrix):
    row, col = len(matrix), len(matrix[0])

    if row == col:
        adjoint = adjointMatrix(matrix)

        return (multiplicaMat(matrix, adjoint) == identityMatrix(matrix)) or (
                    multiplicaMat(matrix, adjoint) == multiplicaMat(adjoint, matrix))


def isHermitan(matrix):
    answ = adjointMatrix(matrix)

    return str(answ) == str(matrix)


def tensorProduct(matrix1, matrix2):
    fil1, col1 = len(matrix1), len(matrix1[0])
    fil2, col2 = len(matrix2), len(matrix2[0])

    size = fil1 * fil2
    if (type(matrix1[0][0]) is int and type(matrix2[0][0]) is int):
        answ = []
        pos = 0

        for i in range(fil1):
            for j in range(fil2):
                answ.append(multComplexNumber(matrix1[i], matrix2[j]))

        return answ


    elif ((fil1 == col1) and (fil2 == col2)):

        answ = []
        column = 0
        for x in range(fil1):
            for y in range(fil2):
                row = []
                for z in range(col1):
                    row += escalVect(matrix2[y][:], matrix1[x][z][:])

                answ.append(row)

        return answ
