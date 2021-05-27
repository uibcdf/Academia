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

## Qué es UIBCDF-Academia y cómo se usa. [50%]

- [Qué es UIBCDF-Academia.](academia/UIBCDF-Academia/Qué_es_UIBCDF-Academia.md) [0%]
- [Cómo usar UIBCDF-Academia.](academia/UIBCDF-Academia/Cómo_usar_UIBCDF-Academia.md) [100%]?

## El laboratorio computacional de investigación. [0%]

- El fraude y la conducta científica inapropiada. [0%]
- Publish or perish: sobreproducción de comunicaciones científicas no siempre relevantes. [0%]
- ¿Es la ciencia democrática? El peer-review. [0%]
- Open Science: transparente, reproducible, compartible. [0%]
- El laboratorio computacional de investigación. [0%]

### Desarrollo de un proyecto de investigación transparente y reproducible. [0%]

- Qué es OSF y cómo se usa. [0%]
- Menos scripts y más librerías y módulos. [0%]
- Cómo compartir las librerías y módulos: GitHub o GitLab. [0%]
- Cómo compartir los datos crudos. [0%]
- Open Source y modalidades de licencias para datos, figuras y librerías. [0%]

### El trabajo en colaboración [0%]

- El foro y el registro de conversaciones: Slack. [0%]
- Las tareas: Trello, etc. [0%]
- Edición de textos en LaTEX: OverLeaf o ShareLatex. [0%]

### La comunicación pública de datos, procesos, resultados e ideas. [0%]

- La importancia de la comunicación: Open Access, los preprints y los live journals. [0%]
- La comunicación social: el twitter científico. [0%]
- La narrativa cientifica de las libretas interactivas: el notebook interactivo. [0%]
- Haz tus productos citables: el Digital Object Identification y Zenodo. [0%]
- Publicando y compartiendo datos. [0%]
- Publicando y compartiendo figuras: Figshare. [0%]
- Publicando y compartiendo presentaciones. [0%]
- Webinars, youtube, twitch... [0%]

## Herramientas fundamentales del laboratorio computacional. <a class="anchor" id="Introduccion"></a>

### El sistema operativo Linux [50%]
- [Introducción a Linux.](academia/Herramientas_computacionales/Linux/Linux.md) [100%]?
- [Algunas buenas prácticas al trabajar en Linux.](academia/Herramientas_computacionales/Linux/Buenas_prácticas.md) [0%]

### Python [?%]
- [Introducción a los lenguajes de programación.](academia/Herramientas_computacionales/Python/Lenguajes_de_programación.md) [0%]
- [Qué es Python, cómo se instala y cómo se usa.](academia/Herramientas_computacionales/Python/Python.md) [100%]
- [Programando en Python.](academia/Herramientas_computacionales/Python/Programando_en_Python.ipynb) [?%]
- [Vectores, matrices y cálculo con Numpy.](academia/Herramientas_computacionales/Python/NumPy.ipynb) [?%]
- [Representación gráfica de datos con Matplotlib.](academia/Herramientas_computacionales/Python/Matplotlib.ipynb) [?%]
- [Análisis de datos con Scipy.](academia/Herramientas_computacionales/Python/Scipy.ipynb) [?%]
- [Análisis de datos y series con Pandas.](academia/Herramientas_computacionales/Python/Pandas.ipynb) [?%]
- [Aprendizaje automático con Scikit-learn.](academia/Herramientas_computacionales/Python/Scikit-learn.ipynb) [?%]
- [Procesamiento de imágenes con Scikit-image.](academia/Herramientas_computacionales/Python/Scikit-image.ipynb) [?%]
- [Rentación gráfica de datos con Seaborn.](academia/Herramientas_computacionales/Python/Seaborn.ipynb) [?%]
- [Representación gráfica de datos con Bokeh.](academia/Herramientas_computacionales/Python/Bokeh.ipynb) [?%]

### Los gestores de microambientes y paquetes. [?%]
- [Qué es Conda, cómo se instala y cómo se usa.](academia/Herramientas_computacionales/Conda/Conda.md) [?%]

### La narrativa construida con texto, algoritmos, resultados y gráficas. [?%]
- [Qué es Jupyter, cómo se instala y cómo se usa.](academia/Herramientas_computacionales/La_narrativa/Jupyter.md) [?%]
- Publicando y compartiendo en linea tus jupyter notebooks: Binder. [0%]
- Tu jupyter notebook como soporte para una comunicación oral. [0%]
- Tu jupyter notebook como documento latex o pdf. [0%]

### Lenguajes de marcado. [0%]
- Qué son los lenguages de marcado ligero de texto y cómo se usa. [0%]
	- [Qué es Markdown y cómo se usa.](academia/Herramientas_computacionales/Lenguajes_marcado/Markdown.md) [100%]
   	- [Qué es reStructuredText y Cómo se usa](academia/Herramientas_computacionales/Lenguajes_marcado/reStructuredText.md) [0%]
- Qué son los lenguages de marcado para la serialización de datos y cómo se usan. [0%]
	- Qué es JSON y cómo se usa. [0%]
	- Qué es XML y cómo se usa. [0%]
	- Qué es YAML y cómo se usa. [0%]

### El sistema de control de versiones distribuida. [?%]
- [Qué es Git, cómo se instala y cómo se usa.](academia/Herramientas_computacionales/Control_versiones_distribuida/Git.md) [?%]
- [Qué es GitHub y cómo se usa.](academia/Herramientas_computacionales/Control_versiones_distribuida/GitHub.md) [?%]

### La documentación de un proyecto de Python. [0%]
- [Qué es Sphinx y Cómo se usa](academia/Herramientas_computacionales/Documentación/Sphinx.md) [0%]
- Qué es Readmedoc y Cómo se usa [0%]

### La evaluación automática y la integración continua de un proyecto de Python. [0%]
- Qué es la integración continua. [0%]
- Qué es Travis CI y cómo se usa. [0%]

### La distribución y publicación de una librería de Python. [0%]
- Qué es Anaconda y cómo se usa. [0%]
- Haz tu proyecto citable: Zenodo. [0%]

### Caso práctico: un proyecto de librería en Python desde cero. [?%]

- [Creando un repositorio en GitHub para la nueva librería](academia/Herramientas_computacionales/Caso_práctico/Creando_GitHub_repo.md) [?%]
- [Creando una librería de Python](academia/Herramientas_computacionales/Caso_práctico/Creando_librería_Python.md) [?%]
- [Documentando una librería de Python](academia/Herramientas_computacionales/Caso_práctico/Documentando_librería_Python.md) [?%]
- [Testeo e integración continua de una librería de Python](academia/Herramientas_computacionales/Caso_práctico/Testeo_librería_Python.md) [?%]

### La computación en GPUs [?%]
- [Qué es CUDA y cómo se instala.](academia/Herramientas_computacionales/GPU/CUDA.md) [?%]
- La programación para GPUs. [?%]

### El cluster de computación intesiva [0%]
- Qué es un cluster de computación intensiva
- Qué es una supercomputadora de acceso público
	- La visión de un administrador y las políticas de usuario.
- Qué debe sabe un usuario de supercomputadora.
	- El sistema de ficheros de un usuario.
	- El gestor de entornos de módulos.
	- El gestor de colas y recursos.

## El modelo de un sistema molecular

- La partícula libre, el movimiento Browniano y la dinámica de Langevin.
- La fricción, la temperatura y la difusión. Fluctuación-disipación.


#### Por colocar
- [Interactuando por primera vez con un modelo.](Sistema_Biomolecular/una_proteína.ipynb)  
- [La partícula libre.](Ejemplos_de_simulaciones_de_MD/Particula_Libre.ipynb)    
- [El potencial harmónico](Ejemplos_de_simulaciones_de_MD/Pozo_Harmónico.ipynb)
- [Un potencial doble pozo 1D.](Ejemplos_de_simulaciones_de_MD/Doble_Pozo.ipynb)
- [Un potencial multipozo 1D.](Ejemplos_de_simulaciones_de_MD/Multipozo_1D.ipynb)
- [Un potencial triple pozo 2D.](Ejemplos_de_simulaciones_de_MD/Triple_Pozo_2D.ipynb)
- [Un potencial tipo embudo 2D.](Ejemplos_de_simulaciones_de_MD/Embudo_2D.ipynb)
- [Un potencial tipo embudo 3D.](Ejemplos_de_simulaciones_de_MD/Embudo_3D.ipynb)
- [Dialanina.](Ejemplos_de_simulaciones_de_MD/DiAlanina.ipynb)
- [Met-encefalina.](Ejemplos_de_simulaciones_de_MD/MetEncefalina.ipynb)
- [Trp-Cage.](Ejemplos_de_simulaciones_de_MD/TrpCage.ipynb)



### Técnicas de reducción de dimensionalidad.
- Las coordenadas de reacción.
- Los peligros de la reducción de dimensionalidad.
- El análisis de componentes principales.

### Las redes cinéticas y los modelos de estados de markov.

### Técnicas de sampleado conformacional.

### El cálculo de energía libre y las técnicas del sampleado termodinámico.
- Introducción al REMD. [Próximamente]    
- Mis primeras simulaciones REMD. [Próximamente]    
- Introducción a Umbrella Sampling. [Próximamente]    
- Mis primeras simulaciones Umbrella Sampling. [Próximamente]    
- Introducción a Transition Path Sampling. [Próximamente]    

### Sampleado cinético.
- Calculo de eventos raros

## El diseño racional de moléculas con potencial farmacológico.

- El modelo de datos estados: acoplado-desacoplado.
- La lucha entalpía vs. entropía: Kd y la energía libre de unión.
- Las implicaciones de la cinética: Kon y Koff.

- Farmacóforos
- Bolsillos y cavidades.
- La energía libre de unión absoluta y relativa.
 
##  La simulación de dinámica molecular.
- [Ruta de desarrollo de contenidos. -TEMPORAL-](Dinámica_Molecular/Ruta.md)
- Mecánica y dinámica clásica: Posición, Velocidad, Aceleración, Energía Potencial, Fuerza y Trabajo.
- Mecánica y dinámica clásica: Integradores.
- Mecánica y dinámica clásica: Determinismo, reversibilidad y conservación del volumen.
- Mecánica y dinámica clásica: El oscilador harmónico.
- Mecánica y dinámica clásica: Términos no lineales, sensibilidad a condiciones iniciales y caos.
- Mecánica y dinámica clásica: ¿Qué no es clásico?
- [Dinámica Estocástica: Movimiento Browniano.](Dinámica_Molecular/Teoría/Movimiento_Browniano.ipynb)
- Dinámica Estocástica: Temperatura y Difusión o Fluctuación-Disipación.
- Dinámica Estocástica: Dinámica de Langevin.
- Dinámica Estocástica: Integradores estocásticos.
- Dinámica Estocástica: Principio de equipartición de la energía.
- Dinámica Estocástica: Oscilador armónico y sistema Orstein-Uhlenbeck.
- Dinámica Estocástica: Limite termodinámico, Ensemble y reproducibilidad.
- Mecánica Estadística: Boltzmann.
- Mecánica Estadística: Entropía de Gibs e interpretación física y cotidiana.
- Mecánica Estadística: Principio de equipartición desde Boltzmann.
- Mecánica Estadística: Distribución de velocidades de Maxwell-Boltzmann.

## OpenMM

- Solvente Implicito.
- Notas.


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

- [Mayavi.](Glosario_librerias/Mayavi.md)
- [MDAnalysis.](Glosario_librerias/MDAnalysis.md)
- [MDTraj.](Glosario_librerias/MDTraj.md)
- [Modeller.](Glosario_librerias/Modeller.md)
- [MolModMT.](Glosario_librerias/MolModMT.md)
- [NGLView.](Glosario_librerias/NGLView.md)
- [OpenMM.](Glosario_librerias/OpenMM.md)
- [OpenMMTools.](Glosario_librerias/OpenMMTools.md)
- [PDBFixer.](Glosario_librerias/PDBFixer.md)
- [Pytraj.](Glosario_librerias/Pytraj.md)
- [YANK.](Glosario_librerias/YANK.md)

# Licencia

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">UIBCDF-Academia</span> es material protegido bajo una licencia <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International</a>.<br />Con fuente original en <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/uibcdf/Academia" rel="dct:source">https://github.com/uibcdf/Academia</a>.

# Agradecimientos

Gracias a todos aquellos que de alguna manera ayudan a que este material crezca y sea util. En
especial a [aquellos que por su colaboración activa pueden ser considerados autores](https://github.com/uibcdf/Academia/graphs/contributors).

Gracias también a los autores de la documentación y tutoriales citados en este repositorio. Gracias a los colegas que desarrollan las librerías y software que aquí se usan. Y gracisa también a [xkcd (Randall Munroe)](https://www.xkcd.com/) por hacer geniales ilustraciones sobre programación y ciencia, entre otras cosas, y permitir compartirlas libremente.
