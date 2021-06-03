[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/uibcdf/Academia/main?urlpath=lab)


# UIBCDF-Academia

**[Manifiesto](#Manifiesto)** |
**[Instrucciones de uso](#Instrucciones-de-uso)** |
**[Una recomendación final](#Una-recomendación-final)** |
**[Tabla de contenidos](#Tabla-de-contenidos)** |
**[Agradecimientos](#Agradecimientos)** |
**[Licencia](#Licencia)** 

## Manifiesto

El propósito de este repositorio es acumular material didáctico que cualquier estudiante o
investigador pueda usar para comenzar de manera autónoma a adquirir las habilidades necesarias
para el trabajo, en colaboración o como miembro, en la UIBCDF. En ningún caso se puede entender este 
repositorio como una guía completa de cada uno de los temas que se presentan. **Este repositorio es solamente un punto de partida**.

Si eres una persona ajena a la UIBCDF y estás aquí por algún otro motivo, eres bienvenido a hacer uso de esta documentación y contribuir en su desarrollo. Esperamos que, si lo necesitas, interactues en [el panel de problemas o questiones -*Issues Board*- del repositorio en GitHub](https://github.com/uibcdf/Academia/issues) sin ninguna reticencia.

Inicialmente el material se desarrollará en español para hacerlo más accesible dado el contexto de la UIBCDF y los potenciales usuarios. De esta manera facilitamos que cualquier estudiante, independientemente de sus conocimientos de inglés, se atreva a participar y contribuir de una manera activa.

El formato debe estar en la medida de lo posible basado en [ficheros Markdown](academia/Laboratorio_computacional/Herramientas/Lenguages_marcado/Markdown/Markdown.md) y [Jupyter notebooks](academia/Laboratorio_computacional/Herramientas/Jupyter/README.md). Se requiere entonces, para la contribución al desarrollo de este repositorio, la instalación de ciertas herramientas en tu computadora, además de unos conocimientos mínimos para su uso:

- Mínimo conocimiento del sistema operativo de tu computadora (preferentemente [Linux](academia/Laboratorio_computacional/Herramientas/Linux/README.md)).
- Mínimo conocimiento de lo que es [Git y GitHub](academia/Laboratorio_computacional/Herramientas/Control_versiones_distribuida/README.md).
- Mínimo conocimiento de [Python](academia/Laboratorio_computacional/Herramientas/Python/README.md).
- Instalación de un gestor de entornos de Python como [Conda](academia/Laboratorio_computacional/Herramientas/Conda/README.md).
- Instalación de [Jupyter lab o Jupyter notebook](academia/Laboratorio_computacional/Herramientas/Jupyter/README.md).
- Instalación de un mínimo de [librerías científicas de Python](academia/Laboratorio_computacional/Herramientas/Python/README.md).

Es por esto que, para que UIBCDF-Academia sea autoconsistente, [el primer](academia/UIBCDF-Academia/README.md) y [segundo](academia/Laboratorio_computacional/README.md) bloque de contenidos están dedicados al [uso de UIBCDF-Academia]() y a [la introducción del laboratorio computacional de investigación y sus herramientas](academia/Laboratorio_computacional/README.md) -algunas de las mismas son necesarias para sacarle todo el provecho posible a este repositorio-. Una vez cubierta la exposición de los elementos generales que debemos conocer para 
trabajar, seguiremos con el material más específico de [introducción a los conceptos físicos, químicos y biológicos para el trabajo de investigación en biología computacional y el diseño
racional de moléculas con potencial farmacológico](academia/README.md). Si perteneces a la UIBCDF o vas a colaborar con nosotros, como penúltimo bloque encontrarás la
descripción de [nuestro flujo de trabajo](academia/Flujo_trabajo/README.md) guíado por criterios de la Ciencia Abierta -*OpenScience*-.
El último bloque es un [glosario de las librerías científicas de utilidad en nuestros proyectos](academia/Glosario_librerias/README.md). En este caso, la función de estos notebooks no es pedagógica, sino documental. Allí puedes encontrar las referencias útiles para su instalación y uso, así como el enlace correspondiente al foro -en forma de cuestión abierta en el [*Issues Board* del repositorio en GitHub](https://github.com/uibcdf/Academia/issues)- para preguntas y comentarios técnicos.

Finalmente, es pertinente añadir que para hacer que el desarrollo de este material sea más flexible, su estructura no será indexada de manera numerada.

## Instrucciones de uso

[El primer bloque de contenido de UIBCDF-Academia](academia/UIBCDF-Academia/README.md) está dedicado a explicar [qué es UICDF-Academia](academia/UIBCDF-Academia/Que_es/Que_es.md), [cómo se usa](academia/UIBCDF-Academia/Como_se_usa/Como_se_usa.md) y [cómo puedes contribuir a su desarrollo](academia/UIBCDF-Academia/Como_contribuir/Como_contribuir.md). Pero no es necesario que lleguemos allí para encontrar unas primeras pautas sobre como comenzar a usarlo. Brevemente, puedes hacer uso de este repositorio de tres maneras distintas descritas a continuación.

### Únicamente quiero leer el contenido de UIBCDF-Academia

Si únicamente quieres leer el contenido de las unidades de UIBCDF-Academia, no debes hacer nada más
que navegar de manera guiada por los ficheros de este repositorio mediante [su web
en GitHub](https://github.com/uibcdf/Academia). No necesitas conocimientos específicos sobre ningún aspecto técnico. Tu puerta de entrada a dichas
unidades será el enlace que puedes encontrar en la sección [Tabla de
contenidos](#Tabla-de-contenidos) de este documento.

### Quiero interactuar con las unidades de UIBCDF-Academia con la ayuda de [Binder](https://mybinder.org/)

Existen unidades de UIBCDF-Academia en dos formatos: en formato [Markdown](academia/Laboratorio_computacional/Herramientas/Lenguages_marcado/Markdown/Markdown.md) -como es el caso de este
documento- o en formato [Jupyter notebook](academia/Laboratorio_computacional/Herramientas/Jupyter/README.md) -un formato interactivo-. Si quieres ir más allá de
simplemente acceder a la visualización de las unidades para su lectura, puedes, sin necesidad de
instalar ni configurar nada, interaccionar con este repositorio mediante a un servidor remoto de [Jupyter lab](academia/Laboratorio_computacional/Herramientas/Jupyter/README.md) ofrecido por [Binder](https://mybinder.org/). Debes saber que cualquier cambio que realices allí, no tendrá ningún impacto sobre este repositorio principal. Así que esta puede ser la manera perfecta para comenzar a jugar con las unidades de UIBCDF-Academia. Échale un ojo a [la sección correspondiente de la unidad "Cómo se usa UIBCDF-Academia"](academia/UIBCDF-Academia/Como_se_usa/Como_se_usa.md) o sigue al menos los tres siguientes pasos:

- Abre [este enlace que nos lleva al servidor de *mybinder* de este repositorio](https://mybinder.org/v2/gh/uibcdf/Academia/main?urlpath=lab) o hacer
  click en la insignia [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/uibcdf/Academia/main?urlpath=lab)
en la parte superior de este documento. Y deja
  que se cargue.
- Haz click con el botón derecho sobre el archivo "README.md" -barra
de archivos a la izquierda de la pantalla- y selecciona en el menú desplegado "Open With > Markdown Preview".
- Verás la copia de este documento en tu recien estrenado servidor remoto de [Jupyter
  lab](academia/Laboratorio_computacional/Herramientas/Jupyter/README.md) en
[Binder](https://mybinder.org/). Continua por allí su lectura, esa versión será a partir de ahora tu página
principal de UIBCDF-Academia.

### Quiero trabajar con mi propia copia local de UIBCDF-Academia

Eres atrevida o atrevido y quieres comenzar configurando tu propio entorno en el que interaccionar
tu copia local de UIBCDF-Academia. Enhorabuena por ese ímpetu. Te sugerimos entonces que saltes al
contenido apropiado para ti en la [sección extendida titulada "Cómo se usa UIBCDF-Academia"](academia/UIBCDF-Academia/Como_se_usa/Como_se_usa.md) del [primer bloque del contenido
de este repositorioi](academia/UIBCDF-Academia/README.md). Allí encontrarás todo lo necesario para configurar tu entorno virtual, clonar
UIBCDF-Academia e interaccionar con tu propia copia local.

#### Además quiero contribuir a desarrollar UIBCDF-Academia

Eres bienvenida o bienvenido a contribuir al desarrollo de este repositorio. Puede que quieras
hacer correcciones, implementar nuevo contenido, o simplemente contribuir con sugerencias. [Existe
una sección en el primer bloque del contenido de UIBCDF-Academia donde puedes encontrar las
indicaciones para hacerlo](academia/UIBCDF-Academia/Como_contribuir/Como_contribuir.md). Por favor, te invitamos a tener una participación activa. Desde el
primer ["Pull Request"](academia/UIBCDF-Academia/Como_contribuir/Como_contribuir.md) que realices, aparecerá tu nombre en [la lista de colaboradores a este
proyecto](https://github.com/uibcdf/Academia/graphs/contributors).

## Una recomendación final

La mejor actitud que debes tener para comenzar a ser un científico capaz de usar herramientas computacionales se resume perfectamente en la siguiente ilustración de [xkcd (Randall Munroe)](https://www.xkcd.com/):

<br>
<center>
<img src="https://imgs.xkcd.com/comics/tech_support_cheat_sheet.png" width="500">
</center>
<br>

Al margen de la broma, perder el miedo, tener curiosidad y saber que gracias a internet es muy facil ser autodidacta, son los mejores consejos que te pueden dar. Te invitamos a jugar con los notebooks: ejecútalos, modifícalos, reprograma el código de sus celdas, añade más celdas para probar cosas nuevas. Comparte este material con quien tu quieras y siéntete en confianza para contribuir con dudas, problemas, sugerencias o soluciones en [el panel de este repositorio en GitHub](https://github.com/uibcdf/Academia/issues). Una vez alcanzado un nivel básico, es momento de estudiar los detalles con dedicación y profesionalidad. Pero eso ya es tarea tuya.

¡Ánimo!

## Tabla de contenidos

Independientemente de [cómo vayas a usar UIBCDF-Academia](academia/UIBCDF-Academia/Como_se_usa/Como_se_usa.md), puedes acceder desde ahora mismo a la primera
tabla de contenidos de este repositorio. Recuerda, si lo estás haciendo desde [la web principal del
repositorio en GitHub](https://github.com/uibcdf/Academia) únicamente podrás visualizar su contenido. Si lo estás haciendo desde [Binder](https://mybinder.org/v2/gh/uibcdf/Academia/main?urlpath=lab) o desde [tu propia copia local](academia/UIBCDF-Academia/Como_se_usa/Como_se_usa.md), podrás interaccionar con él.

[Ir a la tabla de contenidos](academia/README.md)

# Agradecimientos

Gracias a todos aquellos que de alguna manera ayudan a que este material crezca y sea útil. En
especial a [aquellos que por su colaboración activa pueden ser considerados autores o colaboradores](https://github.com/uibcdf/Academia/graphs/contributors).

Gracias también a los autores de la documentación y tutoriales citados en este repositorio. Gracias a los colegas que desarrollan las librerías de código abierto y software libre que aquí se usan. Y gracias también a [xkcd (Randall Munroe)](https://www.xkcd.com/) por hacer geniales ilustraciones sobre programación y ciencia, entre otras cosas, y permitir compartirlas libremente.

# Licencia

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/uibcdf/Academia">UIBCDF-Academia</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/uibcdf/Academia/graphs/contributors">UIBCDF Lab, autores y colaboradores</a> es material protegido bajo una licencia <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

