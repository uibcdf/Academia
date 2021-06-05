<p style="text-align:left;">
   <a href="../README.md">Ir al menú anterior</a>
   <span style="float:right;">
        <a href="../README.md">Ir a la unidad anterior</a>
   </span>
</p>

-----

<br>
<center>
<img src="http://jupyter.org/assets/main-logo.svg" width="200">
</center>
<br>

# Qué es Jupyter, cómo se instala y cómo se usa

<div class="alert alert-info" role="alert">
<strong>Info:</strong> Si crees que este notebook necesita algún cambio no dudes en <a href="../../../../UIBCDF-Academia/Como_contribuir/Como_contribuir.md" class="alert-link">contribuir a su desarrollo</a>.
</div>

<br>

Esta introducción a Jupyter está pensada para aquellos que tienen poco o ningún
conocimiento previo. Esperamos pueda serte útil.

- [¿Qué es Jupyter?](#¿Qué-es-Jupyter?)
   - [IPython](#IPython)
   - [Jupyter Notebook](#Jupyter-Notebook)
   - [JupyterLab](#JupyterLab)
- [¿Cómo se instala?](#¿Cómo-se-instala?)
- [¿Cómo se usa?](#¿Cómo-se-usa?)
- [Dudas, problemas técnicos y soluciones](#dudas)
- [Más recursos útiles](#recursos)
   - [Documentación](#documentacion)
   - [Tutoriales, Webinars y cursos gratuitos](#tutoriales)


## ¿Qué es Jupyter?

El reporte y documentación del desarrollo de un proyecto teórico computacional no cuenta con una tradición como en el caso del trabajo experimental de investigación. En este último caso llevamos generaciones desarrollando y puliendo la dinámica de trabajo en un laboratorio. Sabemos hacer cuadernos de bitácora para reportar el trabajo del día a día, redactamos y ponemos a disposición de todo usuario protocolos de uso de equipos experimentales, somos conscientes de que deben existir mecanismos de comunicación entre los investigadores, mecanismos de entrenamiento, registros y guías para el nuevo personal del laboratorio. Así, en todo laboratorio experimental, existe una documentación ordenada que entre otras cosas da cuenta de los experimentos realizados y resultados obtenidos para un proyecto. Por contra, en el caso de un laboratorio computacional no contamos con tantas décadas de tradición en la profesión como para disponer de una óptima cultura de trabajo. Recien la estamos inventando sobre la marcha. 

No hace muchos años era habitual que un investigador acumulara de manera desordenada en su disco duro cientos de programas, scripts de análisis, ficheros de datos, figuras, documentos de texto intentando reportar resultados, etc. La facilidad con la que se generan nuevos datos y resultados que reportar, y el volumen que estos ocupan, es mayor que en un laboratorio experimental común. De la misma manera, el desorden se incrementa rápidamente y la dificultad para mantener un cuaderno de bitácora "de papel" ordenado es alta.

En el día a día del investigador que necesitaba programar a cualquier nivel, el desarrollo de lenguages interpretados permitieron con alivio el abandono de Fortran o C para las tareas menos demandantes. El uso de Python (o R o Perl) fueron ganando adeptos por la sencillez del código en su escritura y lectura, y por que, dícho sea de paso con honestidad, el programa y el código eran el mismo fichero (era habitual compilar un programa, usarlo, y despistar el código). Por lo mismo, compartir con colegas código bien documentado se hizo más sencillo, incrementando la cantidad de investigadores "no expertos en programación" con la posibilidad de hacer y mantener código modular en colaboración.
Esta facilidad todavía generaba más necesidad de mantener un orden en el relato de la elaboración de scripts de análisis, uso de programas, y tratamiento de datos. Sin embargo, este problema aparecía ya bien resuelto en el uso de software comercial específico como [Mathematica de Wolfram](http://www.wolfram.com/mathematica/), que permitía combinar operaciones matemáticas con la visualización de su resultado en forma aritmética o de gráficas, de manera ordenada y secuencial; y guardar su registro en un fichero visualizable y operable en forma de libreta (notebook).

### IPython

El primera evolución con impacto en la manera de trabajar en ciencia (de manera popular, "*de uso libre*") llegó en 2001 con el desarrollo de [IPython -Interactive Computing with Python-](https://ipython.org/), impulsado por el físico colombiano [Dr. Fernando Pérez](https://en.wikipedia.org/wiki/Fernando_P%C3%A9rez_(software_developer)). IPython era una versión de interpretador de Python un poco más sofisticado que el que usabamos todos: era de verdad interactivo. Era posible con IPython abrir una consola y programar al vuelo, sin necesidad de documento de texto, un algoritmo sencillo de análisis. Poco a poco fue tomando forma el concepto de libreto o libro de notas visualizable y editable por IPython. Editores como Vim o Emacs, acoplaban en su maquinaria IPython para poder visualizar su libro de notas: un registro secuencial de código, resultado de código, gráficas y comentarios. Quizá no era la primera vez que se llegaba a este formato de trabajo, ya se mencionó más arriba el caso de Mathemática, pero al ser de uso libre fue la primera vez que se popularizó democratizando su uso. Actualmente este proyecto sigue vigente como [herramienta independiente](https://ipython.org/), y como nucleo de lo que vino más tarde: Jupyter.
Merece la pena leer [un comentario retrospectivo del mismo Dr. Fernando Pérez publicado en su blog en 2012 a propósito del desarrollo de IPython] (http://blog.fperez.org/2012/01/ipython-notebook-historical.html).

### Jupyter Notebook

La segunda evolución fue el salto de IPython a Jupyter Notebook, también ideado por el Dr. Fernando Pérez. Quizá la necesidad de que ese libreto de IPython que combinaba código, resultados y texto, fuera más exportable, compartible y social, hizo que el notebook mutara a un formato interpretable por cualquier navegador de páginas web. El formato notebook se introdujo en 2011 y en 2015 adoptó su forma "servible como web": Jupyter. Hoy puedes ver [numerosos ejemplos de jupyter notebooks](http://nbviewer.jupyter.org/) para entender el concepto que en palabras podría explicarse como el verdadero libro digital interactivo para el científico (mira por ejemplo proyectos como [Probabilistic Programming
and Bayesian Methods for Hackers](http://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter1_Introduction/Ch1_Introduction_PyMC3.ipynb) o [Mining the Social Web](http://nbviewer.jupyter.org/github/ptwobrussell/Mining-the-Social-Web-2nd-Edition/tree/master/ipynb/).)

Además, el jupyter notebook no sólo se puede visualizar en su forma original (una secuencia de celdas de código o texto) sino que permite ser transformado rápidamente a [una presentación interactiva en slides](https://rise.readthedocs.io/en/docs_hot_fixes/) -gracias al proyecto RISE iniciado por el argentino [Damian Ávila](https://github.com/damianavila)- o como documento pdf, Latex, etc.

### JupyterLab

La tercera evolución, ya de la mano del [consejo de Jupyter](https://jupyter.org/about) y de un elevado número de usuarios que han tenido la posibilidad de [participar en el desarrollo del jupyter notebook como proyecto de software libre y colaborativo](https://github.com/jupyter/notebook), dio respuesta a la integración del numeroso universo de iniciativas periféricas que estaban centradas en el uso del jupyter notebook: el Jupyter Lab. En febrero de 2018 se libera la primera versión estable de Jupyter Lab, un servidor web que envuelve el navegador y editor de Jupyter Notebooks permitiendo la inclusión de [widgets](http://jupyter.org/widgets￼) y [extensiones](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator) como para erigirse como un laboratorio computacional en formato web que integra la programación, la edición y visualización de un gran número de formatos de ficheros, el reporte en jupyter notebooks, el uso de terminales bash para interaccionar con la computadora o la implementación de [nuevas extensiones](https://medium.com/@subpath/jupyter-lab-extensions-for-data-scientist-e0d97d529fc1) como [la integración con GitHub](https://github.com/jupyterlab/jupyterlab-github) o [la integración con Google Drive](https://github.com/jupyterlab/jupyterlab-google-drive). Un laboratorio que puedes probar de manera remota antes de instalar en [jupyter.org/try](https://jupyter.org/try).

En definitiva, Jupyter Lab es ahora mismo el mejor formato de uso libre que nos permite ordenar el desarrollo de la parte computacional de un proyecto científico en un reporte interactivo. Nos ofrece además un soporte interactivo como para generar documentación y material de formación que ofrecer facilmente. Y además se ha convertido en uno de los proyectos de desarrollo libre más exitoso y bonito, demostrando que el trabajo transparente y cooperativo permite aunar el esfuerzo de muchos empujando iniciativas eficiente y rápidamente.

## ¿Cómo se instala?

Como buen proyecto cooperativo, Jupyter está bien documentado. Si tienes nociones de python y conda te resultará facil instalar Jupyter Lab y Jupyter Notebook haciendo uso del comando:

```bash
conda install -c conda-forge jupyterlab
```

Si usas otro gestor de entornos puedes encontrar ayuda sobre el proceso de instalación en la documentación oficial disponible:

http://jupyter.org/install
https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
http://jupyter.org/documentation

## ¿Cómo se usa?

Tanto Jupyter Notebook como Jupyter Lab se operan a través de tu navegador habitual de páginas web.

Abre una terminal y ejecuta:

```bash
jupyter lab
```

o

```bash
jupyter notebook
```

Con cualquiera de los dos comandos se activará un servidor cuyos mensajes dando cuenta de su operatividad se harán dueños de la terminal, y una nueva ventana o pestaña de tu navegador se abrirá mostrando la interfaz operativa de jupyter en formato clásico de notebook o el nuevo lab. 

El uso de ambos formatos es intuitivo en un primer momento. Para conocer un poco más de sus funcionalidades te invitamos a visitar las webs de documentación listadas al final de este documento o al mismo [notebook interactivo introductorio de ipython y jupyter](https://mybinder.org/v2/gh/ipython/ipython-in-depth/master?filepath=binder/Index.ipynb).

---

## Dudas, problemas técnicos y soluciones. <a class="anchor" id="dudas"></a>

Para centralizar esas dudas técnicas sobre el tema de esta unidad o proponer soluciones o sugerencias más técnicas que queremos encontrar en el futuro comentadas y visibles para todos, haz uso del siguiente canal:

[Foro Técnico: Jupyter](https://github.com/uibcdf/Academia/issues/6)

## Más recursos útiles <a class="anchor" id="recursos"></a>

El propósito de esta unidad es ser un documento únicamente introductorio. Puedes encontrar -o contribuir añadiendo- más información útil en el siguiente listado.

### Documentación <a class="anchor" id="documentacion"></a>

http://jupyter.org/    
http://jupyter.org/documentation    
https://jupyterlab.readthedocs.io/en/stable/    
https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html    
https://jupyter-notebook.readthedocs.io/en/latest/    
https://www.datacamp.com/community/blog/ipython-jupyter    
https://medium.com/@brianray_7981/jupyterlab-first-impressions-e6d70d8a175d    
https://medium.com/@subpath/jupyter-lab-extensions-for-data-scientist-e0d97d529fc1   
https://www.slideshare.net/jileon/introduccion-a-jupyter-antes-i-python-notebook    
https://github.com/damianavila/Python-Cientifico-HCC/blob/master/2_IPython.ipynb    

### Tutoriales, Webinars y cursos gratuitos <a class="anchor" id="tutoriales"></a>

https://www.dataquest.io/blog/jupyter-notebook-tutorial/    
https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook    
https://www.adictosaltrabajo.com/2018/01/18/primeros-pasos-con-jupyter-notebook/   
https://github.com/jupyterlab/jupytercon-jupyterlab-training
https://github.com/jupyterlab/jupyterlab-demo
https://github.com/jupyterlab/jupytercon-jupyterlab-tutorial
https://github.com/jupyterlab/jupyterlab-media

<br>

<div style='text-align: right;'> <a href="../Servidores/Servidores.md">Ir a la siguiente unidad</a> </div>

-------
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/uibcdf/Academia">UIBCDF-Academia</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/uibcdf/Academia/graphs/contributors">UIBCDF Lab, autores y colaboradores</a> es material protegido bajo una licencia <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

