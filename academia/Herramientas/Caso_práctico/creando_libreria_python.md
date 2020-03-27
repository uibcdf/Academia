# Creando una libreria de código abierto y de uso libre en Python

El objetivo de este breve tutorial es crear una hipotética librería de Python cuyo código y uso
sean de acceso libre. Para que el código sea abierto haremos uso de GitHub. Allí publicaremos
cualquier avance en el desarrollo de nuestra herramienta.

Nuestra librería se llamará "Morsa" y tendrá un contenido muy simple implementado
únicamente con el propósito de que sea ilustrativo. Todo el proceso de desarrollo se describe
a continuación pero si eres impaciente puedes ver el resultado final [aquí](https://github.com/uibcdf/Morsa).

## El repositorio remoto en GitHub

Crea el repositorio remoto en GitHub, llamado en este como la librería, como se indica en [el tutorial de Academia dedicado a ello](../Creando_GitHub_Repo/creando_github_repo.md).
No olvides crear tu clon remoto en la computadora.

## Estructura de ficheros para la librería

Existen directrices claras sobre qué estructura darle a un proyecto de desarrollo de software en
Python. Vamos a mencionar unas pocas que nos servirán en principio para entender la mayoría de
librerías de código libre con los que trabajaremos así como para homogeneizar unos mínimos criterios en nuestro laboratorio.

### El código fuente

En la carpeta de nuestro proyecto localizaremos el código en un nuevo directorio llamado como la
librería pero en letras minúsculas.

```bash
mkdir morsa
```

### La documentación

Veremos al final cómo documentar el código para que verdaderamente tenga sentido que sea código
abierto. Un código bien documentado será más facil de usar para cualquiera y tendrá más
oportunidades para crecer en su desarrollo. Piensa siempre que programas para que en cualquier
momento otra persona pueda sumarse a tu proyecto y echar una mano (esa otra persona puede ser tu
"yo futuro"). Ubicaremos la documentación en la carpeta `docs`.

```bash
mkdir docs
```

### Tests

Todo código que va a ser de código libre debe implementar una batería de tests. ¿Por qué? Vamos a
suponer que tu proyecto crece y se suman más colaboradores o encuentras usuarios activos que van a
implementar alguna mejor o a corregir algún error inadvertido. Querrás entonces minimizar el
esfuerzo que conlleve controlar que las modificaciones al código no han arruinado inesperadamente
su funcionalidad. Para esto implementaremos una batería de tests que nos permitan confiar
mínimamente en el uso de nuestra herramienta aunque su desarrollo se realice en una continua
implementación de modificaciones.

```bash
mkdir tests
```

### Herramientas de desarrollo y liberación

Uno de los últimos pasos que veremos será la publicación de nuestra herramienta en alguna de las
plataformas de distribución de librerías de Python, p.ej. Conda. Las instrucciones para esto así
como otros ficheros cuya funcionalidad encuentra su contexto en el desarrollo del código o su
liberación las ubicaremos en la carpeta `devtools`.

```bash
mkdir devtools
```

### La licencia

*Para ser escrito más adelante*

### El fichero `.gitignore`

Como seguramente ya conoces `.gitignore` describe la lista de rutas o nombres de fichero que serán
ignorados por git. Puedes encontrar en internet listas de ficheros a ignorar recomendadas según la
naturaleza del repositorio: una librería de python, una página web, etc. En este caso vamos a
incluir en el fichero `.gitignore`:

```
__pycache__/*
*/__pycache__/*
*.so
*.pyc
INSTALL.log
*.egg-info/*
record.txt
*.ipynb_checkpoints
/docs/api/_autosummary
*.mod
dist/*
*/build/
build/
```

### Las instrucciones para la instalación de la librería

El fichero que contendrá las instrucciones de instalación de la librería en nuestro entorno de
trabajo se llamará `setup.py`. Por el momento este fichero contendrá las siguientes lineas de
código:

```python
from setuptools import setup, find_packages

setup(
    name='morsa',
    version='1.0.0',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'morsa': 'morsa'},
    packages=find_packages(),
    package_data={'morsa': []},
    scripts=[],
    url='http://github.uibcdf.org/Morsa',
    download_url ='https://github.com/uibcdf/Morsa',
    license='MIT',
    description="Morsas, pingüinos y ballenas juegan al parchis, dominó, ajedrez y tres en ralla. ¿Quien ganará?",
    long_description="Esta libreria es el producto final de un tutorial sobre cómo programar una\
    librería en Python (ver: xxx). Puedes encontrar más información en xxx.",
)
```

Lo principal a observar en este script es que hay una librería llamada `setuptools` de la cual
estamos importando el método `setup`. Este método requiere una serie de argumentos de entrada como
`name`, `version`, `author`, etc. En este script, en el caso de esta librería, basta con que
modifiques si quieres el valor de alguno de estos argumentos de entrada a tu conveniencia.

Por último, este script instala la librería que le estamos indicando al ser ejecutado (o
interpretaod por python):

```python
python setup.py develop
```

Y para desinstalarla podemos hacer simplemente:

```python
pip uninstall morsa
```

Puedes encontrar más información sobre las posibilidades de este script y el método `setup`
[aquí](https://docs.python.org/3.7/distutils/setupscript.html) o [aquí](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py).

## El código

Desarrollemos en primer lugar lo fundamental, el código. "Morsa" va a ser una librería de python
capaz de realizar unas sencillas tareas con el único motivo de ilustrar la composición e
implementación de una librería con módulos, clases, métodos, dependencia de otras librerías, etc. 

Morsa va a permitir una dinámica sencilla en la que varios personajes virtuales, animales -ballenas, pingüinos o morsas-, se enfrentan entre si en
distintos juegos -parchís, ajedrez, dominó o tres en raya- acumulando o perdiendo puntos según ganan o pierden. Puede que en este momento no
se entienda completamente pero veamoslo poco a poco.

Debes intentar implementar el código únicamente con las siguientes indicaciones. Recuerda que si en
algo te atoras puedes echarle un ojo a [la versión de Morsa publicada en el repositorio de GitHub de
la UIBCDF](https://github.com/uibcdf/Morsa/tree/master/morsa).

### Los juegos

En la carpeta del código en el repositorio vamos a crear el primer fichero o módulo de nuestra
librería. Abre con tu editor de textos favorito el nuevo fichero `juegos.py`.

En él introduce las lineas de código necesarias que resuelvan los siguientes puntos.

#### 1. Lista de juegos

Define un objeto que albergue la lista de juegos: ["parchís", "ajedrez", "dominó", "tres en raya"]

#### 2. Diccionario con puntuaciones por juego

Define un diccionario que contenga la puntuación, positiva cuando gana y negativa cuando pierde,
para cada juego. ¿Qué tal si este diccionario contiene diccionarios dentro? Haz que este objeto
almacene los siguientes valores:

| Juego  | Gana  | Pierde |
|:-:|:-:|:-:|
| "parchís" | +1 | -1 |
| "ajedrez" | +2 | -1 |
| "dominó" | +1 | 0 |
| "tres en raya" | +1 | -2 |


#### 3. Método para listar los juegos

Define un método llamado `consulta_lista_de_juegos` que al ejecutarlo sin ningún argumento devuelva
la lista de juegos del punto 1. De tal manera que su funcionamiento sea como:

```python
consulta_lista_de_juegos()
['parchís', 'ajedrez', 'dominó', 'tres en raya']
```

#### 4. Método para consultar los puntos ganados o perdidos por juego

Define un método llamado `consulta_puntos_por_juego` con el argumento de entrada `juego`. Este
argumento de entrada puede tomar el valor 'parchís', 'ajedrez', 'dominó' o 'tres en raya" para que
el método devuelva los puntos que se ganan y pierden con ese juego. De tal manera que su
funcionamiento sea como:

```python
consulta_puntos_por_juegos(juego='parchís')
{'gana': 1, 'pierde': -1}
```

#### 5. Método para asignar puntos por juego

Define un método llamado `asignar_puntos_por_juego` con tres argumentos de entrada: `juego`, `gana`
y `pierde`. Este método reasignará los valores introducidos por el usuario en el diccionario del
punto 2. De tal manera que su funcionamiento sea como:

```python
asignar_puntos_por_juego(juego='parchís', gana=100, pierde=-1000)
```

Para que ahora encontremos lo siguiente si a continuación se ejecuta el método del punto 4.

```python
consulta_puntos_por_juegos(juego='parchís')
{'gana': 100, 'pierde': -1000}
```

#### 6. Método "interno" para hacer el reparto de puntos

Define un método llamado `_reparte_puntos` con dos argumentos de entrada: `juego` y `resultado`. La
función de este método es devolver la cantidad de puntos según el juego y el resultado definidos en
el objeto del punto 4. Te propongo que `resultado` pueda tomar los valores `gana` o `pierde`, de
tal manera que:

```python
_reparte_puntos(juego='parchís', resultado='pierde'):
-1
```

#### 7. Método selector aleatorio de juegos:

Define un método llamado `generador_aleatorio_de_juegos` que no tenga argumentos de entrada y
devuelva uno de los juegos de la lista. La elección del juego debe ser aleatoria y equiprobable
entre los elementos de la lista definida en el punto 1. Puedes ayudarte del método que más te
convenga del modulo `random` de la librería Numpy (qué tal `random.randint` o `random.choice`).

El funcionamiento entonces ha de ser tal que por ejemplo:

```python
generador_aleatorio_de_juegos()
'dominó'
```

#### 8. Prueba que los elementos del módulo funcionan

Un fichero de python puede ser importado ya como un módulo (o una librería que únicamente tiene un
módulo). Hay varias maneras de hacer esto, veamos cómo podemos hacerlo con python, ipython o
jupyter lab desde la carpeta en la que se encuentra el fichero `juegos.py` y otra cualquiera.

##### 8.1 Importando el módulo con python o ipython desde la misma carpeta

Con la terminal ubicada en la misma carpeta en la que se encuentra `juegos.py` puedes ejecutar:

```bash
python
```

o

```bash
ipython
```

Puedes comprobar con cualquiera de las dos versiones de interpretador que puedes importar
`juegos.py` e interaccionar con sus elementos:

```python
import juegos as juegos
```

Ya puedes ejecutar los métodos a ver si funcionan como deseas. Por ejemplo:

```python
juegos.consulta_puntos_por_juego(juego='parchís')
juegos.asignar_puntos_por_juego(juego='parchís', gana=40, pierde=-80)
juegos.consulta_puntos_por_juego(juego='parchís')
```

o

```python
juegos.generador_aleatorio_de_juegos()
```

##### 8.2 Importando el módulo en un jupyter notebook

Puede que te sea un poco mas cómodo trabajar en un jupyter notebook. Para ello, con la terminal
ubicada en la carpeta del fichero `juegos.py`, ejecuta:

```bash
jupyter lab
```

Abre entonces un nuevo jupyter notebook y ya puedes importar `juegos.py` e interaccionar con sus
elementos. Crea la primera celda en la que importes el módulo y ejecútala:

```python
import juegos as juegos
```

Ya puedes ejecutar los métodos como se propone en la subsección anterior (8.1).

En el caso de que tengas que corregir algo en el fichero `juegos.py` no hace falta que reinicies el
notebook, al igual que ipython, jupyter tiene una serie de comandos mágicos que modifican su
comportamiento. Si como primera celda del notebook ejecutas en siguiente código:

```python
%load_ext autoreload
%autoreload 2
```

Estamos haciendo que el notebook "recargue" las librerías importadas cada vez que ejecutas una
nueva celda. Así, si editas el contenido de `juegos.py` y guardas los cambios, la siguiente celda
que ejecutes en el notebook lo hará leyendo de nuevo el fichero y por consiguiente ejecutando los
cambios hechos.

##### 8.3 Importando el módulo desde cualquier otro sitio

Puedes por último importar el módulo `juegos.py` con la terminal ubicada en cualquier carpeta, pero
en este caso tienes que añadir el directorio en el que se encuentra el `juegos.py` a la lista de
rutas (*paths*) que python checa para buscar librerías. Ejecuta, con la terminal ubicada en
cualquier directorio distinto al del código (`morsa`), python, ipython o jupyter lab.

Ahora que tienes cualquiera de las tres versiones interactivas del interpretador importa la
librería `sys` para ver la lista de directorios en los que python va a buscar librerías:

```python
import sys
print(sys.path)
```

Podemos añadir como primer elemento de la lista la ruta a nuestro fichero. Si estuviera por ejemplo
en el directorio `/home/liliana/Projects/Morsa/morsa`:

```python
sys.path.insert(0, "/home/liliana/Projects/Morsa/morsa")
```

Ahora ya puedes importar el módulo:

```python
import juegos as juegos
```

### Los jugadores

Los jugadores son tres tipos de animales diferentes: ballenas, pingüinos y morsas. 
Como animales que son todos ellos, tendrán elementos comunes y elementos que los distinguen. 
Te propongo que crees la clase de python `Animal` con todo lo que puede ser común, para despues crear las clases `Ballena`, `Pinguino` y `Morsa`.
Estas últimas heredando los atributos y métodos de `Animal`. Hagamos esto en dos ficheros situados en una nueva carpeta que funcionará como módulo independiente.

#### 1. Una estructura de ficheros como módulo

En primer lugar, dentro de la carpeta del código, vamos a crear la carpeta `jugadores`. Hasta Python 3 para declarar que
un directorio actuaba como módulo había que crear en él un fichero llamado `__init__.py`, vamos a seguir haciendolo
porque nos permite tener un código mas ordenado como veremos al final de esta lista de tareas.

```bash
make jugadores
touch jugadores/__init__.py
```

También con el propósito de que la estructura de ficheros sea facilmente inteligible en un primer vistazo, vamos a crear
dos ficheros mas dentro del directorio jugadores: `plantilla.py` con los objetos comunes a cualquier especie a animal y
`animales.py` con las classes de cada especie.

```bash
touch jugadores/plantilla.py
touch jugadores/animales.py
```

#### 2. La clase Animal.

Abre con tu editor de textos el fichero `jugadores/plantilla.py` y crea una clase llamada `Animal`.

##### 2.1 Atributos de la clase Animal

Esta clase debe tener los siguientes atributos:

- nombre [argumento de entrada, por defecto: None]
- edad [argumento de entrada, por defecto: None]
- especie [por defecto: None]
- suerte [veremos el valor por defecto más adelante]
- puntos [por defecto: 0]
- habilidad [por defecto: diccionario vacio {}]

Donde únicamente `nombre` y `edad` son argumentos de entrada para el método constructor de la clase
(`__init__`) con valor por defecto `None`.

##### 2.2 Método para reiniciar los puntos

Define el método en la clase Animal `reiniciar_puntos` sin argumentos de entrada (únicamente `self`). La
función de este método es volver a asignar el valor 0 al atributo `suerte`.
tal manera que:

```python
objeto = Animal()
objeto.reiniciar_puntos()
print(objeto.puntos)
0
```
##### 2.3 Método para conocer quien es

Define el método `quien_soy` en la clase Animal con el argumento de entrada `solo_nombre`(por
defecto: False). Para ilustrar la función de este método supongamos que los atribus `nombre`,
`edad` y `especie` tienen los valores 'Samanta', 35 y 'ballena'. Al ejecutar este método debemos ver impreso:

```python
objeto = Animal()
objeto.nombre = 'Samanta'
objeto.edad = 35
objeto.especie = 'ballena'

objeto.quien_soy(solo_nombre=True)
'Soy Samanta'

objeto.quien_soy()
'Soy Samanta, tengo 35 años y soy una ballena'
``` 

Ten en cuenta que cuando `solo_nombre=False` la frase impresa debe incluir el articulo 'una' en
caso de que `especie` sea 'ballena' o 'morsa', y 'un' en caso de que `especie` sea igual a
'pingüino'.

##### 2.4 En caso de que el argumento de entrada `nombre` sea None...

Al final de la función `__init__` vamos asignar un valor al atributo nombre en el caso de que el usuario no lo haya
hecho mediante el argumento de entrada. Si el atributo `nombre` sigue teniendo el valor None, importa la librería `faker` -que puedes instalar con conda- para asignar
automaticamente un nombre falso (écha un ojo a [la sección Basic Usage de su documentación](https://faker.readthedocs.io/en/latest/index.html#basic-usage)).

##### 2.5 En caso de que el argumento de entrada `edad` sea None...

Al igual que en el punto anterior, otorga un valor aleatorio al atributo `edad` en caso de que no
haya sido asignado ninguno por el usuario mediante el argumento de entrada. Dicho valor debe ser un
numero entero aleatorio mayor o igual que 18 y menor o igual que 100. Puede que el método
`randint` del módulo `random` de Numpy pueda ayudarte

##### 2.6 Funciónes externas a la clase `Animal`

Define en el mismo fichero `plantilla.py` el método externo a la clase Animal `asignar_suerte`. La
función de dicho método es generar un número flotante aleatorio entre 0 y 1 (distribución de
probabilidad uniforme). De tal manera que

```python
asignar_suerte()
0.35
```

Define, de la misma manera, el método `asignar_nivel_de_habilidad`. La función de este método es la
misma que la de `asignar_suerte`. De tal manera que:

```python
asignar_nivel_de_habilidad():
0.84
```
##### 2.7 Prueba la clase y los métodos implementados

Aunque todavía le falta algo a este fichero, ya lo podemos probar. Al igual que en el punto 8 de la
descripción del fichero `juegos.py`, importa este fichero como un módulo independiente y prueba
que:

```python

import plantilla as plantilla

objeto = plantilla.Animal(nombre="Ramón", edad=50)
objeto.especie = 'ballena'
objeto.quien_soy(solo_nombre=True)
'Soy Ramón'
objeto.quien_soy()
'Soy Ramón, tengo 50 años y soy una ballena'

objeto = plantilla.Animal()
objeto.especie = 'pingüino'
objeto.quien_soy()
'Soy Eugenia Silva Moreno, tengo 81 años y soy un pingüino' # nombre y edad aleatorios

plantilla.asignar_suerte()
0.59

plantilla.asignar_nivel_de_habilidad()
0.03
```

#### 3. Las clases `Ballena`, `Pinguino` y `Morsa`.

El fichero `jugadores/plantilla.py` todavía necesita alguna modificación, pero antes vamos a editar
el fichero `jugadores/animales.py`. Será más facil ir entendiendo el sentido de estas clases al
final de esta sección.

##### 3.1 Vamos a necesitar los elementos de `jugadores/plantilla.py`

Las primeras lineas del fichero `jugadores/animales.py` deben ser para importar la clase `Animal` y
los métodos `asignar_nivel_de_habilidad` y `asignar_suerte`.

##### 3.2 Define las clases `Morsa`, `Pinguino` y `Ballena`.

Define las clases `Morsa`, `Pinguino` y `Ballena` heredando todos los atributos y métodos de `Animal`. Los
argumentos de entrada para sus tres funciones `__init__` también serán `nombre` (por defecto, None) y
`edad` (por defecto, None).

Deberás, en las tres clases, despues de la linea de la función `__init__`, invocar el método
`super()` para ejecutar la incialización heredada de la clase 'Animal' (un poco de información
sobre dicho método [aquí](https://realpython.com/python-super/)) con los argumentos `nombre` y
`edad`.

Define, para cada una de las tres clases, el valor apropiado del atributo `especie`: 'morsa',
'pingüino' y 'ballena' según el caso.

Define, para cada una de las tres clases, el contenido del diccionario en el atributo `habilidad`.
Dicho diccionario, para el caso de la clase 'morsa' deberá relacionar el nombre de siguientes tres de los
cuatro juegos disponibles para la competición, 'parchís', 'dominó' y 'tres en raya', con un factor
aleatorio generado por el método `asignar_nivel_de_habilidad` que hemos importado del fichero
`.plantilla` en el punto 3.1. Para que te sea más facil entender este cometido, el contenido de
habilidad para `Morsa` debe ser tal que, por ejemplo:

```python
jugador = Morsa()

type(jugador.habilidad)
dict

print(jugador.habilidad)
{'parchís': 0.23, 'dominó': 0.68, 'tres en raya': .31}
```

Donde los números flotantes, valores del diccionario, fueron creados aleatoriamente por
`asignar_nivel_de_habilidad` a la hora de inicializar el objeto de clase `Morsa`.

Para el caso de la clase `Pinguino` los tres juegos son: 'ajedrez', 'dominó' y 'tres en raya'. Y
para la clase `Ballena`: 'parchís', 'dominó' y 'ajedrez'.

##### 3.3 Define un método ediferente para cada clase

Vamos a definir ahora un método propio de cada clase.

En el caso de `Morsa` define el método `reasigno_suerte`. Este método no debe tener más argumento
de entrada que `self`, y su función que el atributo heredado `suerte` tome un nuevo valor otorgado
por la salida del método `asignar_suerte` importado de `.plantilla` en el punto 3.1.

Para el caso de `Pinguino`, el método se llamará `reasigno_habilidades`. Como puedes deducir del
nombre del método, su función en redefinir los valores del diccionario `habilidad` para los juegos
'ajedrez', 'dominó' y 'tres en raya'. Este método no tendrá tampoco más argumentos de entrada que
`self`.

Por último, para el caso de la clase `Ballena` el método se llamará
`reasigno_suerte_y_habilidades`. En este caso el atributo `suerte` tomará un nuevo valor otorgado
por `asignar_suerte` y los valores 'parchís', 'dominó' y 'ajedrez' del diccionario `habilidades`
serán redefinidos por la salida del método `asignar_nivel_de_habilidad`

##### 3.4 Completando el fichero '__init__.py'

Ya podemos decidir a qué de todo lo programado en ambos fichero tendrá acceso un posible usuario al
importar el módulo: únicamente a las clases `Morsa`, `Pinguino` y `Ballena`. Para esto abre tu
editor de textos e incluye:

```python
from .animales import Morsa, Pinguino, Ballena
```

De esta manera al importar el módulo `jugadores` se entiende que el usuario tiene disponibles
únicamente las clases `Morsa`, `Pinguino` y `Ballena`.

##### 3.5 Importa el módulo `jugadores`

Desde la carpeta principal del código `morsa` ya puedes abrir python, ipython o un notebook de
jupyter lab e importar jugadores:

```python
import jugadores

jugador_1 = jugadores.Morsa(nombre="Ramón", edad=40)
jugador_1.quien_soy()

print(jugador_1.habilidad)

print(jugador_1.suerte)

jugador_1.reasigno_suerte()
print(jugador_1.suerte)
```

Prueba también a crear objetos de clase `Pinguino` y `Ballena`, y prueba que sus atributos y
métodos funcionan como esperas.

#### 4 La competición

El último fichero que completa el contenido de la librería es `competicion.py`. Abre, en la carpeta
`morsa`, con tu editor el nuevo fichero y sigue las instrucciones siguientes para crear dos
métodos: `jugar` y `quien_tiene_mas_puntos`.

##### 4.1 Define la función `quien_tiene_mas_puntos`

Este método llamado `quien_tiene_mas_puntos` devuelve el nombre, la puntación y la especie del
animal que más puntos tiene de una lista dada como argumento de entrada. De tal manera que
si por ejemplo tenemos tres jugadores, `jugador_1`, `jugador_2` y `jugador_3`:

```python
nombre, puntos, especie = quien_tiene_mas_puntos(jugadores=[jugador_1, jugador_2, jugador_3])
print(nombre, puntos, especie)
'Ramón', 103, 'pingüino'
```

##### 4.2 Define la función `jugar`

Este método es el último que debes implementar y el más importante. Debes definirlo con cuatro
argumentos de entrada: `juego` (por defecto, None), `jugador1` (por defecto, None), `jugador2` (por
defecto, None) y `verbose` (por defecto, False).

La función es la siguiente. Dos jugadores se enfrentan en uno de los juegos de la siguiente manera:

- Si alguno de los jugadores no sabe jugar a ese juego (no lo tiene definido en su diccionario
  `habilidad`) la función no hace nada. Únicamente, si `verbose` es `True`, se imprime el mensaje "XXX no sabe jugar YYY", donde
XXX es el nombre de dicho jugador y YYY el nombre del juego.

- Si los dos jugadores saben jugar al juego introducido en el argumento de entrada `juego`, se
  generan dos números aleatorios entre 0 y 2.0, a dichos números los llamaremos
`inspiracion_jugador1` e `inspiracion_jugador2`. Ahora, definiremos dos variables que llamaremos
`acierto_jugador1` y `acierto_jugador2`. Cada una de estas variables toma el valor de la
inspiración más la suerte multiplicada por la habilidad en el juego elegido, para cada jugador. Ya
podemos decidir qué jugador es el ganador, aquel cuyo valor de la variable `acierto_jugador_1` o `acierto_jugador_2` es mayor.

- Al jugador ganador se le suma, a su atributo `puntos`, el valor contenido en el
  diccionario llamado `_reparte_puntos` del fichero `juegos.py` (el valor correspondiente a la
situación 'gana' del juego elegido). Mientras que al jugador que pierde se le suma la
correspondiente cantidad de puntos indicada en el mismo diccionario, esta vez con la clave
'pierde'.

- Por último, en el caso de que el argumento de entrada `verbose` tenga el valor True, se imprime
  por pantalla la frase "Ganó XXX", donde XXX es el nombre del ganador, o "Ninguno gana" en caso de
empate.

##### 4.3 Implementación del fichero `__init__.py` principal

Los distintos módulos ya están programados con los elementos necesarios. Algunos de estos elementos
fueron implementados únicamente para el funcionamiento de otros. Quizá no sería oportuno ofrecer
esos elementos al usuario de la librería, sino únicamente los que fueron pensados para ello. Es por
esto que vamos a crear un fichero `__init__.py` para que el mismo directorio `morsa` pueda ser
importado como librería. En ese fichero `__init__.py` vamos a importar lo siguiente:

- de `competicion.py`: `jugar` y `quien_tiene_mas_puntos`
- de `juegos.py`: `consulta_lista_de_juegos`, `consulta_puntos_por_juego`,
  `generador_aleatorio_de_juegos` y `asignar_puntos_por_juego`
- y el módulo `jugadores` se importa como módulo con el mismo nombre.

##### 4.4 Ya se puede probar finalmente la librería

Desde el directorio principal del repositorio, ese en el que se encuentra la carpeta `morsa`, ya
puedes abrir el interpretador de python e importar toda la librería:

`import morsa`

Comprueba que, por ejemplo, la librería que has implementado ejecuta correctamente el notebook de
jupyter que puedes encontrar en la carpeta `examples`. Pero antes, si quieres, puedes ya instalar
`morsa` en tu entorno de trabajo:

```bash
python setup.py develop
```

Puedes ahora importar `morsa` con la terminal ubicada en cualquier sitio, ya que ahora está
instalado como una librería más. Si por ejemplo estás usando conda como gestor de microambientes y
librerías, veras que `morsa` aparece en la lista de paquetes instalados en el micro ambiente:

```bash
conda list | grep morsa
```

Puedes modificar lo que quieras del código en la carpeta `morsa` sin necesidad de reinstalar la
librería. El script de instalación `setup.py` se ejecutó en la modalidad desarrollo (develop).

Por último, si quieres desinstalar la librería del microambiente puedes en la terminal ejecutar:

```bash
pip uninstall morsa
```

Verás que ya no se encuentra entre los paquetes instalados:

```bash
conda list | grep morsa
```

### Tutorial

Ya tienes lista la librería para poder jugar con ella. Un ejemplo de qué hacer con `morsa` lo
puedes encontrar en el tutorial del repositorio: `examples/tutorial.ipynb`.

