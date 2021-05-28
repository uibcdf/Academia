[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

# UIBCDF-Academia

**[Manifiesto](#Manifiesto)** |
**[Instrucciones de uso](#Cómo-se-usa)** |
**[Tabla de contenidos](#Tabla-de-contenidos)** |
**[Agradecimientos](#Agradecimientos)** |
**[Licencia](#Licencia)** 

## Manifiesto

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

## Instrucciones de uso

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

## Tabla de contenidos

[Ir a la tabla de contenidos](academia/README.md)

# Agradecimientos

Gracias a todos aquellos que de alguna manera ayudan a que este material crezca y sea util. En
especial a [aquellos que por su colaboración activa pueden ser considerados autores o colaboradores](https://github.com/uibcdf/Academia/graphs/contributors).

Gracias también a los autores de la documentación y tutoriales citados en este repositorio. Gracias a los colegas que desarrollan las librerías de código abierto y software libre que aquí se usan. Y gracias también a [xkcd (Randall Munroe)](https://www.xkcd.com/) por hacer geniales ilustraciones sobre programación y ciencia, entre otras cosas, y permitir compartirlas libremente.

# Licencia

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/uibcdf/Academia">UIBCDF-Academia</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/uibcdf/Academia/graphs/contributors">UIBCDF Lab, autores y colaboradores</a> es material protegido bajo una licencia <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

