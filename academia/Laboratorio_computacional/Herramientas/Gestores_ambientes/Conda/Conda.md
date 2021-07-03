<p style="text-align:left;">
   <a href="../README.md">Ir al menú anterior</a>
   <span style="float:right;">
        <a href="../README.md">Ir a la unidad anterior</a>
   </span>
</p>

-----

<br>
<center>
<img src="https://conda.io/docs/_images/conda_logo.svg" width="40%">
</center>
<br>


# Qué es Conda, cómo se instala y cómo se usa

<div class="alert alert-info" role="alert">
<strong>Info:</strong> Si crees que este notebook necesita algún cambio no dudes en <a href="../../../../UIBCDF-Academia/Como_contribuir/Como_contribuir.md" class="alert-link">contribuir a su desarrollo</a>.
</div>

<br>

Esta introducción a Conda está pensada para aquellos que tienen poco o ningún
conocimiento previo. Esperamos pueda serte útil.

- [¿Qué es Conda?](#¿Qué-es-Conda?)
   - [¿Qué es un paquete?](#¿Qué-es-un-paquete?)
   - [¿Qué es un canal?](#¿Qué-es-un-canal?)
   - [¿Qué es un entorno?](#¿Qué-es-un-entorno?)
   - [¿Qué es entonces un gestor de entornos, paquetes y canales?](#¿Qué-es-un-entorno?)
   - [¿Qué es Miniconda?](#¿Qué-es-Miniconda?)
- [¿Cómo se instala?](#¿Cómo-se-instala?)
   - [Linux](#Linux)
   - [MacOS](#MacOS)
   - [Windows](#Windows)
- [¿Cómo se usa?](#¿Cómo-se-usa?)
- [Dudas, problemas técnicos y soluciones](#dudas)
- [Más recursos útiles](#recursos)
    - [Documentación](#documentacion)
    - [Tutoriales, Webinars y cursos gratuitos](#tutoriales)

## ¿Qué es Conda?

Conda es un gestor de entornos, paquetes y canales, operativo para varios lenguages -Python entre ellos-. Antes de nada, aclaremos qué es un paquete, qué es un canal y qué es un entorno de desarrollo. 

### ¿Qué es un paquete?

Un paquete, o librería en este caso, es un conjunto de ficheros de código 'empaquetado' con las instrucciones de instalación pertinentes y programado para realizar unas tareas específicas. Si estuvíeramos hablando de un lenguage compilado, el paquete sería el 'programa' junto con su instalador que compilas (instalas) en tu computadora. Este programa suele requerir para su correcto funcionamiento que en tu computadora tengas otros programas instalados -dependencias-. Así, es habitual que antes de instalar un programa tengas que preocuparte de que las dependencias estén presentes. Por ejemplo, el sistema operativo Linux cuenta con gestores de paquetes que probablemente usas ('apt-get', 'yum', 'synaptic', 'aptitude', etc.) que se preocupan de que el software que quieres instalar encuentre las dependencias en tu máquina o las descargue del repositorio para su instalación.

En el caso de un lenguage interpretado, el paquete o librería se almacena en una carpeta que el interpretador, Python en este caso, conoce. Es allí donde deben estar también las librerías de las que depende. Entenderás entonces que con el uso, la instalación de nuevas librerías o la actualización de las exisistentes, es conveniente que un gestor mantenga el equilibrio en tu ecosistema de paquetes de python.

### ¿Qué es un canal?

Un grupo de desarrolladores o usuarios pueden configurar una lista de paquetes accesibles, de manera pública o privada, a través del gestor de paquetes. Como ejemplo de canal público de conda puedes echarle un ojo a, probablemente, el canal más popular mantenido por usuarios: [conda-forge][conda_forge] y [su lista de más de 5600 paquetes][anaconda_conda_forge].

### ¿Qué es un entorno?

Tu sistema operativo cuenta probablemente con un interpretador de python (versión 2.x o 3.x) además de una extensa colección de librerías requeridas por el mismo sistema o por los programas que instalaste. Cuando desarrollas software o lo usas a un nivel avanzado, como va a ser el caso, es habitual que trabajes con librerías experimentales o herramientas que se encuentran siempre en un eterno proceso de desarrollo y mantenimiento. En este caso es un buen hábito trabajar con ecosistemas de paquetes (entornos) independientes del sistema operativo y entre sí. Por ejemplo, puedes crear un entorno con python 2.7 para usar esa librería que todavía no fue actualizada y otro entorno con python 3.7 para otro tipo de trabajo... y 'cargarlos' y 'descargarlos' como si fueran microsistemas virtuales independientes.

### ¿Qué es entonces un gestor de entornos, paquetes y canales?

Un gestor de entornos, paquetes y canales, como pueden ser conda, homebrew, pip o pipenv, se ocupa de administrar tus entornos de trabajo posibilitando en ellos la instalación y actualización de paquetes desde los canales que configures.

Conda, creado y soportado por [Anaconda][anaconda], ofrece esto y más. La mejor manera de comenzar para un usuario inexperto es instalar la última versión de miniconda y empezar a usarlo.

<br>
<center>
<img src="https://www.explainxkcd.com/wiki/images/c/cb/python_environment.png" width="400">
</center>
<br>

### ¿Qué es Miniconda?

Miniconda es la versión 'mínima' de Conda con la que se aconseja empezar. Conda ofrece descargar un gestor junto con una gran colección de librerías, pero esto además de pesado es innecesario. Instala miniconda en tu máquina para comenzar con el uso de conda y descarga poco a poco los paquetes que vayas requiriendo.

## ¿Cómo se instala?

Puedes encontrar las instrucciones de instalación y manejo de conda en [su página oficial][conda_docs]. Antes de ver las instrucciones según el sistema operativo que uses, échale un ojo al menos a la estructura de la [guía de usuario][guia_conda].

### Linux.

https://conda.io/docs/user-guide/install/linux.html

### MacOS.

https://conda.io/docs/user-guide/install/macos.html

### Windows.

https://conda.io/docs/user-guide/install/windows.html

## ¿Cómo se usa?

Existe una excelente [documentación oficial][conda_docs] con [breves guías para comenzar][conda_getting_started] y [tutoriales más avanzados][conda_tutorials].

Vamos a exponer aquí la pequeña lista de comandos que más vas a usar.

Cómo actualizar conda:

```python
conda update conda
```

Cómo crear un entorno de python 3 llamado en este caso `academia`:

    
```python
conda create -n academia python=3
```

Cómo cargar o activar un entorno:

```bash
source activate academia
```

Cómo instalar el paquete `numpy`:

```bash
conda install numpy
```

Cómo instalar el paquete `jupyter` del canal `conda-forge`:

```bash
conda install -c conda-forge jupyter
```

Cómo actualizar todos los paquetes de un entorno:

```bash
conda update --all
```

Cómo consultar la lista de paquetes instalados en un entorno:

```bash
conda list
```

Cómo desactivar el entorno cargado:

```bash
source deactivate
```

Cómo consultar la lista de entornos:

```bash
conda info --envs
```

Cómo eliminar un entorno:

```bash
conda remove -n academia
```

Cómo añadir un canal, en este caso `conda-forge`, a la lista de canales consultados para la instalación y actualización de paquetes:

```
conda config --add channels conda-forge
```

Cómo consultar la lista de canales incluidos en tu archivo de configuración para instalar y actualizar paquetes, y su prioridad:

```bash
conda config --get
```

Como eliminar un canal, en este caso `conda-forge`, de la lista de canales incluidos en el archivo de configuración.

```bash
conda config --remove channels conda-forge
```

---

## Dudas, problemas técnicos y soluciones. <a class="anchor" id="dudas"></a>

Para centralizar esas dudas técnicas sobre el tema de esta unidad o proponer soluciones o sugerencias más técnicas que queremos encontrar en el futuro comentadas y visibles para todos, haz uso del siguiente canal:

[Foro Técnico: Conda][foro]

## Más recursos útiles <a class="anchor" id="recursos"></a>

Esto era sólo una guia introductoria. No es funcional documentarse o estudiar mucho sin antes comenzar a usar el sistema operativo Linux. Aprenderás de manera más solida si con el uso te van surgiendo necesidades a las que vas dando solución poco a poco. Si la computadora es tu herramienta de trabajo, es tu deber conocerla. Puedes encontrar -o contribuir añadiendo- más información útil en el siguiente listado.

### Documentación <a class="anchor" id="documentacion"></a>

https://conda.io/    

### Tutoriales, Webinars y cursos gratuitos <a class="anchor" id="tutoriales"></a>

https://geohackweek.github.io/Introductory/01-conda-tutorial/   \[EN\]    
http://gatomontez.com/articulo/2014/02/16/computo-cientifico-con-python-y-anaconda/#.W-ySQstKiV4   \[ES\]    
https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/04-sharing-environments/index.html
https://kaust-vislab.github.io/python-novice-gapminder/00-getting-started-with-conda/index.html
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file



<br />

<div style='text-align: right;'> <a href="../../Jupyter/README.md">Ir a la siguiente unidad</a> </div>

-------
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/uibcdf/Academia">UIBCDF-Academia</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/uibcdf/Academia/graphs/contributors">UIBCDF Lab, autores y colaboradores</a> es material protegido bajo una licencia <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

[conda_forge]: https://conda-forge.org/
[anaconda_conda_forge]: https://anaconda.org/conda-forge
[anaconda]: https://www.anaconda.com/
[conda_docs]: https://conda.io/docs/
[guia_conda]: https://conda.io/docs/user-guide/index.html
[conda_getting_started]: https://conda.io/docs/user-guide/getting-started.html
[conda_tutorials]: https://conda.io/docs/user-guide/tutorials/index.html
[foro]: https://github.com/uibcdf/Academia/issues/6

