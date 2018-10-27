# Manifiesto

El propósito de este repositorio es acumular material didáctico que cualquier estudiante o
investigador pueda usar para comenzar de manera autónoma a adquirir las habilidades necesarias
para el trabajo en colaboración o como miembro de la UIBCDF. No se trata de una guía completa en cada uno de los temas que presenta, sino de una introducción.

Si eres una persona ajena a la UIBCDF y estás aquí por algún otro motivo, eres bienvenido a hacer uso de esta documentación y contribuir
en su desarrollo si la encuentras de utilidad.

Inicialmente el material se desarrollará en español para hacerlo más accesible y de evoluación más
rápida dado el contexto de la unidad y los potenciales usuarios.

El formato debe estar en la medida de lo posible basado en jupyter notebooks.
Es por esto que se requieren unos conocimientos mínimos para aprovechar este material:

- mínimo conocimiento de lo que es github
- instalación de un gestor de entornos de Python 3 como pueda ser pip o conda
- instalación de un mínimo de librerías de Python junto con un interpretador de Python 3
- instalación de jupyter lab o jupyter notebook en la computadora personal

Estos requisitos definen los primeros contenidos a cubrir:

- Introducción para comenzar
	- Qué es este repositorio y cómo se usa.  
	- El flujo de trabajo de la UIBCDF.  
	[- Qué es Git, cómo se instala y cómo se usa.](https://github.com/uibcdf/Academia/blob/master/0.10-%20Qu%C3%A9%20es%20git%2C%20c%C3%B3mo%20se%20instala%20y%20c%C3%B3mo%20se%20usa.ipynb)   
	[- Qué es GitHub y cómo se usa.](https://github.com/uibcdf/Academia/blob/master/0.20-%20Qu%C3%A9%20es%20GitHub%20y%20c%C3%B3mo%20se%20usa.ipynb)  
	- Qué es Python, cómo se instala y cómo se usa.  
	- Qué es Conda, cómo se instala y cómo se usa.  
	- Qué es Jupyter, cómo se instala y cómo se usa.  
	- Qué es OSF y cómo se usa.  

Tras estas unidades iniciales, comenzaremos con conceptos básicos de programación en Python y veremos herramientas y librerias comunes para el investigador:

- Breve guia de programación básica en Python.  
	- Breve guía de algebra con Numpy.
	- Breve guía de manejo estadístico de datos con Scipy.
	- Breve guía de manejo estadístico de datos con Pandas.
	- Breve guía de manejo estadístico de datos con Scikit-learn.  
	- Breve guía de representación gráfica de datos con Matplotlib.  
	- Breve guía de representación gráfica de datos con Seaborn.  

Comenzamos, ahora que ya conocemos las herramientas necesarias.

- El sistema biomolecular
	[- Interactuando por primera vez con una proteína.](https://github.com/uibcdf/Academia/blob/master/2.10-%20Interactuando%20por%20primera%20vez%20con%20una%20prote%C3%ADna.ipynb)  
	- Interactuando por primera vez con una trayectoria.
  
- La simulación de dinámica molecular.
	- Campos de fuerza
	- Termostatos
	- Integradores
	- ...
	- La simulación de dinámica molecular con OpenMM.  
	- La simulación de dinámica molecular con Gromacs. 
	- Simulaciones fuerza bruta para futura referencia.  

- Sampleado termodinámico. 
	- Introducción al REMD.  
	- Mis primeras simulaciones REMD.  
	- Introducción a Umbrella Sampling.  
	- Mis primeras simulaciones Umbrella Sampling.  
	- Introducción a Transition Path Sampling.

- Sampleado termodinámico y cinético.

...

El último bloque es un glosario de las librerias más especificas de utilidad en nuestros proyectos. Los siguientes notebooks están aquí como material de consulta y para centralizar nuestras dudas y sugerencias de uso.

X.00- UIBCDF Toolkit  
X.10- NGLview  
X.20- mdtraj  
X.30- OpenMM  



# Cómo debe usarse este repositorio

La documentación aquí presente asume que tienes conocimientos básicos en el uso de sistema
operativo con el que trabajas: mac, windows o preferiblemente linux.

Como usuario/a de este repositorio este es el acercamiento que te recomendamos:

- Si no sabes qué es GitHub, Python o Jupyter, echale antes que nada un vistazo al primer bloque de notebooks: 0.00, [0.10](https://github.com/uibcdf/Academia/blob/master/0.10-%20Qu%C3%A9%20es%20git%2C%20c%C3%B3mo%20se%20instala%20y%20c%C3%B3mo%20se%20usa.ipynb), [0.20](https://github.com/uibcdf/Academia/blob/master/0.20-%20Qu%C3%A9%20es%20GitHub%20y%20c%C3%B3mo%20se%20usa.ipynb), 0.30, 0.40, 0.50 y 0.60.
- [Clona en local el repositorio.](https://help.github.com/articles/cloning-a-repository/)
- Ejecuta y abre desde jupyter los notebooks en el orden que prefieras.
- Interacciona con tu copia local del material como te parezca: edita, modifica, juega, etc.
- Si tienes alguna duda o sugerencia cuelga un post en [el panel del repositorio](https://github.com/uibcdf/Academia/issues).

Si quieres además contribuir con nuevos notebooks o con modificaciones al material:

- Aprende cómo hacer "commit" y "push requests" de tus modificaciones o implementaciones. Las
  revisaremos y aceptaremos los cambios a la brevedad.
- Propón modificaciones y comunica sugerencias en [el panel del repositorio](https://github.com/uibcdf/Academia/issues).


