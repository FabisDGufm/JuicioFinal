# Juicio Final  
**Proyecto final de Estructuras de Datos**

---

## Caso de uso

**Juicio Final** es un juego interactivo en donde el jugador toma el rol de una entidad divina encargada de decidir el destino de la Humanidad. 

Existen distintos grupos de humanos —como niños, políticos, artistas, entre otros— y el objetivo del jugador es determinar su destino basándose en su **karma**, una medida de su bondad o maldad, que podría ser un número de -100 a 100.

El ser divino dentro del juego puede escojer **salvar al grupo más bondadoso**, estos serían los que tengan el karma con el número mas alto. Esta decision por consecuencia conde
naría   00 al resto de grupos, por lo que se entiende que si eliges esta opción, premias la perfección. 

También, puedes elegir **castigar al grupo más malvado**, ese grupo con el nivel de karma más bajo, incluso podiendo llegar a ser un nivel en números negativos. Si tomas esta decisión, estarías condenando unicamente al grupo que tuvo las peores acciones, por lo que estarías teniendo una postura de castigo unicamente al que más lo merezca.

Otra decisión diferente a las dos anteriores, sería la de elegir **salvar a los grupos dentro de cierto rango de karma**. Se eligiría un karma mínimo e incluso máximo para ser salvado. Si tomas esta decisión, estarías buscando el justo medio, no estás a favor de la imperfección y no te agrada que existan personas super bondadosas. También puede que simplemente intentes salvar al máximo de grupos posibles. 

Finalmente, puedes dejar todo en manos del destino, y que **sea un grupo random el que sea salvado**, condenando al resto. Su elección sería totalmente aleatoria y tu no tendrías ningun tipo de poder directamente a la hora de decidir especificamente el destino de cada uno.


---

## Uso del AVL

El juego utiliza un **Árbol AVL** como estructura principal, representando cada nodo como un grupo humano con su nombre y karma.

El árbol no se limita a almacenar datos, sino que cobra protagonismo en la **lógica de toma de decisiones** del juego. Gracias al AVL, se garantiza una inserción ordenada y balanceada de los grupos usando el karma como clave, evitando árboles desbalanceados.

Esto permite **búsquedas eficientes** para funcionalidades como:

- **Buscar máximos y mínimos**
- **Filtrar por rangos**
- **Recorrer grupos en orden**

### Funcionalidades con AVL

- `insert()`: Calcula e inserta los valores de karma al árbol.
- `buscar_max()`: Devuelve el grupo con el karma más alto (más bondadoso).
- `buscar_min()`: Devuelve el grupo con el karma más bajo (más malvado).
- `buscar_rango(inf, sup)`: Encuentra grupos con karma entre dos valores dados.
- `inorder()`: Muestra todos los grupos ordenados de menor a mayor karma.
- `decision()`: Muestra opciones al jugador para decidir:
  1. Salvar al más bondadoso  
  2. Eliminar al más malvado  
  3. Salvar a los del rango # - #  
  4. Dejar que el destino decida (aleatorio)

---

## Uso de datos primitivos

Después de implementar todas las funcionalidades usando AVL, se realiza una **versión paralela del juego usando únicamente tipos de datos primitivos** (`int`, `str`, `bool`, etc.) sin estructuras de datos.

El objetivo es **demostrar las ventajas del uso del AVL** frente a soluciones más rudimentarias.

### Funcionalidades con datos primitivos

- `insert()`: Se asignan valores a cada grupo, por ejemplo:  
  `grupo1_nombre = "Niños"; karma1 = 85`
  
- `buscar_max()`: Se usa una cadena de `if` y `elif` para encontrar el mayor karma.
  
- `buscar_min()`: Se usa una cadena de `if` y `elif` para encontrar el menor karma.
  
- `buscar_rango(inf, sup)`: Se recorren los valores y se imprimen los que están dentro del rango usando `if`.
  
- `inorder()`: Orden manual de los grupos usando múltiples `if` anidados.
  
- `decision()`: Igual que en la versión con AVL, pero llamando funciones primitivas:
  1. Salvar al más bondadoso  
  2. Eliminar al más malvado  
  3. Salvar los del rango # - #  
  4. Dejar que el destino decida (aleatorio)

---

##  Delimitación del proyecto

- Se comparan **6 grupos humanos**
- Se utiliza `int` para los valores de karma y `str` para los nombres
- Se emplea `random` para la generación de karma
- En la versión primitiva se usan extensivamente `if`, `elif` y `else` para replicar la lógica del AVL


## Conclusiones del Proyecto

Durante el desarrollo de este proyecto, nos propusimos como objetivo resolver un mismo problema utilizando dos enfoques distintos: uno basado en un árbol AVL y otro utilizando únicamente datos primitivos.

### Retos encontrados

El mayor desafío surgió al trabajar con **datos primitivos**, ya que, al no contar con estructuras como listas o árboles, fue necesario encontrar soluciones empleando condicionales `if` y `elif`. Este enfoque implicó más líneas de código y un esfuerzo adicional en la lógica.

Por el contrario, la implementación con **árbol AVL** resultó mucho más eficiente y manejable, especialmente al realizar operaciones como la búsqueda del valor máximo o mínimo, donde pudimos aprovechar las ventajas que trae esta estructura.

### Reflexiones finales

Este proyecto dejó claro que el uso de **estructuras de datos** no solo simplifica el desarrollo, sino que también mejora la legibilidad, eficiencia y mantenibilidad del código. Si bien trabajar con datos primitivos fue una experiencia enriquecedora desde el punto de vista lógico, trabajar con árboles AVL ofreció una solución más elegante y funcional.

A pesar de las dificultades, logramos cumplir con el objetivo de implementar un **juego funcional utilizando ambos enfoques**, demostrando así nuestras habilidades para resolver problemas desde distintas perspectivas.


## Organización de código

* [tree](https://github.com/FabisDGufm/JuicioFinal/blob/main/tree.py)
* [main](https://github.com/FabisDGufm/JuicioFinal/blob/main/main.py)
* [AVL](https://github.com/FabisDGufm/JuicioFinal/blob/main/AVL.py)
* [primi](https://github.com/FabisDGufm/JuicioFinal/blob/main/primi.py)
