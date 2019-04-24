[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

**[Manifiesto](#Manifiesto)** |
**[Instrucciones de uso](#Cómo-se-usa)** |
**[Tabla de Contenidos](#Tabla-de-contenidos)** |
**[Licencia](#Licencia)** |
**[Agradecimientos](#Agradecimientos)**

# Manifiesto

El propósito de este repositorio es acumular material didáctico que cualquier estudiante o
investigador pueda usar para comenzar de manera autónoma a adquirir las habilidades necesarias
para el trabajo, en colaboración o como miembro, en la UIBCDF. En ningún caso se puede entender este 
repositorio como una guía completa de cada uno de los temas que presentan. Este repositorio es un punto de partida.

Si eres una persona ajena a la UIBCDF y estás aquí por algún otro motivo, eres bienvenido a hacer uso de esta documentación y contribuir en su desarrollo. Esperamos que, si lo necesitas, interactues en [el panel de problemas](https://github.com/uibcdf/Academia/issues) sin ninguna reticencia.

Inicialmente el material se desarrollará en español para hacerlo más accesible dado el contexto de la UIBCDF y los potenciales usuarios. De esta manera facilitamos que cualquier estudiante, independientemente de sus conocimientos de inglés, se atreva a participar y contribuir de una manera activa.

El formato debe estar en la medida de lo posible basado en jupyter notebooks. Se requiere entonces la instalación de ciertas herramientas en tu computadora, además de unos conocimientos mínimos para su uso:

- Mínimo conocimiento del sistema operativo de tu computadora.
- Mínimo conocimiento de lo que es Git y GitHub.
- Mínimo conocimiento de Python 3.
- Instalación de un gestor de entornos de Python 3 como Conda.
- Instalación de Jupyter lab o Jupyter notebook en la computadora personal.
- Instalación de un mínimo de librerías de Python junto con un interpretador de Python 3.

Estos requisitos, para que el material sea autoconsistente, definen los contenidos de la primera sección de unidades didácticas: ["Introducción para comenzar."](#Introduccion).
Tras estas unidades iniciales, comenzaremos con [conceptos básicos de programación en Python y veremos herramientas y librerias comunes para el investigador](#Python).
Una vez cubierta la exposición de los elementos generales que debemos conocer para 
trabajar, seguiremos con el material más específico en el marco de la simulación de dinámica
molecular y su aplicación al diseño racional de ligandos.
Si perteneces a la UIBCDF o vas a colaborar con nosotros, como penúltimo bloque encontrarás la
descripción de [nuestro flujo de trabajo](#Flujo_UIBCDF) guíado por criterios de Ciencia Abierta (OpenScience).
El último bloque es un [glosario de las librerías más especificas de utilidad en nuestros proyectos](#Glosario). En este caso, la función de estos notebooks no es pedagógica, sino documental. Allí puedes encontrar las referencias útiles para su instalación e instrucciones uso.

Por último, es pertinente añadir que para hacer que el desarrollo de este material sea más flexible, su estructura no será indexada de manera numerada.

# Instrucciones de uso

La documentación aquí presente asume que tienes conocimientos básicos en el uso del sistema
operativo con el que trabajas si es MacOS o Windows. En el caso del sistema operativo Linux, dado que queremos invitarte a usarlo, suponemos que no tienes experiencia en su uso e instalación. Es por eso que dedicamos [la primera unidad a Linux](Introducción/Linux.ipynb).

Si sabes bien como trabajar en Linux o si seguirás con MacOS o Windows, empieza entonces revisando el resto de unidades de la sección ["Introducción para comenzar."](#Introduccion). Esta sección está escrita para asegurarnos, antes de seguir con el resto del material, de que conoces mínimamente las herramientas con las que vamos a trabajar y las tienes instaladas o configuradas.

La última unidad de la ["Introducción para comenzar."](#Introduccion) es quizá la que tienes que revisar con más detalle para conocer [cómo usar este repositorio](Introducción/Academia.ipynb). En ella, suponiendo que empiezas de cero, se dan instrucciones desde cómo instalar git en tu computadora a como proponer cambios o añadir material, pasando obviamente por cómo usar los notebooks con Jupyter localmente en tu computadora.

Te animamos a jugar con los notebooks: ejecútalos, modifícalos, reprograma el código de sus celdas, añade más celdas para probar cosas nuevas. Comparte este material con quien tu quieras y siéntete en confianza para contribuir con dudas, problemas, sugerencias o soluciones en [el panel de este repositorio en GitHub](https://github.com/uibcdf/Academia/issues).

### Recomendación final

La mejor actitud que debes tener para comenzar a ser un científico computólogo se resume perfectamente en la siguiente ilustración de xkcd:

<img src="https://imgs.xkcd.com/comics/tech_support_cheat_sheet.png" width="500">

Al margen de la broma, perder el miedo, tener curiosidad y saber que gracias a internet es muy facil ser autodidacta, son los mejores consejos que te pueden dar. Una vez alcanzado un nivel básico, es momento de estudiar los detalles con dedicación y profesionalidad. Pero eso ya es tarea tuya.

¡Ánimo!

# Tabla de contenidos.

## Introducción para comenzar. <a class="anchor" id="Introduccion"></a>

- [Introducción a Linux.](Introducción/Linux.ipynb)
- [Qué es Git, cómo se instala y cómo se usa.](Introducción/Git.ipynb)       
- [Qué es GitHub y cómo se usa.](Introducción/GitHub.ipynb)     
- [Qué es Python, cómo se instala y cómo se usa.](Introducción/Python.ipynb)  
- [Qué es Conda, cómo se instala y cómo se usa.](Introducción/Conda.ipynb)  
- [Qué es Jupyter, cómo se instala y cómo se usa.](Introducción/Jupyter.ipynb)  
- [Qué es Markdown y cómo se usa.](Introducción/Markdown.ipynb)
- [Qué es CUDA y cómo se instala.](Introducción/CUDA.ipynb)
- [Cómo usar este repositorio.](Introducción/Academia.ipynb)  

## Breve guía de programación básica en Python. <a class="anchor" id="Python"></a>

- [Programando en Python.](Python/Python.ipynb)    
- [Vectores, matrices y cálculo con Numpy.](Python/NumPy.ipynb)    
- [Representación gráfica de datos con Matplotlib.](Python/Matplotlib.ipynb)   
- Manejo estadístico de datos con Scipy. [Próximamente]    
- Manejo estadístico de datos con Pandas. [Próximamente]    
- Manejo estadístico de datos con Scikit-learn. [Próximamente]    
- Manejo estadístico de datos con Statmodels. [Próximamente]    
- Representación gráfica de datos con Seaborn. [Próximamente]    
- Representación gráfica de datos con Bokeh. [Próximamente]   


## El sistema biomolecular y la simulación de dinámica molecular.

### El sistema biomolecular

- [Interactuando por primera vez con una proteína.](Sistema_Biomolecular/una_proteína.ipynb)  
- Interactuando por primera vez con una trayectoria. [Próximamente]    
  
###  Teoría de dinámica molecular.
- Campos de fuerza [Próximamente]    
- Termostatos [Próximamente]    
- Integradores [Próximamente]

### Programas para simular la dinámica molecular
- OpenMM. [Próximamente]     
- Gromacs. [Próximamente]  

### Ejemplos de simulaciones con OpenMM
- [La partícula libre.](Dinámica_Molecular/Partícula_Libre.ipynb)    
- [El potencial harmónico](Dinámica_Molecular/Pozo_Harmónico.ipynb)
- [Un potencial doble pozo 1D.](Dinámica_Molecular/Doble_Pozo.ipynb)
- [Un potencial multipozo 1D.](Dinámica_Molecular/Multipozo_1D.ipynb)
- [Un potencial triple pozo 2D.](Dinámica_Molecular/Triple_Pozo_2D.ipynb)
- [Un potencial tipo embudo 2D.](Dinámica_Molecular/Embudo_2D.ipynb)
- [Un potencial tipo embudo 3D.](Dinámica_Molecular/Embudo_3D.ipynb)
- [Dialanina.](Dinámica_Molecular/DiAlanina.ipynb)
- [Met-encefalina.](Dinámica_Molecular/MetEncefalina.ipynb)
- [Trp-Cage.](Dinámica_Molecular/TrpCage.ipynb)

### Sampleado termodinámico. 
- Introducción al REMD. [Próximamente]    
- Mis primeras simulaciones REMD. [Próximamente]    
- Introducción a Umbrella Sampling. [Próximamente]    
- Mis primeras simulaciones Umbrella Sampling. [Próximamente]    
- Introducción a Transition Path Sampling. [Próximamente]    

### Sampleado termodinámico y cinético.

## ...

## El flujo de trabajo en la UIBCDF. <a class="anchor" id="Flujo_UIBCDF"></a>

### Principios Generales

- Open Science y la UIBCDF [Próximamente]    
- Esquema de flujo de trabajo.  [Próximamente]    

### Reproducibilidad y Transparencia

- Qué es OSF y cómo se usa. [Próximamente]    
- Compartiendo herramientas computacionales. [Próximamente]    

### Desarrollo de un proyecto

### Comunicación de resultados

- El trabajo de comunicación en forma de figuras, posters o manuscritos.[Próximamente]    
   - Edición de textos en LaTEX    
   - Qué es OverLeaf o ShareLatex y cómo se usa.    
   - Imagenes de Pymol.    

## Recursos Computacionales

### Ixtlilton

- Descripción.
- Uso.

### Tlaloc

- Descripción.
- Uso.

## Recursos Experimentales

### ITC

## Glosario de librerias. <a class="anchor" id="Glosario"></a>

- [Mayavi.](Glosario_librerias/Mayavi.ipynb)
- [MDAnalysis.](Glosario_librerias/MDAnalysis.ipynb)
- [MDTraj.](Glosario_librerias/MDTraj.ipynb)
- [Modeller.](Glosario_librerias/Modeller.ipynb)
- [MolModMT.](Glosario_librerias/MolModMT.ipynb)
- [NGLView.](Glosario_librerias/NGLView.md)
- [OpenMM.](Glosario_librerias/OpenMM.ipynb)
- [OpenMMTools.](Glosario_librerias/OpenMMTools.ipynb)
- [PDBFixer.](Glosario_librerias/PDBFixer.ipynb)
- [Pytraj.](Glosario_librerias/Pytraj.ipynb)
- [YANK.](Glosario_librerias/YANK.ipynb)

# Licencia

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">UIBCDF-Academia</span> es material protegido bajo una licencia <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International</a>.<br />Con fuente original en <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/uibcdf/Academia" rel="dct:source">https://github.com/uibcdf/Academia</a>.

# Agradecimientos

Gracias a todos aquellos que de alguna manera ayudan a que este material crezca y sea util. En
especial a [aquellos que por su colaboración activa pueden ser considerados autores](https://github.com/uibcdf/Academia/graphs/contributors).

Gracias también a los autores de la documentación y tutoriales citados en este repositorio. Gracias a los colegas que desarrollan las librerías y software que aquí se usan. Y gracisa también a [xkcd (Randall Munroe)](https://www.xkcd.com/) por hacer geniales ilustraciones sobre programación y ciencia, entre otras cosas, y permitir compartirlas libremente.
