# __CNYT__
---
## Built in:

> Python 3
>
>The first part of the repository was made on 3.7 (32 bit) IDLE
>
>However, for some features and conveniences it was later built on 3.8 (32 bit) IDLE

## __Contributors:__

>Leonardo Galeano [Ersocaut](https://github.com/Ersocaut)

## How to

### Clone

- Open the Microsoft Windows command / Terminal on Mac.

- Go to the location where you want to clone the repository with ```cd XX``` where XX is the path of the location ``` cd Desktop/Downloads```.

- Execute the command ```git clone https://github.com/Ersocaut/CNYT``` This will take a few seconds to finish.

### Use the repository

- As long as you clone the repository, open the Microsoft Windows command / Terminal on Mac.

- Enter to the Directory of the library you're interested in with ```cd XX``` where XX is the Path of the library you want to use ````cd Primer Corte/ComplexNumbers```.

- Use the command line ```py XX.py``` where XX is the name of the py file of the library you want to run, or as you wish, run some Tests ```py TestComplex.py```.

### Contribute to the repository

- As long as:
  - You're a contributor.
  - You've made changes to the code.
  - You've tested that changes.
  - Those changes are definitive or mean an advance to the project.
  - The final commit you make must be into the Master branch.
- Open the Microsoft Windows command / Terminal on Mac, and locate on the main folder of the repository.

- Execute the command ```git add .```.

- Execute the command ```git status```, this is just to be sure of what changes are you going to submit.

- Execute the command ```git commit -m "XX"```, where XX must be an explanation of what you are going to push on the repository.

- Execute the command ```git push origin master```, to finally upload those changes to the remote repository.

### Download the last update of the repository as a contributor

- Open the Microsoft Windows command / Terminal on Mac.

- Execute the command ```git pull```.

---
## __Primer corte__
---
### ComplexNumbers:

Se hace la consideración de un número complejo como:

```
#Consideración de un número complejo
#Donde:
# a := parte entera del número complejo
# b := parte imaginaria del número complejo
Complex = (a,b)
Complex = [a,b]
```

Librería de Números complejos que cumple con:
  * Suma.
  * Producto.
  * Resta.
  * División.
  * Módulo.
  * Conjugado.
  * Conversión de Polar a Cartesiano.
  * Conversión de Cartesiano a Polar.
  * Fase de un número.
  
#### Pruebas relacionadas:

![](https://github.com/Ersocaut/CNYT/blob/master/_resources/ComplexTest.png)

---
### ComplexVectors:

Se hace la consideración de un vector complejo como:

```
#Consideración de un vector complejo
Complex = [a,b]

ComplexVector = [Complex,Complex,Complex]

#Consideración de una matriz compleja

ComplexMatrix = [ComplexVector,ComplexVector,ComplexVector]
```
Librería de Vectores y Matrices complejas que cumple con:
 * Adición de vectores complejos.
 * Inverso de un vector complejo.
 * Multiplicación de un escalar por un vector complejo.
 * Adición de matrices complejas.
 * Inversa de una matriz compleja.
 * Multiplicación de un escalar por una matriz compleja.
 * Transpuesta de una matriz/vector.
 * Conjugada de una matriz/vector.
 * Adjunta de una matriz/vector.
 * Producto de dos matrices de tamaños compatibles.
 * "Acción" de una matriz sobre un vector.
 * Producto interno de dos vectores.
 * Norma de un vector.
 * Distancia entre dos vectores.
 * Revisar si una matriz es unitaria.
 * Revisar si una matriz es hermitiana.
 * Producto tensor de dos matrices/vectores.

#### Pruebas relacionadas:

![](https://github.com/Ersocaut/CNYT/blob/master/_resources/ComplexVectorTest.png)

---
## __Segundo corte__
---
### ClassicToQuantum

Realizamos las siguientes consideraciones de un sistema:

1. Un sistema está compuesto tanto por un vector, como por una matriz.

2. Este varía con el tiempo, que es representado en unidades enteras.

3. Las siguientes consideraciones del código:

```
#Consideración de un número complejo
Complex = [a,b]

#Consideración de un vector complejo
ComplexVector = [Complex,Complex,Complex]

#Consideración de una matriz compleja
ComplexMatrix = [ComplexVector,ComplexVector,ComplexVector]

#Consideración de las unidades del tiempo
times = int(number) #type(number) is int

#Las dimensiones de la matriz y el vector están relacionados de la siguiente forma
len(ComplexMatrix) == len(ComplexVector)
```
Librería de sistemas probabilisticos cuánticos que cumple con:
* Los experimentos de la canicas con coeficiente booleanos.
* Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
* Experimento de las múltiples rendijas cuántico.
* Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se debe poder guardar en el computador con un formato de imágen.

#### Pruebas relacionadas:

![](https://github.com/Ersocaut/CNYT/blob/master/_resources/ClassicToQuantumTest.png)

---

