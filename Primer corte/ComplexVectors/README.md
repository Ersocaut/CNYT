# **Números complejos**

En esencia, son números que constan de una parte real y otra imaginaria, siendo representados comunmente de la forma:

> c = a + b _i_
>
> Donde:
>
> a := Parte real del número complejo
>
> b := Parte imaginaria del número complejo
>
> Si b = 0, la representación del número complejo sigue siendo valida, aunque por definición sería un número real

## ¿Para qué sirven los números complejos e imaginarios?

Para dar solución a sistemas de ecuaciones que no la tengan dentro de los números reales.
Uno de los varios ejemplos es: _*X^2 + 1 = 0*_
Encontraremos que la solución es la raíz cuadrada de un número negativo, lo que dentro de los reales, no tiene cabida.

## Operaciones con números complejos

Al estar compuestos de una forma diferente a los números que solemos trabajar, la forma en que los operamos también cambia considerablemente.

```
#Para las implementaciones en el lenguaje Python haremos la siguiente consideración.
ComplexNumber = [a,b]
```

* **Suma**
  - Sumamos la parte real de ambos números, y así mismo con la parte imaginaria.
    Siendo la combinación de estos dos, el número complejo resultante.
    
    **(a1,b1) + (a2,b2) = (a1 + a2, b1 + b2)**

* **Resta**
  - El proceso es el conjugado de la suma, es decir, de la misma forma pero con un cambio en los signos.
    
    **(a1,b1) - (a2,b2) = (a1 - a1, b1 - b2)**

* **Multiplicación**
  - A la hora de multiplicarlos ya se complica un poco más el procedimiento, pues no es igual de sencillo a los anteriores.
   
    **(a1,b1) x (a2,b2) = (a1,b1)(a2,b2) = (a1a2 - b1b2, a1b2 + a2b1)**
* **División**
  - En definitiva es la operación más complicada a efectuar con números complejos.
    En esta sigue aplicando la excepción de que no se puede realizar una división por cero.
    Podemos plantear en un primer momento la división como:
    
    **(x,y) = (a1,b1) / (a2,b2)**

    Al saber que la división es la operación contraria a la multiplicación podemos decir que:

    (a1,b1) = (x,y)(a2,b2)

    Despejando, y resolviendo tanto para x como para y, obtenemos que:

    **x = (a1a2 + b1+b2) / (a2^2) + (b2^2)**

    **y = (a2b1 - a1b2) / (a2^2) + (b2^2)**

    Si (a2^2) + (b2^2) = 0, no se puede realizar la división.