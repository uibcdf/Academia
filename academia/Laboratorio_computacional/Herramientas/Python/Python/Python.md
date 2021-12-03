<p style="text-align:left;">
   <a href="../README.md">Ir al menú anterior</a>
   <span style="float:right;">
        <a href="../Lenguajes/Lenguajes.md">Ir a la unidad anterior</a>
   </span>
</p>

-----

<br>
<center><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="40%"></center>
<br>

# Qué es Python, cómo se instala y cómo se usa

<div class="alert alert-info" role="alert">
<strong>Info:</strong> Si crees que esta unidad necesita algún cambio no dudes en <a href="../../../../UIBCDF-Academia/Como_contribuir/Como_contribuir.md" class="alert-link">contribuir a su desarro
llo</a>.
</div>

<div class="alert alert-danger" role="alert">
<strong>En desarrollo:</strong> 80% porque falta una mejor introducción a la historia de Python y
una mejor descripción adecuada para la persona que se acerca a este lenguaje por primera vez.
</div>


<br>

- [¿Qué es Python?](#¿Qué-es-Python?)
   - [¿Python 2 o 3?](#¿Python-2-o-3?)
- [¿Cómo se instala?](#¿Cómo-se-instala?)
   - [En Linux](#En-Linux)
   - [En MacOS](#En-MacOS)
   - [En Windows](#En-Windows)
- [¿Cómo se usa?](#¿Cómo-se-usa?)
- [Dudas, problemas técnicos y soluciones](#dudas)
- [Más recursos útiles](#recursos)
    - [Documentación](#documentacion)
    - [Tutoriales, Webinars y cursos gratuitos](#tutoriales)

## ¿Qué es Python?

Python es un lenguaje de [programación interpretado](https://blog.makeitreal.camp/lenguajes-compilados-e-interpretados/) que en la última década se ha impuesto como uno de los más populares en ciencia por los siguientes motivos:

- Fácil de aprender en un nivel básico.
- Fácil de leer.
- Fácil de comentar, documentar y compartir.
- No es el lenguage más eficiente pero es de los primeros lenguages intepretados en ganar masa crítica (motivos históricos).
- Existe una gran oferta de librerías científicas auxiliares.
- Existe una gran comunidad de desarrolladores-usuarios.
- El consenso que se ha alcanzado en cuanto a su uso y conocimiento en nuestra comunidad.


Por esto y [otras razones](http://www.scipy-lectures.org/intro/intro.html#why-python) hoy día podemos justificar la elección de Python como primer lenguaje de trabajo en la UIBCDF.

Python, como todo lenguaje intepretado, no es computacionalmente eficiente para el cálculo intensivo. Para optimizar el costo en tiempo y memoria de un proceso, y hasta que lenguajes como [Rust](https://www.rust-lang.org/en-US/) se hagan más populares, programamos o hacemos uso de librerías escritas en [lenguages compilados](https://blog.makeitreal.camp/lenguajes-compilados-e-interpretados/) como Fortran o C, cuya operabilidad desde Python es posible gracias a protocolos como [F2PY](https://docs.scipy.org/doc/numpy/f2py/), [Cython](https://cython.org/) o [Ctypes](https://docs.python.org/3/library/ctypes.html).

En la UIBCDF somos conscientes de que existen otros lenguajes interpretados como Perl, Ruby o R. Animamos al lector a conocerlos, así como recomendamos aprender a programar en algún lenguage compilado como Fortran o C.

### ¿Python 2 o 3?

Python 2 fue declarado obsoleto el [1 de enero de 2020](https://www.python.org/dev/peps/pep-0373/). La duda de qué versión de Python debo usar, 2 o 3, no tiene sentido en la actualidad si queremos poder compartir y ejecutar el código en un futuro próximo. Empieza a usar Python 3.

## ¿Cómo se instala?

Por su popularidad y utilidad el interpretador de Python está seguramente instalado en tu sistema operativo Linux o MacOS. No obstante compartimos a continuación páginas web que te pueden ayudar a instalar Python en tu sistema operativo.

### En Linux

- Instalación según [RealPython blog](https://realpython.com/installing-python/#linux)
- Instalación según [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/starting/install3/linux/#install3-linux)

### En MacOS

- Instalación según [RealPython blog](https://realpython.com/installing-python/#macos-mac-os-x)
- Instalación según [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/starting/install3/osx/)

### En Windows

- Instalación según [RealPython blog](https://realpython.com/installing-python/#windows)
- Instalación según [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/starting/install3/win/)

## ¿Cómo se usa?

Para programar únicamente necesitamos un editor de texto. Y para ejecutar el programa basta con tener el [interpretador o compilador](https://blog.makeitreal.camp/lenguajes-compilados-e-interpretados/) correspondiente al lenguaje que estamos usando.

Con el editor creamos un fichero de texto plano que contenga la secuencia de órdenes a ejecutar, el programa. Por ejemplo, imagina que creas el fichero 'hola.txt' con la siguiente linea:

```python
print("hola!")
```

El interpretador lo puedes entender como el software que leerá tu texto y lo ejecutará traduciéndolo, en ese mismo momento, a lenguaje máquina. En el caso anterior, invocando el comando `python` y ofreciendole como argumento el fichero 'hola.txt':

```bash
python hola.txt
```

Veremos que el resultado será la impresión en pantalla:

```
hola!
```

<div class="alert alert-info" role="alert">
<strong>Sugerencia:</strong> Para comenzar a aprender a programar en Python te sugerimos que despues de terminar esta unidad continues con la siguiente titulada <a href='../Programando/Programando.ipynb'>"Programando en Python"</a>
</div>

---

## Dudas, problemas técnicos y soluciones. <a class="anchor" id="dudas"></a>

Para centralizar esas dudas técnicas sobre el tema de este notebook o proponer soluciones o sugerencias más técnicas que queremos encontrar en el futuro comentadas y visibles para todos, haz uso del siguiente canal:

[Foro Técnico: Python](https://github.com/uibcdf/Academia/issues/5)

## Más recursos útiles <a class="anchor" id="recursos"></a>

El propósito de esta unidad es ser un documento únicamente introductorio. Puedes encontrar -o contribuir añadiendo- más información útil en el siguiente listado:

### Documentación <a class="anchor" id="documentacion"></a>
https://www.python.org/    
https://realpython.com/    
https://docs.python-guide.org/    
https://wiki.python.org/moin/SpanishLanguage    
http://www.scipy-lectures.org/intro/intro.html
https://github.com/damianavila/Python-Cientifico-HCC/blob/master/1_Python_Cientifico_Intro.ipynb    

### Tutoriales, Webinars y cursos gratuitos <a class="anchor" id="tutoriales"></a>
https://www.python.org/about/gettingstarted/    
https://docs.python.org/3/tutorial/    
http://docs.python.org.ar/tutorial/    
http://swcarpentry.github.io/python-novice-inflammation/   
https://www.datacamp.com/community/open-courses?tag=python
https://www.datacamp.com/community/tutorials?tag=python
https://realpython.com/tutorials/python/    
https://www.learnpython.org/    
https://www.datacamp.com/courses/intro-to-python-for-data-science    
https://docs.python-guide.org/intro/learning/    
https://www.codecademy.com/    
https://pythonprogramming.net/   
http://www.scipy-lectures.org/
https://www.programiz.com/
https://www.sololearn.com/
https://www.codewars.com/
https://jasonpark.me/DuoCoder/public/
https://www.afterhoursprogramming.com/
https://www.datacamp.com/community/open-courses?tag=python

### Plataformas de aprendizaje donde encontrar cursos gratuitos

https://www.edx.org/    
https://www.mooc.org/     
https://www.coursera.org/
https://ocw.mit.edu/
https://www.udacity.com/
https://openlearning.mit.edu/



<br />

<div style='text-align: right;'> <a href="../Programando/Programando.ipynb">Ir a la siguiente unidad</a> </div>

-------
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/uibcdf/Academia">UIBCDF-Academia</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/uibcdf/Academia/graphs/contributors">UIBCDF Lab, autores y colaboradores</a> es material protegido bajo una licencia <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

