from math import pi as pi
from math import atan as arctan
global e
e = 2.718281828459045
def suma(num1,num2):
    """
        Param num1: Primer número complejo
        Param bnum2: Segundo número complejo
        Return: Número complejo resultante
    """
    a1,b1 = num1[0], num1[1]
    a2,b2 = num2[0], num2[1]
    a3 = a1 + a2
    b3 = b1 + b2
    return [a3, b3]

def producto(num1,num2):
    """
        Param num1: Primer número complejo
        Param bnum2: Segundo número complejo
        Return: Número complejo resultante
    """
    a1,b1 = num1[0], num1[1]
    a2,b2 = num2[0], num2[1]
    a3 = (a1*a2) - (b1*b2)
    b3 = (a1 * b2) + (a2 * b1)
    return [a3, b3]

def resta(num1,num2):
    """
        Param num1: Primer número complejo
        Param bnum2: Segundo número complejo
        Return: Número complejo resultante
    """
    a1,b1 = num1[0], num1[1]
    a2,b2 = num2[0], num2[1]
    a3 = a1 - a2
    b3 = b1 - b2
    return [a3, b3]

def division(num1,num2):
    """
        Param num1: Primer número complejo
        Param num2: Segundo número complejo
        Return: Número complejo resultante
    """
    a1,b1 = num1[0], num1[1]
    a2,b2 = num2[0], num2[1]
    piv = (a2**2)+(b2**2)
    a3,b3 = 0,0
    try:
        a3 = ((a1 * a2) + (b1*b2)) / piv
        b3 = ((a2 * b1) - (a1*b2)) / piv
        return [a3, b3]
    except ZeroDivisionError as error:
        print("Error:",error)

def modulo(num):
    """
        Param num: Número complejo
        Return c: Valor del módulo del número
    """
    a,b = num[0],num[1]
    a = a**2
    b = b**2
    c = (a + b)**(1/2)
    return c

def conjugado(num):
    """
        Param num: Número complejo
        Return: Conjugado
    """
    return [num[0],-num[1]]

def sin(x):
    """
        Param x: En radianes, el número del que se desea hallar el seno
        Return s: Seno de x
    """
    global e
    s = (e**(x*1j)).imag
    return s

def cos(x):
    """
        Param x: En radianes, el número del que se desea hallar el coseno
        Return c: Coseno de x
    """
    global e
    c = (e**(x*1j)).real
    return c

def polarACartesiano(coord):
    """
        Param coord: Coordenadas polares
        Return: Coordenada cartesiana
    """
    r,t = coord[0],coord[1]
    x = r * (cos(t))
    y = r * (sin(t))
    return [x, y]

def cartesianoAPolar(coord):
    """
        Param coord: Coordenada cartesiana
        Return: Coordenada polar
    """
    x,y = coord[0], coord[1]
    r = ((x**2) + (y**2))**(1/2)
    t = fase(coord)
    return [r,t]

def fase(num):
    """
        Param num: Número complejo
        Return f: Fase del número
    """
    a,b = num[0], num[1]
    f = arctan(b/a)
    if (a < 0 ):
        f += pi
    elif (a >= 0) and (b < 0):
        f += 2 * pi
    return f

