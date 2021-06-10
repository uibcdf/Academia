<p style="text-align:left;">
   <a href="../README.md">Ir al menú anterior</a>
   <span style="float:right;">
        <a href="../README.md">Ir a la unidad anterior</a>
   </span>
</p>

-----

<br>
<center><img src="https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png" width="20%"></center>
<br>

# Qué es Git y cómo se usa

<div class="alert alert-info" role="alert">
<strong>Info:</strong> Si crees que este notebook necesita algún cambio no dudes en <a href="../../../../UIBCDF-Academia/Como_contribuir/Como_contribuir.md" class="alert-link">contribuir a su desarrollo</a>.
</div>

<br>

- [¿Qué es Git?](#¿Qué-es-Git?)
- [¿Cómo se instala?](#¿Cómo-se-instala?)
   - [Linux](#Linux)
      - [Ubuntu](#Ubuntu)
   - [MacOS](#MacOS)
   - [Windows](#Windows)
- [¿Cómo se usa?](#¿Cómo-se-usa?)
   - [Como controlador de versiones local y personal](#Como-controlador-de-versiones-local-y-personal)
      - [¿Quieres generar un proyecto y llevar tu propio control de versiones?](#¿Quieres-generar-un-proyecto-y-llevar-tu-propio-control-de-versiones?)
   - [Como cliente para un servidor remoto central de git](#Como-cliente-para-un-servidor-remoto-central-de-git)
      - [En un servidor nuestro](#En-un-servidor-nuestro)
      - [En la nube](#En-la-nube)
   - [Breve compendio de los comandos más útiles](#Brever-compendior-de-los-comandos-más-útiles)
      - [Listado de ramas](#Listado-de-ramas)
      - [Cambio de rama](#Cambio-de-rama)
      - [Listado de ramas y commits](#Listado-de-ramas-y-commits)
      - [Creación de nueva rama](#Creación-de-nueva-rama)
      - [Eliminación de una rama](#Eliminación-de-una-rama)
      - [Creación del clon local de una nueva rama remota](#Creación-del-clon-local-de-una-nueva-rama-remota)
   - [Compendio de las rutinas más útiles](#Compendio-de-las-rutinas-más-útiles)
      - [Creo una nueva rama y la empujo también al origin remoto](#Creo-una-nueva-rama-y-la-empujo-también-al-origin-remoto)
- [Más recursos útiles](#recursos)
    - [Documentación](#documentacion)
    - [Tutoriales, Webinars y cursos gratuitos](#tutoriales)

## ¿Qué es Git?

[Git][git] es una herramienta de [control de versiones][acerca_control_versiones]. Estas herramientas fueron concebidas para el desarrollo de software, ya que permiten un flujo de trabajo eficiente al mantener un historial de cambios y versiones anteriores. Más especificamente Git, fue creada por Linus Torvalds para gestionar el desarrollo de los kernels (nucleos del sistema) de Linux. Existen otras herramientas similares, como SVN de la cual quizás hayas escuchado o usado, no obstante hoy en dia Git se ha convertido en un protocolo muy popular para el desarrollo de cualquier proyecto que involucre la participación de varias personas.

¿Cómo funciona exactamente? El historial que comentamos anteriormente es el "corazón" de Git, pues incluye: qué cambios hizo quién o cúando, así como el propósito de los mismos. Tener dicho registro ofrece varias ventajas, pues facilita cosas como: ir hacia atrás en la historia del desarrollo del proyecto, implementar nuevos cambios de manera tentativa, trazabilidad de errores, crear copias del proyecto en las que hacer pruebas para posteriormente fusionar la copia con el proyecto original, etc.

Por esta razón, para la comunidad científica (especialmente la que desarrolla trabajo computacional), Git se ha convertido en una manera cómoda y relativamente flexible de gestionar tareas en grupo. Justo por eso, Git ya no se limita únicamente al desarrollo de software. Puedes desde escribir un documento en colaboración hasta desarrollar unos scripts de análisis o crear una figura. En resumen, Git es un controlador de cambios que se encuentra detrás de muchas de las tareas que realizamos individualmente y en grupo en la UIBCDF. Así que vale la pena presentar algunos aspectos generales sobre su uso.


## ¿Cómo se instala?

### Linux

Git suele estar por defecto instalado en cualquier distribución de Linux. En caso de que no sea así puedes recurrir a [su repositorio oficial][repositorio_git].

#### Ubuntu

Si tu distribución de Linux es Ubuntu, Git se encuentra en el repositorio principal y puede ser instalado con el comando:

```bash
sudo apt install git
```

### MacOS

Para instalar Git en Mac recomendamos acudir a [su repositorio oficial][repositorio_git].

### Windows

Para instalar Git en Windows recomendamos acudir a [su repositorio oficial][repositorio_git].

## ¿Cómo se usa?
<center>
<img src="https://imgs.xkcd.com/comics/git.png" width="250">
</center>
    
### Como controlador de versiones local y personal

#### ¿Quieres generar un proyecto y llevar tu propio control de versiones?

Cómo crear un proyecto/repositorio:

```bash
git init
```

Cómo clonar un proyecto existente en tu máquina:

```bash
git clone /path/to/repository
```


También puedes clonar un proyecto que se encuentra en una máquina remota.

```bash
git clone username@host:/path/to/repository
```

Cómo añadir un nuevo fichero al listado de ficheros del proyecto que controla Git:

```bash
git add <filename>
```

Cómo añadir todos los ficheros presentes en el directorio al listado que controlado Git:

```bash
git add *
```

Recordarás que comentamos sobre los registros de Git, ahora lo veremos en acción. Primeramente veremos el comando status: 

```bash
git status
```

Notarás que Git nos menciona que estamos al día con la versión master, eso quiere decir que la copia local y la copia en Git son idénticas. En caso contrario se nos muestran los archivos de los cuales Git no lleva registro (si no existen) o aquellos en los que la copia local y el master no coinciden. Por ejemplo, crea un nuevo documento en el repositorio git y repite el comando anterior:

```bash
touch nuevo.txt

git status
```

Ahora, supongamos que este archivo será un cambio a implementar en el repositorio, lo que sigue es notificar a Git que estos cambios serán "permanentes". A esta acción se la denomina "comprometer" (*commit* en inglés) los cambios, y se realiza para registrar en el histórico el estado actual del proyecto. Junto a estos cambios se recomienda incluir un mensaje de texto explicando las modificaciones:

```bash
git commit -m "Commit message"
```

<center>
<img src="https://imgs.xkcd.com/comics/git_commit.png" width="400">
</center>

Procura que tus notas sobre los commits sean claras, así aprovecharás al máximo el registro de Git y te ahorrarás dolores de cabeza en el futuro.

Cabe mencionar que notificar los cambios no es suficiente para implementarlos. Si cuentas con los permisos adecuados, despues de haber hecho el correspondiente `commit`, es necesario "empujar" tus cambios al repositorio remoto, mediante el siguiente comando:

```bash
git push
```

Durante el uso personal, el comando push casi no te dará algun error a menos que pierdas conexión con Git. Cuando se trabaja en colaboración es posible que haya cambios en el repositorio remoto, en ese caso Git evitará que implementes cambios si no posees la versión "más actual". Para resolver esta situación puedes "tirar" de estos para implementarlos en tu clon:

```bash
git pull
```
Después de esto, podrás revisar los cambios implementados y decidir antes de duplicar o implementar de forma innecesaria. Recuerda, el comando pull sirve para mantener al día tu clon local, por lo que una buena práctica de trabajo es "tirar" del repositorio antes de intentar implementar cambios.

En la introducción comentamos también que Git permite hacer pruebas al margen de la copia principal. Para realizar dicha operación haremos uso de los siguientes comandos:

```bash
git checkout -b nombre_de_la_rama # para crear la rama
git checkout master # para volver a la copia maestro
git branch -d nombre_de_la_rama # para borrar la rama
git merge nombre_de_la_rama # para fusionar los cambios de una rama en la copia maestra
```

Encuentra un breve listado de otros comandos útiles [aquí][git_commands]

### Como cliente para un servidor remoto central de git

#### En un servidor nuestro

La UIBCDF no tiene todavía su servidor de Git central configurado y la información e instrucciones para configurar uno escapan al propósito de este documento.

#### En la nube

En la UIBCDF hacemos uso de un servidor remoto en la nube como GitHub. Conocemos que existen otras posibilidades, por ejemplo GitLab, pero por motivos históricos y porque muchas de las librerías y herramientas que usamos se encuentran como proyectos públicos en GitHub, [puedes encontrarnos ahí][github_uibcdf].

Para hacer uso de GitHub, o interaccionar desde tu máquina con un repositorio de GitHub, te sugerimos acudas al [siguiente notebook][unidad:github] en este repositorio.

### Breve compendio de los comandos más útiles

#### Listado de ramas

Para listar únicamente las ramas locales:

```bash
git branch
```

Para listar únicamente las ramas remotas:

```bash
git branch -r
```

Para listar todas las ramas:

```bash
git branch -a
```

#### Cambio de rama

```bash
git checkout nombre_de_rama
```

#### Listado de ramas y commits

Para listar únicamente las ramas locales:

```bash
git show-branch
```

Para listar únicamente las ramas remotas:

```bash
git show-branch -r
```

Para listar todas las ramas:

```bash
git show-branch -all
```

#### Creación de nueva rama

Para crear una nueva rama en el repositorio local

```bash
git branch nombre_de_rama
```

Podemos tambien crear una nueva rama y saltar a ella con un solo comando:

```bash
git checkout -b nombre_de_rama
```

En el caso de que exista un clon remoto del repositorio podemos empujar la creación de la nueva
rama. Por ejemplo, supongamos que nuestro repositorio original es remoto, podemos empujar la
creación de nuestra nueva rama local como:

```bash
git push -u origin <new-branch>
```

#### Eliminación de una rama

Para eliminar una rama:

```bash
git branch -d nombre_de_rama
```

#### Creación del clon local de un una nueva rama remota

Supongamos que en el repository remoto denominado 'origin' hay una rama llamada 'foo'. Esto se puede ver de la siguiente manera:

```bash
git branch --all

  gh-pages
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/foo
  remotes/origin/gh-pages
  remotes/origin/master
```

Podemos traer al clon local del repositorio la copia de la rama 'foo':

```bash
git fetch origin foo:foo
```

Ya podemos ver que existe la rama local 'foo':

```bash
git branch --all

  foo
  gh-pages
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/foo
  remotes/origin/gh-pages
  remotes/origin/master
```

Y podemos también cambiar a la nueva rama para trabajar localmente:

```bash
git checkout foo
```

### Compendio de las rutinas más útiles

#### Creo una nueva rama y la empujo también al origin remoto

```bash
gir checkout -b nombre_de_rama
git push -u origin nombre_de_rama
```

---

## Dudas, problemas técnicos y soluciones. <a class="anchor" id="dudas"></a>

Para centralizar esas dudas, sugerencias o soluciones técnicas sobre el tema de esta unidad, haz uso del siguiente canal:

[Foro Técnico: Git][foro_tecnico_git]

## Más recursos útiles <a class="anchor" id="recursos"></a>

El propósito de este notebook es ser un documento únicamente introductorio. Puedes encontrar -o contribuir añadiendo- más información útil en el siguiente listado:

### Documentación <a class="anchor" id="documentacion"></a>

https://git-scm.com/book/es  
http://rogerdudler.github.io/git-guide/index.es.html  
https://codigofacilito.com/articulos/que-es-git  
https://swcarpentry.github.io/git-novice-es/

https://git-scm.com/book/en  
https://git-scm.com/docs  
http://swcarpentry.github.io/git-novice/
http://rogerdudler.github.io/git-guide/  
https://www.atlassian.com/git/tutorials/what-is-git  
https://jahya.net/blog/git-vs-github/  
https://www.atlassian.com/git/tutorials
https://github.com/joshnh/Git-Commands
https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud

### Tutoriales, Webinars y cursos gratuitos <a class="anchor" id="tutoriales"></a>

<br />

<div style='text-align: right;'> <a href="../GitHub/GitHub.md">Ir a la siguiente unidad</a> </div>

-------
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/uibcdf/Academia">UIBCDF-Academia</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/uibcdf/Academia/graphs/contributors">UIBCDF Lab, autores y colaboradores</a> es material protegido bajo una licencia <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>



[unidad:github]: ../GitHub/GitHub.md 

[git]: https://git-scm.com/
[acerca_control_versiones]: https://git-scm.com/book/es/v1/Empezando-Acerca-del-control-de-versiones
[repositorio_git]: https://git-scm.com/downloads
[github_uibcdf]: https://github.com/uibcdf
[foro_tecnico_git]: https://github.com/uibcdf/Academia/issues/1
[git_commands]: http://rogerdudler.github.io/git-guide/index.es.html

