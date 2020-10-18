import math


def suma(complexNumber1, complexNumber2):
    answ = [complexNumber1[0] + complexNumber2[0],
            complexNumber1[1] + complexNumber2[1]]
    return answ


def sub(complexNumber1, complexNumber2):
    answ = [complexNumber1[0] - complexNumber2[0],
            complexNumber1[1] - complexNumber2[1]]

    return answ


def multComplexNumber(complexNumber1, complexNumber2):
    answ = [complexNumber1[0] * complexNumber2[0] - complexNumber1[1] * complexNumber2[1],
            complexNumber1[1] * complexNumber2[0] + complexNumber1[0] * complexNumber2[1]]

    return answ


def divComplexNumber(complexNumber1, complexNumber2):
    div = (complexNumber2[0]) ** 2 + (complexNumber2[1]) ** 2

    try:
        answ = [(complexNumber1[0] * complexNumber2[0] + complexNumber1[1] * complexNumber2[1]) / div,
                (complexNumber2[0] * complexNumber1[1] - complexNumber1[0] * complexNumber2[1]) / div]

        return answ

    except ZeroDivisionError as error:
        print('Se produjo el siguiente error', error)


def conjugated(complexNumber):
    answ = [complexNumber[0],
            -complexNumber[1]]

    return answ


def module(complexNumber):
    answ = math.sqrt((complexNumber[0]) ** 2 + (complexNumber[1]) ** 2)

    return answ


def phase(complexNumber):
    x, y = complexNumber[0], complexNumber[1]

    if (x < 0 and y < 0) or (x < 0 and y >= 0):
        return math.pi + (math.atan(complexNumber[1] / complexNumber[0]))

    elif x >= 0 and y < 0:
        return 2 * math.pi + (math.atan(complexNumber[1] / complexNumber[0]))

    else:
        return (math.atan2(complexNumber[1] , complexNumber[0]))


def cartesianToPolar(complexNumber):
    angle = phase(complexNumber)
    answ = [module(complexNumber),
            angle]
    return answ
