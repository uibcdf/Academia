# Manifiesto

El propósito de este repositorio es acumular material didáctico que cualquier estudiante o
investigador pueda usar para comenzar de manera autónoma a adquirir las habilidades necesarias
para el trabajo, en colaboración o como miembro, en la UIBCDF. En ningún caso se puede entender este 
repositorio como una guía completa de cada uno de los temas que presentan. Este repositorio es un punto de partida.

Si eres una persona ajena a la UIBCDF y estás aquí por algún otro motivo, eres bienvenido a hacer uso de esta documentación y contribuir en su desarrollo.

Inicialmente el material se desarrollará en español para hacerlo más accesible dado el contexto de la UIBCDF y los potenciales usuarios. De esta manera facilitamos que cualquier estudiante, independientemente de sus conocimientos de inglés, se atreva a participar y contribuir de una manera activa.

El formato debe estar en la medida de lo posible basado en jupyter notebooks. Se requiere entonces la instalación de ciertas herramientas en tu computadora, además de unos conocimientos mínimos para su uso:

- Mínimo conocimiento de lo que es GitHub.
- Mínimo conocimiento de Python 3.
- Instalación de un gestor de entornos de Python 3 como Conda.
- Instalación de Jupyter lab o Jupyter notebook en la computadora personal.
- Instalación de un mínimo de librerías de Python junto con un interpretador de Python 3.

Estos requisitos, para que el material sea autoconsistente, definen los contenidos de las primeras unidades.
Tras estas unidades iniciales, comenzaremos con conceptos básicos de programación en Python y veremos herramientas y librerias comunes para el investigador.
Una vez cubierta la exposición de los elementos generales que debemos conocer para 
trabajar, seguiremos con el material más específico en el marco de la simulación de dinámica
molecular y su aplicación al diseño racional de ligandos.
Si perteneces a la UIBCDF o vas a colaborar con nosotros, como penúltimo bloque encontrarás la
descripción de nuestro flujo de trabajo guiado por por criterios de Ciencia Abierta (OpenScience).
El último bloque es un glosario de las librerias más especificas de utilidad en nuestros proyectos. En este caso, la función de estos notebooks no sería pedagógica, sino documental en cuanto a sugerencias y modos de uso en la unidad.

Para hacer que el desarrollo de este material sea más flexible, su estructura no será indexada de manera numerada (temas, subtemas, subsubtemas, etc.).

# Cómo debe usarse este repositorio

La documentación aquí presente asume que tienes conocimientos básicos en el uso del sistema
operativo con el que trabajas: mac, windows o preferiblemente linux. Si esto no es cierto porque estás comenzando a usar Unix (Linux o MacOS), puedes encontrar algo de ayuda en las siguientes páginas: [La terminal de Unix de SoftwareCarpentry](http://swcarpentry.github.io/shell-novice-es/) o [su versión en inglés](http://swcarpentry.github.io/shell-novice/).

Como usuario/a de este repositorio, este es el acercamiento que te recomendamos:

- Si no sabes qué es Python, GitHub, Conda o Jupyter, échale antes que nada un vistazo al primer bloque de unidades haciendo uso del navegador y GitHub.
- [Clona en local el repositorio.](https://help.github.com/articles/cloning-a-repository/)
- Ejecuta y abre desde jupyter los notebooks en el orden que prefieras.
- Interacciona con tu copia local del material como te parezca: edita, modifica, juega, etc.
- Si tienes alguna duda o sugerencia cuelga un post en [el panel del repositorio](https://github.com/uibcdf/Academia/issues).

Si quieres además contribuir con nuevos notebooks o con modificaciones al material:

- Aprende cómo hacer "commit" y "push requests" de tus modificaciones o implementaciones. Las
  revisaremos y aceptaremos los cambios a la brevedad.
- Propón modificaciones y comunica sugerencias en [el panel del repositorio](https://github.com/uibcdf/Academia/issues).

# Tabla de contenidos

## Introducción para comenzar

- [Qué es este repositorio y cómo se usa.](Introducción/Academia.ipynb)  
- [Qué es Git, cómo se instala y cómo se usa.](Introducción/Git.ipynb)       
- [Qué es GitHub y cómo se usa.](Introducción/GitHub.ipynb)     
- [Qué es Python, cómo se instala y cómo se usa.](Introducción/Python.ipynb)  
- [Qué es Conda, cómo se instala y cómo se usa.](Introducción/Conda.ipynb)  
- [Qué es Jupyter, cómo se instala y cómo se usa.](Introducción/Jupyter.ipynb)  
- [Qué es Markdown y cómo se usa.](Introducción/Markdown.ipynb)
- [Ejercicio Resumen: Cómo jugar con este repositorio en tu máquina.](Introducción/Resumen.ipynb) [Próximamente]    

## Breve guia de programación básica en Python.  

- [Programando en Python.](Python/Python.ipynb)    
- Algebra con Numpy. [Próximamente]    
- Manejo estadístico de datos con Scipy. [Próximamente]    
- Manejo estadístico de datos con Pandas. [Próximamente]    
- Manejo estadístico de datos con Scikit-learn. [Próximamente]    
- Representación gráfica de datos con Matplotlib. [Próximamente]    
- Representación gráfica de datos con Seaborn. [Próximamente]    


## El sistema biomolecular y la simulación de dinámica molecular.

### El sistema biomolecular

- [Interactuando por primera vez con una proteína.](https://github.com/uibcdf/Academia/blob/master/2.10-%20Interactuando%20por%20primera%20vez%20con%20una%20prote%C3%ADna.ipynb)  
- Interactuando por primera vez con una trayectoria. [Próximamente]    
  
###  La simulación de dinámica molecular.
- Campos de fuerza [Próximamente]    
- Termostatos [Próximamente]    
- Integradores [Próximamente]    
- ... [Próximamente]    
- La simulación de dinámica molecular con OpenMM. [Próximamente]     
- La simulación de dinámica molecular con Gromacs. [Próximamente]    
- Simulaciones fuerza bruta para futura referencia. [Próximamente]    

### Sampleado termodinámico. 
- Introducción al REMD. [Próximamente]    
- Mis primeras simulaciones REMD. [Próximamente]    
- Introducción a Umbrella Sampling. [Próximamente]    
- Mis primeras simulaciones Umbrella Sampling. [Próximamente]    
- Introducción a Transition Path Sampling. [Próximamente]    

### Sampleado termodinámico y cinético.

## ...

## La UIBCDF
## El flujo de trabajo en la UIBCDF

- Open Science y la UIBCDF [Próximamente]    
- Qué es OSF y cómo se usa. [Próximamente]    
- Compartiendo herramientas computacionales. [Próximamente]    
- El trabajo de comunicación en forma de figuras, posters o manuscritos.[Próximamente]    
   - Edición de textos en LaTEX    
   - Qué es OverLeaf o ShareLatex y cómo se usa.    
   - Imagenes de Pymol.    
- Esquema de flujo de trabajo.  [Próximamente]    


## Glosario de librerias.

- UIBCDF Toolkit.  [Próximamente]    
- NGLview.  [Próximamente]    
- mdtraj. [Próximamente]    
- OpenMM. [Próximamente]     

# Agradecimientos

Gracias a todos aquellos que de alguna manera ayudan a que este material crezca y sea util. En
especial a [aquellos que por su colaboración activa pueden ser considerados autores](https://github.com/uibcdf/Academia/graphs/contributors).


