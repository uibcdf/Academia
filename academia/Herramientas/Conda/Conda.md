<img src="https://conda.io/docs/_images/conda_logo.svg" width="400">

---
`Nota: Si crees que este notebook necesita algún cambio no dudes en contribuir a su desarrollo.`

---

# ¿Qué es Conda?

Conda es un gestor de entornos, paquetes y canales, operativo para varios lenguages -Python entre ellos-. Antes de nada, aclaremos qué es un paquete, qué es un canal y qué es un entorno de desarrollo. 

## ¿Qué es un paquete?

Un paquete, o librería en este caso, es un conjunto de ficheros de código 'empaquetado' con las instrucciones de instalación pertinentes y programado para realizar unas tareas específicas. Si estuvíeramos hablando de un lenguage compilado, el paquete sería el 'programa' junto con su instalador que compilas (instalas) en tu computadora. Este programa suele requerir para su correcto funcionamiento que en tu computadora tengas otros programas instalados -dependencias-. Así, es habitual que antes de instalar un programa tengas que preocuparte de que las dependencias estén presentes. Por ejemplo, el sistema operativo Linux cuenta con gestores de paquetes que probablemente usas ('apt-get', 'yum', 'synaptic', 'aptitude', etc.) que se preocupan de que el software que quieres instalar encuentre las dependencias en tu máquina o las descargue del repositorio para su instalación.

En el caso de un lenguage interpretado, el paquete o librería se almacena en una carpeta que el interpretador, Python en este caso, conoce. Es allí donde deben estar también las librerías de las que depende. Entenderás entonces que con el uso, la instalación de nuevas librerías o la actualización de las exisistentes, es conveniente que un gestor mantenga el equilibrio en tu ecosistema de paquetes de python.

## ¿Qué es un canal?

Un grupo de desarrolladores o usuarios pueden configurar una lista de paquetes accesibles, de manera pública o privada, a través del gestor de paquetes. Como ejemplo de canal público de conda puedes echarle un ojo a, probablemente, el canal más popular mantenido por usuarios: [conda-forge](https://conda-forge.org/) y [su lista de más de 5600 paquetes](https://anaconda.org/conda-forge).

## ¿Qué es un entorno?

Tu sistema operativo cuenta probablemente con un interpretador de python (versión 2.x o 3.x) además de una extensa colección de librerías requeridas por el mismo sistema o por los programas que instalaste. Cuando desarrollas software o lo usas a un nivel avanzado, como va a ser el caso, es habitual que trabajes con librerías experimentales o herramientas que se encuentran siempre en un eterno proceso de desarrollo y mantenimiento. En este caso es un buen hábito trabajar con ecosistemas de paquetes (entornos) independientes del sistema operativo y entre sí. Por ejemplo, puedes crear un entorno con python 2.7 para usar esa librería que todavía no fue actualizada y otro entorno con python 3.7 para otro tipo de trabajo... y 'cargarlos' y 'descargarlos' como si fueran microsistemas virtuales independientes.

## ¿Qué es entonces un gestor de entornos, paquetes y canales?

Un gestor de entornos, paquetes y canales, como pueden ser conda, homebrew, pip o pipenv, se ocupa de administrar tus entornos de trabajo posibilitando en ellos la instalación y actualización de paquetes desde los canales que configures.

Conda, creado y soportado por [Anaconda](https://www.anaconda.com/), ofrece esto y más. La mejor manera de comenzar para un usuario inexperto es instalar la última versión de miniconda y empezar a usarlo.


<img src="https://www.explainxkcd.com/wiki/images/c/cb/python_environment.png" width="400">

*Title text by the author (XKCD): The Python environmental protection agency wants to seal it in a cement chamber, with pictoral messages to future civilizations warning them about the danger of using sudo to install random Python packages.*


## ¿Qué es Miniconda?

Miniconda es la versión 'mínima' de Conda con la que se aconseja empezar. Conda ofrece descargar un gestor junto con una gran colección de librerías, pero esto además de pesado es innecesario. Instala miniconda en tu máquina para comenzar con el uso de conda y descarga poco a poco los paquetes que vayas requiriendo.

# ¿Cómo se instala?

Puedes encontrar las instrucciones de instalación y manejo de conda en [su página oficial](https://conda.io/docs/). Antes de ver las instrucciones según el sistema operativo que uses, échale un ojo al menos a la estructura de la [guía de usuario](https://conda.io/docs/user-guide/index.html).

## Linux.

https://conda.io/docs/user-guide/install/linux.html

## MacOS.

https://conda.io/docs/user-guide/install/macos.html

## Windows.

https://conda.io/docs/user-guide/install/windows.html

# ¿Cómo se usa?

Existe una excelente [documentación oficial](https://conda.io/docs/index.html) con [breves guías para comenzar](https://conda.io/docs/user-guide/getting-started.html) y [tutoriales más avanzados](https://conda.io/docs/user-guide/tutorials/index.html).

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

# Dudas de uso, problemas técnicos y soluciones.

Para centralizar esas dudas técnicas sobre el tema de este notebook o proponer soluciones o sugerencias más técnicas que queremos encontrar en el futuro comentadas y visibles para todos, haz uso del siguiente canal:

[Foro Técnico: Conda](https://github.com/uibcdf/Academia/issues/6)

# Más recursos útiles 

El propósito de este notebook es ser un documento únicamente introductorio. Puedes encontrar -o contribuir añadiendo- más información útil en el siguiente listado:

## Documentación

https://conda.io/    

## Tutoriales y cursos gratuitos

https://geohackweek.github.io/Introductory/01-conda-tutorial/   \[EN\]    
http://gatomontez.com/articulo/2014/02/16/computo-cientifico-con-python-y-anaconda/#.W-ySQstKiV4   \[ES\]    

## Webinars


```python

```
