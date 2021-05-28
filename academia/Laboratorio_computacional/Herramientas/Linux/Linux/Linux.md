<center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1200px-Tux.svg.png" width="200"></center>

---
`Nota: Si crees que este notebook necesita algún cambio no dudes en contribuir a su desarrollo.`

---

## Tabla de contenidos

* [¿Qué es Linux?](#Que)
* [¿Por qué Linux?](#Por_que)
* [Distribuciones de Linux.](#Distribuciones-de-Linux.)
* [¿Cómo se instala?](#Como)
   * [Búsqueda de información.](#Busqueda)
   * [¿USB booteable o CD para la instalación?](#USB_booteable)
   * [¿Particiones?](#Particiones)
   * [El sistema de ficheros.](#El-sistema-de-ficheros.)
   * [La memoria Swap.](#La-memoria-Swap.)
* [¿Puedo usar además otros sistemas operativos en la misma máquina?](#Otros_SOs)
   * [Sistemas operativos virtuales.](#Sistemas-operativos-virtuales.)
   * [Compatibilidad de ficheros.](#Compatibilidad-de-ficheros.)
   * [Usando una memoria usb compatible con distintos SOs.](#Usando-una-memoria-usb-compatible-con-distintos-SOs.)
* [La instalación de software.](#Instalacion_software)
* [La organización de ficheros del sistema Linux.](#organizacion)
* [Entornos de escritorio.](#Entornos-de-escritorio.)
* [La terminal y la sintaxis de Bash.](#La-terminal-y-la-sintaxis-de-Bash.)
   * [La navegación de ficheros.](#navegacion_ficheros)
   * [Otros comandos útiles en la gestión de ficheros: touch, mv, rm y rmdir.](#mv_rm)
   * [echo, less y more.](#echo)
   * [cat y paste para concatenear ficheros.](#cat-y-paste-para-concatenar-ficheros.)
   * [El reconocimiento y filtrado de texto: grep, awk y sed.](#grep)
   * [top, ps y kill](#top)
   * [Ayuda de comandos con man, --help y apropos.](#man)
   * [Bash como lenguage de programación para la terminal.](#bash)
      * [Variables.](#Variables.)
      * [Bucles.](#Bucles.)
      * [Condicion lógica *if*.](#if)
      * [Conversión de imágenes encontradas en un directorio.](#convert)
      * [Listado de ficheros pesados.](#Listado-de-ficheros-pesados.)
      * [Finalización de un proceso como gatillo para otro.](#gatillo)
* [Editores de texto.](#Editores-de-texto.)
* [El script.](#El-script.)
* [Las extensiones de los archivos.](#Las-extensiones-de-los-archivos.)
* [Los permisos de los ficheros.](#Los-permisos-de-los-ficheros.)
* [Los enlaces simbólicos de fichero.](#ln)
* [Los usuarios y los grupos.](#Los-usuarios-y-los-grupos.)
* [Root, el superusuario, y sudo.](#sudo)
* [Los ficheros de configuración de usuario.](#configuracion_usuario)
* [Las variables de entorno.](#Las-variables-de-entorno.)
* [SSH y la conexión con otras máquinas.](#ssh)
* [Nota final.](#Nota-final.)

* [Dudas, problemas técnicos y soluciones.](#dudas)

## ¿Qué es Linux? <a class="anchor" id="Que"></a>

Un sistema operativo (SO) es el software que instalas en tu computadora para gestionar el uso de su hardware (monitor, teclado, procesador, etc.) y que sirve de plataforma para la instalación de las herramientas que usarás (editor de texto, editor de imágenes, navegador, etc.). En ese sentido Linux no es un sistema operativo. Es una familia de sistemas operativos. Todos basados en la misma tecnología y filosofía de desarrollo, todos descendientes del mismo sistema madre.

Es relevante entender cómo nace Linux para valorar en lo que se ha convertido, y así saber qué podemos esperar de él. En la década de los 90, lo que comenzó en los 60 como un proyecto frustrado -MULTICS- entre el MIT, AT&T Bell Labs y General electric, cristalizó en un proyecto de sistema operativo casi como un proyecto académico. En 1970, Ken Thompson, un ingeniero de AT&T que seguía trabajando por iniciativa propia sobre los rescoldos del sistema operativo creado para MULTICS, programó un nuevo sistema operativo multitarea con linea de comandos y unas poquitas aplicaciones: UNICS (más tarde llamado UNIX). Ken Thompson en realidad sólo pretendía que un juego que Bell Labs había programado para la computadora del proyecto MULTICS, Space Travel, corriera de manera rápida y barata. Pero su proyecto acabo siendo empujado por su equipo de trabajo para crear un sistema operativo de soporte para los desarrolladores de nuevas aplicaciones de entonces. Años después, en 1985, Richard Stallman crea la licencia GNU y funda la Free Software Foundation. Richard S. había entendido que el desarrollo de aplicaciones de uso libre, el acceso a ellas y la posibilidad de modificarlas y transformarlas, iba a impulsar rápidamente el progreso científico y tecnológico. En este contexto, en un momento en el que ya se contaba con varias aplicaciones de uso libre para UNIX y un pequeño grupo de desarrolladores que apostaban por el acceso libre y la cooperación, Linus Torvals en 1991 programa un sistema operativo basado en los mismos principios que UNIX y bajo licencia GNU. Linux, así llamado, nace libre de uso y desarrollo, con un conjunto de aplicaciones plenamente operativas con las mismas características y con el potencial de ser modificadas y mejoradas por cualquiera.

Es así como, desde el comienzo de los 90, Linux comienza en la cabeza y las manos de varios desarrolladores a generar ramificaciones en forma de distintas distribuciones. Muchas de ellas respetando el espíritu inicial de la licencia GNU, de acceso y desarrollo libre. Esto cataliza su uso primero en el entorno académico para más tarde saltar a la iniciativa privada y el uso doméstico. La posibilidad para cualquier usuario de actuar de forma activa en el desarrollo: documentando, reportando fallos, generando soluciones, creando software o incluso generando nuevas distribuciones de Linux; hace que este proyecto haya de manera muy rápida resuelto problemas de uso general, como entornos sencillos y ligeros para el uso de la ofimática, y específicos, como protocolos de seguridad que hacen de Linux la base para el sistema operativo que opera por ejemplo en el Departamento de Defensa de Estados Unidos o en el Banco de China.

## ¿Por qué Linux? <a class="anchor" id="Por_que"></a>

Los motivos para usar Linux como SO de trabajo van mucho más allá que una cuestión de principios. Linux nació como un SO capaz de manejar múltiples procesos y múltiples usuarios en la misma computadora. Desde entonces ha ido sofisticándose y adaptandose, gracias a la gran población de usuario/desarrolladores, para ser eficaz en cuestiones como el cálculo científico o el análisis masivo de datos. Por ir concretamente a lo que más nos interesa. Linux es el entorno usado desde su nacimiento en entornos académicos donde la computación es una herramienta de desarrollo esencial. La manera de trabajar de Linux nos permite tener todo el control de la máquina de un modo óptimo en la programación de tareas, aunque esto requiera un esfuerzo de aprendizaje. Puede que tengas experiencia en el manejo de Windows o MacOS, y son perfectamente útiles para todas las cuestiones que aprenderás en este repositorio, pero su diseño original fue hecho para cubrir otras necesidades. Es cierto que sus entornos de escritorio ya no son la única interfaz de interacción con la máquina, puedes usar también terminales. Al igual que Linux incluyó también un entorno gráfico sofisticado para navegar con ventanas. Pero el desarrollo de aplicaciones de alta demanda computacional se hace, no por motivos ideológicos, en Linux. A esto podemos añadir que:

- Encontrarás un activo y numeroso grupo de usuarios como tú comentando en foros y blogs sus problemas de uso y sus soluciones.
- El aprendizaje de su uso te permite convertirte no sólo en consumidor de aplicaciones, sino en generador de tus propias soluciones (que pueden ser útiles para los demás también).
- Tiene menos problemas de seguridad que otros SOs.
- Está en constante evolución, dictada por las necesidades de la comunidad, no por criterios de mercado.
- La mayoría de distribuciones pueden ser instaladas sin coste alguno. Este es el caso de todos los programas que vas a necesitar para seguir este material.
- Linux tiene problemas, y más si usas la última versión de ciertas distribuciones más experimentales. Pero los desarrolladores o la comunidad de usuarios pronto encuentra la solución y ésta es implementada para todo el mundo.

<br>
<br>
<center><img src="https://imgs.xkcd.com/comics/command_line_fu.png" width="450"></center>

## Distribuciones de Linux.

Hay infinidad de distribuciones de Linux ([aquí por ejemplo una lista ordenada por popularidad](https://distrowatch.com/dwres.php?resource=popularity)). Pero si Linux es la base común de estos sistemas operativos, ¿de qué estamos hablando cuando nos referimos a distribuciones de Linux? Una distribución es un sistema operativo configurado sobre Linux con cierto grado de personalización y optimización, con una serie de paquetes de software ajustados entre si para que el entorno funcione amigablemente y facilitando una experiencia de uso particular. La distribución de Linux suele condicionar la forma en que se instala, el entorno de escritorio, las utilidades de administración y los paquetes más sencillos que cualquier usuario usa para su gestión. Sin embargo las distribuciones no limitan ni restringen las utilidades o paquetes a instalar; y la experiencia de uso a través de la terminal no suele depender de la distribución más que en unos pocos comandos como por ejemplo la manera en la que instalamos paquetes. Vamos a hablar de algunas distribuciones para que entiendas a qué nos referimos con 'distribución' y [cúal se recomienda para cada caso](https://distrowatch.com/dwres.php?resource=major).

**Nota**: Las herramientas que se presentan posteriormente a esta unidad en el repositorio Academia y su uso (Git, Conda, Python, Jupyter, ...) no dependen en absoluto de la distribución de Linux que estés usando. Tampoco los comandos y conceptos que aprenderás en este notebook, comunes a todas las distribuciones por estar en la esencia del funcionamiento de Linux.

### Ubuntu

Si es la primera vez que usas Linux para trabajar, [Ubuntu](https://www.ubuntu.com/) puede ser la distribución más adecuada para tu máquina de trabajo (de escritorio o laptop). Ubuntu lleva años haciendo un esfuerzo por ser una de las distribuciones más amistosas en su instalación y uso para usuarios no expertos. Además, puedes encontrar la estabilidad necesaria en sus versiones LTS (Long Time Stable). El corazón de un sistema operativo Linux, el kernel, se actualiza constantemente para incluir la compatibilidad necesaria con el nuevo software o hardware, así como para solucionar problemas de seguridad o adoptar los últimos protocolos de operabilidad. Es habitual que todos los años se liberen varios kernels y tengas que actualizar el tuyo para estar 'a la última'. Sin embargo esto puede generar inestabilidades, ya que caminas siempre en el terreno de la innovación con herramientas y configuraciones no tan 'testeadas'. Ubuntu libera dos versiones de su distribución nuevas y actualizadas al año. Y a pesar de que su vocación es ofrecer un sistema operativo con pocos fallos de uso a usuarios no expertos, suelen aparecer algunos problemas que a los usuarios de linux con experiencia no nos parecen graves, pero a un usuario novato pueden generarle una sensación de inseguridad. Por eso, y para no comprometer máquinas dedicadas a la producción, hay una versión cada cierto tiempo cuyo mantenimiento y estabilidad se cuida por encima de las demás: [la versión LTS (Long Time Stable)](https://www.ubuntu.com/download/desktop). Te aconsejamos que para tu máquina de trabajo, si eres principiante, instales la última versión LTS de Ubuntu. Afrontarás menos problemas, disfrutarás de un entorno fácil de configurar y dispondrás de todo lo necesario para trabajar.

Además, Ubuntu, por ser una de las distribuciones más usadas, cuenta en internet con un elevado número de blogs y foros donde encontrarás información sobre todo lo que quieres hacer tanto en español como en inglés.

### ElementaryOS

Si lo que buscas es algo más estético, sencillo para una primera experiencia de uso, y que nadie te mire como a un o una nerd: puede que esta sea tu distribución. En el laboratorio no tenemos experiencia con [ElementaryOS](https://elementary.io/) y por lo tanto no la recomendamos para un entorno de producción. Pero en los últimos meses está ganando mucha popularidad y entendemos que si vienes de MacOs, ElementaryOS te parezca muy agradable.

### Arch

Si lo que buscas es una distribución que venga ligera en su instalación original y en la que puedas configurarlo todo como un nerd, échale un ojo a [ArchLinux](https://www.archlinux.org/). Esta distro es para usuarios más experimentados o para valientes novatos; y para máquinas que requieren un sistema operativo liviano y ajustable a su hardware, sin artificios ni vistosos procesos poco útiles.

### CentOS

Gran parte de los servidor y supercomputadores dedicados a cómputo científico suelen correr con [CentoOS](https://www.centos.org/). Esta distribución está bien optimizada y equipada, y es muy estable para este tipo de máquinas. Sin embargo, no es una distro muy popular para instalar en una laptop de alguien que está comenzando a usar Linux.

### Pop!\_OS
[System76](https://system76.com/pop), además de hacer unos laptops y unas computadoras de escritorio muy atractivos, han desarrollado una distribución de Linux pensada para el científico con una estética muy agradable: Pop!\_OS. Si estás buscando una distribución productiva, no orientada tanto a la ofimática o el uso doméstico-personal, sino al trabajo computacional intensivo, puede que Pop!\_OS sea lo que buscas.

### Otras distribuciones

Con el tiempo aprenderás que en el mundo de Linux, las distribuciones son como los equipos de futbol. Hay razones de todo tipo para ser fan de una u otra. [LinuxMint](https://linuxmint.com/) está los últimos años ganando mucho seguidores por conjugar una buena experiencia de uso para usuarios inexpertos y una larga colección de paquetes personalizados y versatiles, [Debian](https://www.debian.org/) puede que funcione para perfiles más expertos y nostálgicos (fue el primer sistema operativo Linux de muchos de nosotros), [RedHat](https://www.redhat.com/en) es una distro que se ha especializado en servir para entornos laborales privados con soporte bajo pago... Y así podemos encontrar personas que nos defiendan con argumentos plausibles, y pasión, que indudablemente [OpenSUSE](https://www.opensuse.org/), [Fedora](https://getfedora.org/), [Slackware](http://www.slackware.com/), [Gentoo](https://www.gentoo.org/), [FreeBSD](https://www.freebsd.org/) o [Mandriva](https://www.openmandriva.org/), son las mejores distribuciones de Linux. 

## ¿Cómo se instala? <a class="anchor" id="Como"></a>

Si es la primera vez que usas Linux, has de saber que cada distribución tiene su instalador. No hay un protocolo único de instalación para todo Linux. Puedes encontrar instaladores muy sencillos, con poco margen para personalizar la configuración, o muy completos pero complicados para un usuario inexperto. Es recomendable entonces que para empezar elijas una distribución amigable, bien documentada y con un buen grado de popularidad. El proceso que aquí vamos a describir es únicamente una descripción sobre la toma de decisión que has de hacer, eso sí es común a cualquier instalación. Tomaremos el ejemplo de querer instalar Ubuntu como caso práctico para introducir los comentarios a esas decisiones. Si tu intención es instalar otra distribución, seguramente tras leer esta sección y acudir a la documentación web correspondiente, encuentres el proceso más sencillo. 

### Búsqueda de documentación <a class="anchor" id="Busqueda"></a>

Lo primero que debes hacer es una búsqueda de la documentación que te oriente sobre el proceso de instalación de la distribución que deseas. En el caso de Ubuntu es fácil llegar tras una búsqueda rápida a abrir en el navegador páginas como las siguientes:

https://www.ubuntu.com/download/desktop   
https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop#0   
https://www.muylinux.com/2018/06/18/guia-instalacion-ubuntu-18-04-lts/   
https://www.muylinux.com/2018/05/29/instalar-ubuntu-consideraciones-previas/   
https://es.wikihow.com/instalar-Ubuntu   
https://www.genbeta.com/paso-a-paso/linux-paso-a-paso-instalar-ubuntu-con-dual-boot-junto-a-windows-10   
https://www.sololinux.es/que-hacer-despues-de-instalar-ubuntu-18-04-bionic-beaver/   
https://www.genbeta.com/a-fondo/8-cosas-y-algun-extra-que-hacer-luego-de-instalar-ubuntu-18-04    
https://maslinux.es/15-cosas-que-hacer-despues-de-instalar-ubuntu-18-04-bionic-beaver/   
https://www.linuxadictos.com/9-cosas-que-hacer-despues-de-instalar-ubuntu-18-04.html   

Como verás hay infinidad de foros, blogs y documentación que puedes encontrar. Échales un ojo antes de ponerte manos a la obra.

### ¿USB booteable o CD para la instalación? <a class="anchor" id="USB_booteable"></a>

Uno de los primeros pasos para instalar cualquier distribución de Linux es descargar el SO y su instalador. Estos habitualmente vienen en forma de único fichero '.iso' para quemar un CD o DVD, y guardarlo como soporte de instalación. Pero hoy en día muchas computadoras ya no cuentan con lector de CD o DVD. Es mejor idea descargar la distribución de Linux para su instalación en un USB. Esto no es sin más descargar el instalador y copiarlo en tu USB. Hay que hacer que en la memoria USB se genere un pequeño sistema Linux para que cualquier computadora pueda arrancar sin necesidad de sistema operativo propio. Es lo que se llama hacer un USB booteable (que sirve para hacer *boot*). Esta opción tiene, además de servir como dispositivo de instalación, otras dos ventajas:

- Te va a permitir probar la distribución de Linux con tu computadora sin necesidad de instalar nada. En el caso de Ubuntu, puedes conocer sobre esta posibilidad [aquí](https://tutorials.ubuntu.com/tutorial/try-ubuntu-before-you-install#0).
- Te permite disponer de un sistema operativo de auxilio en el caso de tener que diagnosticar, reparar, recuperar o reinstalar el SO de tu computadora.

En el caso de Ubuntu, el proceso para hacer un USB booteable de instalación está bien documentado. Es uno de los primeros pasos a dar en cualquier documentación que encuentres: ver el [proceso de instalación aquí](https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop#0), o [la creación del usb booteable aquí](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows#0).

Para usar el USB booteable debes tenerlo enchufado a la computadora antes de encenderla. Muy probablemente la bios de tu máquina esté configurada para darle prioridad al SO encontrado en un USB amtes que a los ubicados en el disco duro. Si es así, el instalador te guiará enseguida y podrás comenzar el proceso. Si no, debes modificar el orden de prioridad de los dispositivos de arranque en la bios o acceder a las opciones del menú de arranque de tu máquina, ya que habitualmente el fabricante habilita la posibilidad de iniciar desde el USB sin modificar la configuración de manera permanente.

En el caso de Ubuntu, lo primero que verás al arrancar con el USB será una ventana que te permite decidir entre probar Ubuntu o instalarlo:

<center><img src="https://i.stack.imgur.com/pNTOi.png" width="300"></center>

Si decides instalarlo, el proceso es guiado y sencillo. El mismo instalador te orientará en la toma de decisiones. Puede que la única decisión sobre la que necesites un poco de información es la creación de particiones.

### ¿Particiones? <a class="anchor" id="Particiones"></a>

Con respecto a la máquina sobre la que vas a hacer la instalación, casi la única decisión que debes tomar es si vas a hacer particiones en el disco duro, cúales y para qué. Una partición es un sector del disco duro que va a funcionar como volumen estanco e independiente. Estarás pensando: ¿como si fuera un nuevo disco dentro del disco duro? Si, exactamente así. Y puedes generar varias particiones. Podrías por ejemplo sobre el mismo disco instalar Windows y varias distribuciones de Linux, y decidir en el momento de arrancar la computadora qué sistema y partición quieres usar. O podrías, por ejemplo, decidir una política de cuotas de disco para algunas de tus carpetas de Linux creando, por poner un caso, un volumen de tamaño fijo para el directorio llamado 'home' y otro para 'opt', que no sea ocupado por otros directorios. Las posibilidades son muy diversas, pero nos centraremos aquí en el caso de que estés haciendo una sencilla instalación en tu computadora de trabajo. Puedes entonces encontrarte en uno de los siguientes escenarios.

#### Tengo Windows instalado y quiero además usar Linux.

Posiblemente tu máquina venía con un sistema Windows. Puede que quieras usarlo, además del Linux que vas a instalar.
Para esto puedes comenzar el proceso de instalación de Linux con Windows en tu disco duro. Este proceso guiado te comunicará en un determinado momento que se detectó otro sistema operativo y te ofrecerá la opción de instalar únicamente Linux, borrando todos los datos que hasta entonces se encuentran en tu computadora, o instalar Linux junto con Windows (en otra partición). En el caso de Ubuntu, la correspondiente pantalla del instalador se ve así:

<center><img src="Linux_data/Install-Ubuntu-Alongside-With-Windows.png" width="400"></center>

Debes elegir la primera opción, 'Install Ubuntu alongside Windows boot manager'.

#### Tengo Windows instalado pero sólo quiero usar Linux.

En este caso puedes, arrancando la computadora con el USB booteable, reformatear el disco duro para dejarlo limpio antes de la instalación. O puedes comenzar el proceso guiado con Windows en tu disco duro. Este proceso te comunicará en un determinado momento que se detectó otro sistema operativo y te ofrecerá la opción de instalar únicamente Linux borrando todos los datos que hasta entonces se encuentran en tu computadora (haz copia de seguridad de todo lo que quieres guardar antes de la instalación). En el caso de Ubuntu, la correspondiente pantalla del instalador es como la imagen de la subsección anterior, y debes elegir la segunda opción: 'Erase disk and Install Ubuntu'.

#### Mi máquina no tiene SO y quiero usar sólo Linux.

Este puede ser el caso más sencillo. Arranca la computadora con el USB booteable e inicia el proceso de instalación. Llegado el momento verás que tienes la opción de hacer una instalación únicamente de Linux sobre todo tu disco duro. En este caso el instalador tomará las decisiones de cómo reformatear y particionar el disco. Si estás instalando Ubuntu, esto es lo que verás:

<center><img src="Linux_data/erase-disk-and-install-ubuntu.png" width="400"></center>

Como se indica en la imagen, elige la opción que dice "Erase disk and install Ubuntu". Y continua el proceso de instalación guiada.

#### Mi máquina no tiene SO y quiero usar más de uno.

Lo primero en esta circunstancia es decidir cúanto espacio de disco duro vas a dedicar a cada SO. Además, si lo que quieres es instalar varias distribuciones de Linux, puedes tambien tomar la decisión de compartir particiones. Supongamos que quieres la carpeta 'Proyectos' como una única partición visible para tus distribuciones de Linux, por ejemplo. Lo puedes hacer. Pero aquí supondré que quieres instalar otro sistema operativo, como Windows, y hay que dejarle espacio. En este caso vas a tener que optar por definir manualmente tu esquema de particionado para instalar. En la imagen mostrada en la subsección anterior, haz click en "Something else". Aparecerá una ventana como la siguiente en la que decidir el tamaño y ubicación de las particiones:

<center><img src="https://i.stack.imgur.com/3DBJC.png" width="400"></center>

El proceso lo vas a encontrar muy bien documentado en webs como por ejemplo [esta](https://www.linuxtechi.com/ubuntu-18-04-lts-desktop-installation-guide-screenshots/). Vamos a mencionar aquí alguna cosa:

- Es recomendable que hagas una partición para el directorio 'boot'. Medio giga de memoria está más que bien para una gestión cómoda de una computadora personal.
- Hacer una partición para '/home' también puede ser buena idea, aunque no necesario. Tener el resto en su propia partición puede evitar disgustos al ocupar mucho espacio con tus cosas no dejando espacio para el sistema.
- Puedes hacer una partición para todos los directorios, o los directorios restantes, designandola como punto de anclaje de '/'.
- Aunque ya no es muy necesaria, todavía debemos definir una partición de memoria auxiliar de intercambio *swap*. Existen guías y criterios para definir su tamaño, pero como regla del pulgar podemos elegir la misma cantidad de memoria que tenemos de RAM.

El último concepto, la memoria swap, merece a continuación un párrafo ya que será una partición con la que no vas a interaccionar explícitamente. Pero antes verás que para crear una partición, además de su tamaño, debes elegir la naturaleza de su gestión de ficheros.

### El sistema de ficheros.

[Qué es el *journaling* o el *journal file system*](https://help.ubuntu.com/community/LinuxFilesystemsExplained) es algo que escapa a los objetivos de este notebook. Puedes buscar información para comprender los detalles. Es recomendable que alguna vez lo hagas. Pero para poder culminar el proceso de instalación correctamente debes saber que existen distintas estrategias de gestión de ficheros en disco que pueden condicionar su uso. [Desde finales de los 70 y hasta los 90 Dos y Windows manejaban el sistema FAT (FAT12, FAT16 y FAT32)](https://web.archive.org/web/20150925082826/http://www.wizcode.com/articles/comments/a-brief-introduction-to-fat-file-allocation-table/). Su origen estaba motivado por cómo indexar la organización de ficheros en un disco Floppy blando. Te puedes imaginar que a medida que los ficheros crecían en tamaño y los soportes en capacidad de memoria, hubo que diseñar nuevas estrategias. [FAT12 tenía una limitación de tamaño máximo de partición de 32 MB, FAT16 ya permitía un tamaño máximo de fichero de 2GB y FAT 32 de 4GTB](http://www.ntfs.com/ntfs_vs_fat.htm). Hoy día Windows maneja un protolo llamado NTFS que permite gestionar ficheros de tamaño máximo 16TB -por hablar de algo que nos puede afectar directamente-. Sin embargo Linux adoptó desde el principio otro tipo de estrategias, [desde EXT2 a comienzos de los 90 hasta el día de hoy en el que la mayoría de distribuciones para computadora de escritorio hacen uso de EXT4](https://opensource.com/article/18/4/ext4-filesystem) ([aunque existen otros tipos de sistemas de fichero que pueden adoptar las computadoras de cálculo intensivo o los servidores](https://en.wikipedia.org/wiki/Comparison_of_file_systems)).

Dicho esto, te preguntarás: Bien, ¿Pero qué sistema debo de elegir cuando creo las particiones? [En caso de duda, y para un uso común, la mejor opción ahora mismo es EXT4 para todas tus particiones de Liinux (menos la de memoria swap)](https://www.howtogeek.com/howto/33552/htg-explains-which-linux-file-system-should-you-choose/).

### La memoria Swap.

En Linux, desde las primeras distribuciones, se recomienda generar una partición de disco duro que se usará como area de intercambio temporal en el caso de que la memoria RAM se haya ocupado. Se llama memoria Swap. Obviamente el uso del disco duro para memoria de ejecución de procesos es algo muy lento, pero efectivo en caso de rescate. Si estás trabajando con un disco de estado sólido, el escenario cambia, ya que es de lectura y escritura mucho más rápida. Pero si no, cuando tengas muchas aplicaciones abiertas o estés ejecutando un programa que requiera un gran manejo de datos en memoria, notarás, si la memoria RAM se agota, como la computadora se vuelve muuuuy lenta... no se colgará, pero se vuelve extremadamente lenta mientras migra ciertos datos de la memoria RAM a la Swap. Esta situación entonces no es del todo catastrófica, te dejará margen para que elimines el proceso que aumentó el consumo. Después, suele tardar un tiempo en recuperar el comportamiento normal y puede que por el camino haya algún proceso dando mensajes de que no responde. Puedes leer un poco más sobre la swap [aquí](https://hipertextual.com/2015/09/swap-en-linux), [aquí](https://blog.desdelinux.net/que-es-el-swap-en-linux-y-como-utilizarlo/), [aquí](http://culturacion.com/que-es-una-particion-swap/) o [aquí](http://web.mit.edu/rhel-doc/3/rhel-sag-es-3/ch-swapspace.html).

[¿Cúanta memoria entonces tienes que dedicar a tu Swap?](https://maslinux.es/cuanto-swap-deberia-usarse-en-gnu-linux/) No hay una respuesta clara. También podemos [preguntarnos si efectivamente esta memoria es necesaria cuando ya la RAM que tienes en la computadora tiene un tamaño razonable](https://geekytheory.com/es-necesaria-una-particion-swap-en-linux). El consejo que podemos dar es que si tienes un disco duro de más de 1 Tera, no te va a hacer daño crear una partición Swap, y el tamaño puede ser entre una y dos veces la cantidad de memoria RAM que tienes. En mi caso, en la laptop tengo 8 GB de RAM y una Swap de otros 8 GB, y para el uso que le doy es suficiente. En la computadora de escritorio tengo 64 GB de RAM y 16 GB de Swap, aunque más de 8 GB de Swap puede ser innecesario, ya que la uso para hacer cálculos más demandantes y prefiero prevenir.

## ¿Puedo usar además otros sistemas operativos en la misma máquina? <a class="anchor" id="Otros_SOs"></a>

Hemos mencionado en la sección anterior que sí es posible instalar en el mismo disco duro, en particiones distintas, Linux junto con otros sistemas operativos (u otras distribuciones de Linux). Al iniciar la computadora, un menú te dará la opción de elegir con qué sistema operativo quieres trabajar. La desventaja quizá puede ser que para ejectuar una aplicación que tienes en tu partición de Windows, por ejemplo, debes de cerrar tu sesión en Ubuntu y reiniciar la máquina. No es tan cómodo pasar de uno a otro si sólo es para cuestiones puntuales y sencillas. Para simultanear sobre la misma sesión de tu computadora varios sistemas operativos, existe otra opción: los sistemas operativos virtuales.

### Sistemas operativos virtuales.

Imagina que puedes abrir Ubuntu desde tu sistema operativo Windows como si fuera una aplicación más. O al revés, que sobre tu distribución de Linux puedes abrir y cerrar una sesión en Windows u otro sistema operativo como si fuera un programa más. Esto es lo que posibilitan la instalación de máquinas virtuales como [VirtualBox](https://www.virtualbox.org/) de Oracle -gratuito-. Esta máquina virtual la puedes instalar en tu sistema operativo y crear computadoras virtuales con un espacio de disco duro asignado y con una gestión del hardware de tu computadora independiente a la que realizará tu SO de soporte. Si nunca has usado Linux, esta puede ser una buena manera para comenzar asumiendo poco riesgo: puedes aprender a usar una distribución como Ubuntu como si fuera una ventana más abierta en tu escritorio. 

### Compatibilidad de ficheros.

Otro inconveniente similar al mencionado anteriormente, puede ser el acceso a ficheros en particiones de sistemas distintos. Supongamos que tienes una partición en Linux y otra en Windows. Imagina que trabajando en Linux, con todas tus terminales y aplicaciones abiertas, necesitas acceder a la información de un archivo de la partición en Windows. ¿Tienes que cerrar tus aplicaciones, reiniciar en Windows, leer el fichero, y volver a Linux? Puede que te parezca acertada esa suposición pensando además que ambas particiones fueron formateadas con sistemas de ficheros distintos, seguramente EXT4 y NTFS. Pero no, no es necesario. Linux puede acceder a otros volúmenes con otros sistemas de ficheros. Así puedes "montar" tu volumen de Windows y tener acceso al menos seguramente para lectura. Y si dicho volumen fue formateado en otro sistema como vFAT32, es posible también escribir. Puedes checar qué sistema de ficheros puede ser leido y/o escrito desde qué sistema operativo en la tabla denominada "OS support" en [la comparación reportada en Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_file_systems).

### Usando una memoria usb compatible con distintos SOs.

Si leiste la sección anterior entenderás entonces que si vas a formatear una memoria USB para uso indistintamente en Linux, Windows y MacOS, no sirve hacerlo en cualquier sistema de ficheros. Puedes encontrar [tablas en internet en las que consultar qué formato debe tener tu memoria USB para ser leida con los sistemas operativos que trabajas](https://www.7dayshop.com/blog/operating-systems-and-file-systems-cross-compatibility-windows-apple-linux-playstation-xbox-android/). En principio, tu memoria de 16 o 32 Gb para ser usada sin problema en los tres SOs anteriormente citados, debería ser formateada como FAT32.

## La instalación de software <a class="anchor" id="Instalacion_software"></a>

A través de la terminal puedes instalar software. Seguramente ya aprendiste a hacerlo mediante tu entorno de escritorio, pero puede ser muy útil conocer que también puedes llevar la gestión de los paquetes de software instalados en tu computadora a través del terminal.

En este punto, dado que esto sí depende de la distribución de Linux que estés usando, pondremos aquí los comandos útiles para el caso de Ubuntu y CentOS:

### Ubuntu

Para actualizar la lista de paquetes disponibles en los repositorios:

```bash
sudo apt update
```

Seguramente has tenido que introducir tu contraseña en la terminal. Más adelante veremos qué significa el comando `sudo`. Ahora, para actualizar los paquetes que encuentran una versión superior en los repositorios:

```bash
sudo apt upgrade
```

Para instalar un paquete:

```bash
sudo apt install nombre_paquete
```

La lista de repositorios que tienes configurada en el sistema la puedes encontrar en el siguiente fichero:

```bash
less /etc/apt/sources.list
```

### CentOS

Para actualizar la lista de paquetes disponibles en los repositorios:

```bash
yum check-update
```

Para actualizar los paquetes que encuentran una versión superior en los repositorios:

```bash
yum update
```

Para instalar un paquete:

```bash
yum install nombre_paquete
```

La lista de repositorios que tienes configurado en el sistema la puedes encontrar en el siguiente directorio:

```bash
ls /yum/yum.repos.d
```

## La organización de ficheros del sistema Linux. <a class="anchor" id="organizacion"></a>

En el sistema operativo Linux la organización de archivos tiene forma de arbol. E independientemente de dónde está físicamente alojado un directorio (puedes jugar con distintos discos duros) su localización debe estar incluida en esta estructura anidada que parte de un punto, o directorio supremo, llamado '/' o directorio raiz. En '/' encontramos el primer nivel de directorios en esta estructura jerárquica. En este nivel todas las distribuciones suelen tener los mismos directorios. Vamos a comentar alguno de ellos por orden alfabético:

#### /bin
Es la carpeta que almacena los comandos y ejectables, scripts o binarios, del sistema que usarán todos los usuarios de la máquina. De muchos de ellos hablaremos en una sección posterior.

#### /boot
Es la carpeta que resguarda el gestor de arranque del sistema y sus instrucciones. El núcleo del sistema ('kernel') va a tener actualizaciones independientemente de la versión de la distribución de Linux. Cuando enciendes la computadora, si tienes varios kernels y además algún otro sistema operativo, aparecerá un menú en el que puedes elegir con qué iniciar la computadora. Eso es el gestor de arranques, y la información que gestiona está en '/boot'.

#### /dev
En Linux cada dispositivo, físico o virtual, o pieza de hardware tiene un archivo de llamada. Esos archivos están todos en la carpeta '/dev'. Podemos encontrar allí archivos que hacen referencia a las CPUs, GPUs, USBs, la red, etc. Usualmente un usuario no administrador no tiene motivo ninguno para operar con estos ficheros.

#### /etc
Puedes encontrar documentación en internet que argumenta que en su origen el directorio '/etc' almacenaba todos aquellos ficheros que no encontraban su lugar en cualquier otro directorio contenido en '/'. Puede que de ahí venga su nombre. Pero hoy en día '/etc' resguarda de manera ordenada la mayoría de archivos de configuración de software y servicios del sistema.

#### /home
Si eres un usuario con poca motivación por convertirte en administrador experto de tu sistema operativo, esta es tu carpeta. '/home' contiene en su interior un directorio por usuario. Lo que coloquialmente se conoce como el directorio hogar o 'home' de cada usuario. Vamos a suponer que tu nombre de usuario es 'chewbacca', encontrarás una carpeta llamada '/home/chewbacca' que será tu espacio de almacenamiento y trabajo.

#### /lib
Aquí encontramos módulos del o los kernels y librerías que en muchas ocasiones van a ser usadas de manera compartida entre varios procesos, servicios o programas.

#### /media
Como hemos descrito en el párrafo dedicado a '/dev', cada dispositivo viene anclado a la estructura de ficheros como un archivo o directorio. '/media' es el directorio que centraliza los puntos de anclaje de los dispositivos 'removibles' como el cdrom, unidades de memoria externas, etc.

#### /mnt
Puede haber, comprensiblemente, un poco de confusión entre '/mnt' y '/media'. Ya que ambos directorios alojan archivos de anclaje de periféricos, pero '/mnt' suele ser para dispositivos temporales y de usuarios específicos. Aunque esta regla no siempre se cumple.

#### /opt
Es el lugar de almacenamiento del software instalado ajeno al sistema y de uso para todos los usuarios.

#### /proc
No sólo los dispositivos físicos tienen un punto de anclaje, también los virtuales y los procesos mismos. '/proc' almacena archivos de información del sistema y una larga lista de directorios etiquetadas por números: PIDs. El PID es el número de identificación de proceso. Cualquier cosa que se ejecuta en la computadora se registra como un proceso con un PID. Esas carpetas por lo tanto tienen en su interior todo la información relacionada con la ejecución de cada proceso. 

#### /root
Directorio "home" para el superusuario 'root'. Más adelante se dedica una sección al superusuario 'root'.

#### /sbin
Este directorio es similar a '/bin'. Es último almacena comandos útiles para todo usuario, mientras que en 'sbin' podemos encontrar los ejecutables (comandos) de administración y gestión del sistema.

#### /sys
Aquí podemos encontrar toda la información relacionada con el hardware y los módulos de los kernel instalados.

#### /tmp
Este directorio sirve de archivo temporal para ficheros. Su contenido es borrado cada vez que se reinicia el sistema.

#### /usr
Este directorio es seguramente el más poblado en número de ficheros. '/usr' contiene una estructura similar a la que tiene '/', y sirve para almacenar de manera organizada las partes de los paquetes y software instalados por los usuarios, no por el administrador ni por el mismo sistema.

#### /var
Contiene ficheros auxiliares del sistema, usualmente 'logfiles' que reportan la salida en tiempo real de muchos de los servicios del sistema como impresión, mail interno, procesos internos, etc.

Como ves no es que Linux tenga 'una' carpeta que se llame 'sistema'. Más bien hay una carpeta que alberga todo el espacio de almacenamiento privado de cada usuario ('/home') y el resto es una estructura de archivos optimizada para asegurar el funcionamiento del sistema operativo a varios usuarios ejecutando varios procesos simultaneamente.

## Entornos de escritorio.

Si estás aproximándote a Linux desde hace poco es posible que confundas los entornos de escritorio con las distribuciones. El entorno de escritorio es la parte más visible de la distribución y lo primero con lo que probablemente vas a interaccionar: el escritorio, la barra superior, el menú desplegable, el docker, las ventanas, etc. Hay entornos de escritorio tradicionales, tan populares como sólidos, como son [Gnome](https://www.gnome.org/) ([proyecto fundado por los mexicanos](https://www.xataka.com.mx/aplicaciones/miguel-de-icaza-y-federico-mena-los-padres-mexicanos-del-proyecto-gnome-uno-de-los-entornos-de-escritorio-mas-famosos-de-linux) [Miguel de Icaza](https://en.wikipedia.org/wiki/Miguel_de_Icaza) y [Federico Mena](https://es.wikipedia.org/wiki/Federico_Mena)) o [KDE](https://www.kde.org/), y otros más novedosos y vistosos como [Pantheon](https://www.fosslinux.com/4652/pantheon-everything-you-need-to-know-about-the-elementary-os-desktop.htm/), o ligeros y sencillos como [XFCE](https://www.xfce.org/). Aunque las distribuciones apuestan por que uno u otro venga instalado por defecto, y a veces desarrollan su propio entorno de escritorio (como hizo Ubuntu con [Unity](https://unity8.io/) o Elementary con Pantheon), casi todos los entornos de escritorio pueden ser instalados en cualquier distribución. Es por esto que no debería de condicionar tu elección de distribución, puedes [instalar Pantheon en Ubuntu](https://www.maketecheasier.com/install-run-pantheon-desktop-ubuntu/) o descargar [KUbuntu -Ubuntu con KDE-](https://kubuntu.org/), aunque por defecto ahora venga con GNOME.

## La terminal y la sintaxis de Bash.

Probablemente estés habituado/a a interaccionar con tu computadora a través del entorno gráfico de escritorio. Resulta muy intuitivo y casi no requiere proceso de aprendizaje, pero consume muchos recursos y es altamente ineficiente cuando la computadora es tu herramienta para algo más que el uso de una o dos herramientas de ofimática.

La terminal es esa ventanita monocolor que sólo contiene texto y cuya última linea siempre acaba con un cursor parpadeante que puede resultar al principio intimidante... ya que aparece y desaparece intermitentemente como diciendote: ¿y ahora qué? Pues bien, efectivamente es la puerta de entrada a la interacción con tu máquina. El cursor espera comandos, y esa lista de comandos que entiende son un lenguage, con sus reglas sintácticas, que debes aprender para comunicarte con tu máquina. El lenguage que puebla por defecto la mayoría de los sistemas Linux se llama Bash. ¿Es el único? No, hay otros lenguages para la terminal más sofisticados como Zsh o Fish, pero Bash es el interpretador más común y el que únicamente usarás a lo largo de tu vida si no es que eres una persona muy curiosa o alcanzas un nivel de experiencia como para encontrar los límites e incomodidades del uso de Bash.

Antes de hablar de qué vamos a escribir en la terminal, hagamos un breve comentario sobre lo que precede al cursor en la terminal. Ese fragmento de texto que no desaparece por mucho que le demos a la tecla 'entrar' se llama 'prompt'. Es perfectamente configurable y personalizable y habitualmente suele contener el nombre del usuario que está operando la terminal, el nombre de la máquina precedido del símbolo '@' (muy util cuando en la misma terminal hacemos conexiones remotas con otras máquinas) y por último la dirección o 'path' del archivo en el que nos encontramos en la terminal. Esto nos lleva otro concepto que usaremos como punto de inicio en nuestro aprendizaje de Bash: la navegación de ficheros.

### La navegación de ficheros. <a class="anchor" id="navegacion_ficheros"></a>

La terminal es una herramienta poderosísima. Todo lo que necesitas hacer con la computadora se puede hacer a través de la terminal, no requieres el entorno gráfico para casi nada. Y la navegación de ficheros es probablemente lo menos relevante pero lo más sencillo de entender para comenzar a sentirte cómodo o cómoda con la terminal.

Como decíamos en la sección anterior, el sistema de archivos tiene estructura de árbol y podemos escribir la secuencia de directorios que contienen, como muñecas rusas, el fichero con el que queremos trabajar. A esta dirección, o secuencia de directorios, se le llama camino o 'path'. Si el 'path' comienza en el directorio raiz, se dice que el path absoluto. Si sin embargo se trata del recorrido que tenemos que hacer desde el directorio en el que se encuentra la terminal u otro directorio, se dice path relativo -efectivamente path es una palabra tan comunmente usada en este contexto he dejado de entrecomillarla-.

Vamos a hacer una serie de ejercicios que nos ayuden a introducir la navegación de ficheros, su sintaxis y los comandos más útiles. Comencemos abriendo una terminal. Para esto suele funcionar las primeras veces acudir al menú de aplicaciones de tu entorno de escritorio, aunque poco a poco sentirás la necesidad de usar una combinación de teclas que rápidamente, sin mover la mano al ratón, te dispare terminales nuevas. En el caso de Gnome y Ubuntu, esta es 'ctrl'+'alt'+'t'.

En este momento tienes una terminal expectante a tus ordenes. Ves tu nombre de usuario, el nombre de tu máquina, y no me equivocaré mucho si predigo que estás viendo el símbolo '\~' entre ':' y '\\$'. Ese simbolo, llamado virgulilla, se usa como álias de tu 'home'. Es decir, si tu usuario, cómo decíamos anteriormente, se llama 'chewbacca', '\~' es lo mismo que '/home/chewbacca'. Y el espacio en el 'prompt' entre ':' y '\\$' está dedicado a contener el path del directorio en el que se encuentra la terminal. Si de todas formas te desorientas, o tu prompt no es lo suficientemente explícito, existe un comando que imprime en la terminal el path en el que te encuentras: `pwd` (del inglés *print working directory*). Ejecútalo y comprueba la relación entre '\~' y tu 'home':

```bash
pwd
```

Para listar el contenido de un directorio disponemos del comando `ls`. Ejecútalo para ver los ficheros y directorios que se encuentran en tu home.

```bash
ls
```

Ya conoces tus dos primeros comandos. Si has leido la sección previa llamada [*La organización de ficheros del sistema Linux*](#organizacion), puede que estés pensando: ¿Estos son comandos que se encuentran en algún sitio? Si, en '/bin'. A ver si los encuentras allí:

```bash
ls /bin
```

Puedes ahora ver el contenido de tu directorio raíz:

```bash
ls /
```

O de nuevo, pero de otra forma, el contenido de tu directorio hogar:

```bash
ls ~
```

Ahora veamos como cambiar de directorio. El comando `cd` (del inglés *change directory*) ubica la terminal en el directorio que le digamos. Por ejemplo, podemos movernos al directorio raiz '/' y descubrir los directorios que hay en él y que se han relatado en la sección [*La organización de ficheros del sistema Linux*](#organizacion):

```bash
cd /
ls
```

También `cd` tiene ciertos atajos. Por ejemplo, `cd` solito te lleva a tu directorio hogar:

```bash
cd /bin
pwd
cd
pwd
```

Ahora imaginemos que existe un directorio llamado 'dir4' ubicado en el directorio 'dir3', que a su vez está ubicado en 'dir2', ubicado en 'dir1', contenido en el directorio raíz '/'. Se dice que su path absoluto es '/dir1/dir2/dir3/dir4', ya que desde cualquier ubicación `cd /dir1/dir2/dir3/dir4` nos lleva a 'dir4'. Vamos a hacer un ensayo, y para ello vamos a crear en tu directorio hogar la carpeta 'dir3' y dentro de ella 'dir4'.

```bash
cd # puedes hacer después `pwd` comprobar dónde estás
mkdir dir3
cd dir3 # puedes hacer después `pwd` comprobar dónde estás
mkdir dir4
cd dir4 # puedes hacer después `pwd` comprobar dónde estás
```

Hemos visto, de paso, que `mkdir` sirve para crear directorios. Vamos ahora a cambiar nuestra ubicación en la terminal a un directorio cualquiera como puede ser `/usr` para después regresar, haciendo uso de su path absoluto, a `dir4`.

```bash
cd /usr
pwd
cd /home/diego/dir3/dir4
pwd
```

Ahora que ya sabemos lo que es el path absoluto, veamos cómo nos podemos mover en el árbol de ficheros con paths relativos. Anteriormente hemos visto como subir un fichero en la jerarquía de la estructura. Si estamos por ejemplo en nuestro 'home' basta con mencionar uno de los directorios que contiene para entrar en el:

```bash
cd ~ # o sólamente cd
pwd
cd dir3
pwd
cd dir4
```

¿Y cómo retrocedemos? ¿Cómo descendemos en la estructura de ficheros hasta llegar a la raíz '/'? Supongamos que estamos en 'dir4', usamos `..` para descender un nivel -al directorio anterior-:

```bash
cd ~/dir3/dir4
pwd
cd ..
pwd
cd ..
pwd
cd ..
pwd
```

Puedes usarlo también de manera combinada para descender más de un nivel:

```bash
cd ~/dir3/dir4
pwd
cd ../..
pwd

cd ~/dir3/dir4
cd ../../..
pwd
```

Puedes también construir paths que indican una ruta de cambio de directorio según el punto en el que estés, paths relativos:

```bash
cd ~/dir3/dir4
pwd
cd ../../../../usr/local
pwd
cd ../../bin
pwd
cd ../home/diego/../diego/../diego/dir3/../../diego/dir3/dir4
pwd
```

Por último, y para completar la sintaxis que debes conocer para moverte en el sistema de ficheros, así como `..` quiere decir *el directorio anterior*, `.` quiere decir *aquí*:

```bash
cd
pwd
cd .
pwd
cd dir3/dir4/.
pwd
```

### Otros comandos útiles en la gestión de ficheros: touch, mv, rm y rmdir. <a class="anchor" id="mv_rm"></a>

Para borrar un directorio vacío podemos hacer uso del comando `rmdir`:

```bash
cd ~/dir3/.
rmdir dir4
cd ..
rmdir dir3
pwd
ls
```

Ahora, para crear ficheros -vacíos- podemos usar el comando `touch`:

```bash
cd
ls
touch foo1
touch foo2
touch foo3
ls
```

Para borrar cualquier tipo de fichero usamos `rm`. Recuerda que `rmdir` borra únicamente directorios vacios.

```bash
cd
ls
rm foo1 foo2 foo3
ls
```

Para renombrar o mover un fichero o directorio contamos con el comando `mv` (del inglés *move*):

```bash
cd
ls
mkdir zaragoza79
touch zaragoza79/foo
ls zaragoza79
mv zaragoza79 méxico16
ls méxico16
mv méxico16/foo .
ls
ls méxico16
rmdir méxico16
rm foo
```

Nota que para borrar el directorio 'méxico16' no hemos hecho uso del comando 'rmdir', ya que únicamente funciona con directorios vacíos. Para borrar `méxico16` hacemos un borrado recursivo con `rm -r`. `-r` otorga efecto sobre el directorio y todo su contenido.

Para terminar con la navegación de ficheros, veamos ciertos caracteres comodín (en inglés *wildcard*) muy utiles para hacer la gestión de ficheros más cómoda. Veamos si puedes deducir para qué podemos emplear el carácter `?` y el carácter `*` introducido en un path:

```bash
cd
ls
mkdir dir10 dir20 dir30 dir01 dir02 dir03
ls
rmdir dir?0
ls
rmdir dir0?
ls
```


```bash
cd
ls
touch x1xpatatas x1xpatos x1xpatotas x1xpatitos
ls
rm x1xpat?tas
ls
rm x1xp*
ls
touch x1xpatatas x1xpatos x1xpatotas x1xpatitos
rm x1xpat?t*
ls x1x*
rm x1x*
```

Tienes más ejemplos del uso de los comodines en internet en páginas como [esta](https://kompjuteras.com/en/wildcards-in-linux-commands-with-practical-examples/) o [esta](https://www.tecmint.com/use-wildcards-to-match-filenames-in-linux/).

### echo, less y more. <a class="anchor" id="echo"></a>

Antes de ver en acción dos comandos muy útiles para visualizar el contenido de un fichero, veamos que hace el comando `echo`.
`echo` imprime por pantalla el texto que pongamos a continuación:

```bash
echo "hola!"
```

A la salida por terminal se llama `stdout` (del inglés *standard output*). Podemos redirigir la salida por `stdout` del comando a un fichero con el carácter `>`:

``` bash
echo "hola!" > mi_nuevo_fichero
```

Ahora, para visualizar el contenido del fichero, es donde aparecen los comandos `less` o `more`. Los dos sirven para lo mismo aunque `less` se inventó más tarde superando en funcionalidad a `more`. Es por eso que se llamó `less`, por el dicho inglés: *less is more*.

``` bash
more mi_nuevo_fichero
```

```bash
less mi_nuevo_fichero
# Presiona la tecla 'q' para volver a la terminal
``` 

Pero el desvío de `stdout` a un fichero mediante `>` tiene una peculiaridad, siempre reescribe el fichero:

```bash
echo "Hola Liliana" > mi_nuevo_fichero
more mi_nuevo_fichero

echo "Hola Carmen" > mi_nuevo_fichero
more mi_nuevo_fichero

echo "Hola Homero" > mi_nuevo_fichero
more mi_nuevo_fichero

echo "Hola Angel" > mi_nuevo_fichero
more mi_nuevo_fichero
```

Si quieres que las entradas vayan registrandose en el fichero de manera concatenada, has de usar `>>`:

```bash
echo "Hola Liliana" > mi_nuevo_fichero
echo "Hola Carmen" >> mi_nuevo_fichero
echo "Hola Homero" >> mi_nuevo_fichero
echo "Hola Angel" >> mi_nuevo_fichero
more mi_nuevo_fichero
```

Una última cosa, si `more` saca por pantalla el contenido de un fichero, ¿podemos desviar su salida estandard a otro fichero?

```bash
more mi_nuevo_fichero > otro_fichero
more otro_fichero
```

### cat y paste para concatenar ficheros.

Hagamos ahora un fichero con una columna de números y otro fichero con una columna de letras:

```bash
echo "1" > fichero_numeros
echo "2" >> fichero_numeros
echo "3" >> fichero_numeros
echo "4" >> fichero_numeros
more fichero_numeros
```

```bash
echo "a" > fichero_letras
echo "b" >> fichero_letras
echo "c" >> fichero_letras
echo "d" >> fichero_letras
more fichero_letras
```

Dejaré ahora que adivines el efecto de los comandos `cat` y `paste` cuando se aplican sobre más de un fichero:

```bash
cat fichero_numeros fichero_letras
```

```bash
paste fichero_numeros fichero_letras
```

O volcando la salida a un fichero:

```bash
cat fichero_numeros fichero_letras > nuevo_fichero
more nuevo_fichero
```

```bash
paste fichero_numeros fichero_letras > nuevo_fichero
more nuevo_fichero
```

### El reconocimiento y filtrado de texto: grep, awk y sed. <a class="anchor" id="grep"></a>

Algo que harás habitualmente es el filtrado y reconocimiento de texto directamente desde la línea de comandos. Vamos a presentar en esta sección tres herramientas que pueden serte de utilidad. La primera, `grep`, filtra de manera muy sencilla líneas según contengan o no el patrón que estás buscando. Un ejemplo:

```bash
echo "Paso 0   Energía 10.4" > Experimento_626.oup
echo "Paso 0   Temperatura 303" >> Experimento_626.oup
echo "Paso 1   Energía 10.2" >> Experimento_626.oup
echo "Paso 1   Temperatura 300" >> Experimento_626.oup
echo "Paso 2   Energía 10.5" >> Experimento_626.oup
echo "Paso 2   Temperatura 306" >> Experimento_626.oup
echo "Paso 3   Energía 10.1" >> Experimento_626.oup
echo "Paso 3   Temperatura 299" >> Experimento_626.oup
echo "Paso 4   Energía 10.8" >> Experimento_626.oup
echo "Paso 4   Temperatura 302" >> Experimento_626.oup
echo "Paso 5   Energía 10.1" >> Experimento_626.oup
echo "Paso 6   Temperatura 304" >> Experimento_626.oup
```

Podemos fácilmente filtrar las líneas que contienen o no la palabra *Temperatura*:

```bash
grep 'Temperatura' Experimento_626.oup > Temperatura_Experimento_626.oup
grep -v 'Temperatura' Experimento_626.oup > Energía_Experimento_626.oup
```

```bash
more Temperatura_Experimento_626.oup
more Energía_Experimento_626.oup
```

En la terminal de Linux la salida de un comando se puede redireccionar como la entrada de otro comando. Por ejemplo, podemos filtrar `stdout` como si de un fichero se tratara:

```bash
less Energía_Experimento_626.oup | grep '10.1' > Energía_10.1_Experimento_626.oup
```

De hecho, es lo que hacemos cuando escribimos la salida de la línea anterior a un fichero, porque lo podríamos dejar únicamente como:

```bash
less Energía_Experimento_626.oup | grep '10.1'
```

Así por ejemplo podemos concatenar filtros:

```bash
less Experimento_626.oup | grep 'Energía' | grep '10.1'
```

El segundo comando que vemos aquí, `awk`, es un poco más sofisticado a la hora de hacer búsqueda de patrones de texto. Vamos a poner un ejemplo:

```bash
echo "Paso 0   Energía 10.4" > Experimento_626.oup
echo "Paso 0   Temperatura 303  Distancia 8.2" >> Experimento_626.oup
echo "Paso 1   Energía 10.2" >> Experimento_626.oup
echo "Paso 1   Temperatura 300  Distancia 8.1" >> Experimento_626.oup
echo "Paso 2   Energía 10.5" >> Experimento_626.oup
echo "Paso 2   Temperatura 306  Distancia 8.0" >> Experimento_626.oup
echo "Paso 3   Energía 10.1" >> Experimento_626.oup
echo "Paso 3   Temperatura 299  Distancia 7.8" >> Experimento_626.oup
echo "Paso 4   Energía 10.8" >> Experimento_626.oup
echo "Paso 4   Temperatura 302  Distancia 7.6" >> Experimento_626.oup
echo "Paso 5   Energía 10.1" >> Experimento_626.oup
echo "Paso 5   Temperatura 304  Distancia 7.5" >> Experimento_626.oup
```

Filtremos, como primer caso, según el número de campos. Antes de nada usemos `awk` para sacar por pantalla el número de campos por línea después de las dos primeras columnas

```bash
awk '{print $1, $2, NF}' Experimento_626.oup
```

Filtremos entonces las líneas que contienen sólo 4 campos:

```bash
awk '{if (NF==4) print $0}' Experimento_626.oup
```

Ahora, como último ejemplo que ilustra para qué puedes emplear `awk`, filtremos las líneas en las que existe el patrón *Distancia* y su valor es menor o igual que 8.0, e imprimamos dicho valor precedido únicamente del índice de paso:

```bash
awk '/Distancia/ {if ($6<=8.0) print $2, $6}' Experimento_626.oup
```

Ninguno de los dos comandos anteriores remplaza texto, bueno, con `awk` se puede. Pero `sed` puede ser otra alternativa a usar con este propósito. Veamos un ejemplo sencillo de substitución de texto con `sed`. En este caso, la palabra *Distancia* por la palabra *Posición*.

```bash
sed 's/Distancia/Posición X/g' Experimento_626.oup
```

Puede que la sintaxis de estos comandos te pueda parecer un poco complicada pero en internet es fácil encontrar tutoriales sobre su uso. Tanto `awk` como `sed` son herramientas muy poderosas para el tratamiento de patrones de texto. Hacen lo que hemos visto anteriormente, y mucho más. En principio no te recomiendo que te detengas ahora para hacerte un super experto o experta de `awk`, por ejemplo. Es mejor que continues tu proceso de formación y cuando tengas la necesidad de usar el comando encuentres un tiempo para saber más. Por el momento, es suficiente saber que existe y qué es lo que hace. 

### top, ps y kill. <a class="anchor" id="top"></a>

Anteriormente, a propósito del directorio `/proc` dijimos que todo proceso ejecutado por la computadora lleva asociado un número como identificador, el PID. El comando `top` nos lista los procesos regitrados activos, durmientes o suspendidos:

```bash
top
```

El mismo `top` nos permite por ejemplo "matar" un proceso que se ha podido quedar colgado o está dando problemas. O sencillamente queremos abortarlo por algún motivo. Veremos esto más adelante, en esta sección. Vamos a configurar una sencilla situación de ejemplo para ilustrar esto.

Anteriormente hemos visto que `more` saca todo el contenido del fichero en la terminal, pero a veces el fichero es excesivamente largo. Si lo visualizas con `more` todas las líneas aparecerán en tu terminal, haciendo muy incomodo que quieras regresar en ella a ver tu historial de comandos. Para poder navegar mejor en la visualización del fichero, porque *less is more* -un dicho inglés-, `less` nos permite ir adelante y hacia atrás en la salida del fichero, e incluso hacer búsqueda de patrones de texto sin afectar la terminal. Por eso `less` la secuestra, como si hubieramos abierto un programita que no tiene salida gráfica y con el que se interacciona por la misma ventana que la terminal (de hecho, así es). Para salir de `less` basta con presionar la tecla 'q', pero vamos a imaginar ahora que `less` no responde... se atoró porque el fichero es muy grande. Le hemos pedido por ejemplo a `less` que haga una búsqueda de patrón de texto, pero la cantidad de información es tanta que le está tomando mucho tiempo y nos hemos arrepentido... haremos la búsqueda con `awk`. ¿Cómo interrumpimos el proceso? ¿Cómo lo matamos?

Vamos a generar, antes que nada, nuestro gran fichero. Veremos más adelante que Bash es un lenguage de programación donde puedo hacer todo tipo de cosas, como bucles por ejemplo:

```bash
for i in `seq 1 10`;
   do
      echo $i
   done
```

o lo que es lo mismo:

```bash
for i in `seq 1 10`; do echo $i; done
```

Vamos a emplear un bucle para hacer un gran fichero de un 10 millones de números aleatorios -le costará un minuto escribirlo en disco-:

```bash
for i in `seq 1 10000000`; do echo "En la linea" $i "el número aleatorio" $RANDOM >> numeros_aleatorios.txt ; done
```

El fichero es grande. Pesa más de 400 megas. Puedes ver el tamaño que ocupa en disco con el comando:

```bash
du -sh numeros_aleatorios.txt
```

Y si quieres saber cuantas líneas o caracteres tiene:

```bash
wc -l numeros_aleatorios.txt
wc -c numeros_aleatorios.txt
```

Ahora vamos a abrirlo con `less` para buscar la línea que contiene el patrón `la linea 1000000`. Para ello:

```bash
less numeros_aleatorios.txt
```

Con `less` abierto sobre nuestro fichero teclea `/la linea 1000000` y presiona la tecla 'entrar'. Verás que tarda un par de segundos en leer secuencialmente el fichero hasta que encuentra el texto que buscamos. Busquemos ahora '10000000'. Para repetir la operación desde el principio, sal de `less` con la tecla 'q', vuelve a abrir el fichero y teclea `/10000000`. Verás que tarda un poquito. Vamos a suponer que queremos abortar la búsqueda porque el fichero es excesivamente grande. Con `less` abierto sobre nuestra terminal vamos a encontrar buscar su PID. Abre otra terminal y ejecuta:

```bash
ps aux
```

Verás que se listan todos los procesos que están corriendo en tu computadora en este momento. La primera columna ofrece el nombre del usuario propietario del proceso, la segunda es el PID (número de identificación del proceso), y el resto muestran información como la hora y el día de inicio, el tiempo que llevan ejecutandose, la terminal a la que están vinculados, o el nombre o comando del proceso mismo. Puedes encontrar información sobre estas columnas haciendo [una sencilla búsqueda en internet](https://www.google.com/search?q=ps+aux+columns).

Vamos ahora a buscar el proceso `less` para "matarlo" y liberar la primera terminal. En lugar de revisar toda la lista, hagamos uso del poderoso comando `grep` que nos ayuda a filtrar patrones de texto. Vamos a hacer lo que se conoce en Linux como `pipe` o tubería, redirigiendo la salida de `ps aux` a la entrada del comando `grep` (como si concatenáramos los dos):

```bash
ps aux | grep less
```

Obtendrás algo como:

```
diego    15949  0.0  0.0  11072  2572 pts/3    S+   13:57   0:00 less numeros_aleatorios.txt
diego    16454  0.0  0.0  15652  1160 pts/5    S+   14:07   0:00 grep --color=auto less
```

La segunda línea es el mismo comando `grep` que se está ejecutando, y '15949' es el PID del proceso que queremos matar con el comando `kill`:

```bash
kill -9 15949
```

Verás que, como resultado, la primera terminal en la que se estaba ejecutando `less` ha quedado liberada. Si te estás preguntando por qué añadimos `-9` al comando `kill` puedes buscarlo en internet o acudir a la documentación propia que acompaña a todos los comandos de Linux. Para esto ejecutamos el comando `man`:

```bash
man kill
```

O puedes también encontrar una versión de la documentación más breve añadiendo la bandera, en inglés *flag*, `--help`:

```bash
kill --help
```

Antes de pasar a la siguiente sección recuerda borrar el fichero `numeros_aleatorios.txt`, es muy pesado. Antes de eso, deja que te cuente que si querías ver cúal era el último número aleatorio registrado en el fichero, no hacía falta hacer la búsqueda de la última línea con `less`. El comando `tail` saca por pantalla el final de un fichero, así como `head` imprime las primeras lineas:

```bash
tail numeros_aleatorios.txt
```

```bash
head numeros_aleatorios.txt
```

Vamos a jugar con los dos comandos para sacar por ejemplo la línea 9456:

```bash
head -9456 numeros_aleatorios.txt | tail -1
```

Ahora sí, no olvides borrar el fichero:

```bash
rm numeros_aleatorios.txt
```

### Ayuda de comandos con man, --help y apropos. <a class="anchor" id="man"></a>

Hemos visto en la sección anterior como `man`, o la bandera `--help`, sobre cualquier comando puede dar algo de información sobre dicha orden. Vamos a ver ahora cómo la misma terminal puede sugerirnos una lista de comandos según una búsqueda en su documentación. Pongamos por caso que queremos unir dos ficheros pdf. ¿Qué podemos hacer si no tenemos internet ni otra documentación? `apropos` nos puede ayudar. Digámosle a `apropos` que nos liste los comandos que tenemos instalados en la computadora relacionados con la palabra 'pdf':

```bash
apropos pdf
```

El listado es largo, ¿verdad? Vamos a filtrar con la palabra 'join' (unir o juntar en inglés):

```bash
apropos pdf | grep join
```

En mi caso obtengo la siguiente propuesta de comando útil para nuestro propósito:

```
pdfjoin (1)          - join together pages from multiple PDF files
```

Puedo ahora encontrar más información sobre cómo se usa `pdfjoin` con `man`:

```bash
man pdfjoin
# puede salir con la tecla 'q'
```

O si te resulta muy extensa y sólo quieres un resumen de su uso:

```bash
pdfjoin --help
```

### Bash como lenguage de programación para la terminal. <a class="anchor" id="bash"></a>

En secciones anteriores hemos advertido que Bash es un lenguage de programación. La terminal no es únicamente un medio para invocar comandos... puedes programar algoritmos que resuelvan de un manera más eficiente la tarea que pretendes resolver. Vamos a poner tres ejemplos sencillos: convertir como pdf todas las imágenes con extensión png que se encuentren en un directorio, listar todos los ficheros de tamaño mayor que un cierto límite en un directorio, o ejecutar un proceso cuando otro haya terminado.

Antes de ver los ejemplos enunciaremos un poco de información sobre alguno de los aspectos que caracteriza un lenguage de programación, como pueden ser las variables, los bucles o las condiciones lógicas.

#### Variables.

Como en todo lenguage de programación, la definición y almacenamiento de variables es esencial. Puedes definir variables en la terminal de la siguiente manera:

```bash
var_A='patata'
var_B=4
```

Puedes con `echo` sacar por la terminal el contenido de las variables:

```bash
echo $mi_variable
echo $otra_variable
```

Puedes realizar operaciones algebráicas con las variables:

```bash
var_C=$(($var_B + 2))
echo $C
```

No es el objetivo de este texto enseñar a programar en Bash. Se trata únicamente de que comprendas por qué es más util trabajar con la terminal que con el entorno de escritorio. Puedes encontrar en internet guías y tutoriales de programación en Bash si quieres profundizar. Allí aprenderas que también puedes definir variables lógicas, vectores, etc. 

Antes de terminar la introducción a las variables, has de saber que estas variables que defines en una terminal están asociadas a esa terminal... en cuanto la cierres se van a perder, y si pasas a otra terminal no las vas a ver. Son locales.

Linux hace uso también de las variables para la gestión de los procesos y los usuarios. Muchas de las cosas que están detrás de un usuario son variables. El nombre de tu usuario, el conjunto de paths en los que tu usuario busca comandos o archivos ejecutables, la lista de paths donde tu usuario busca librerías, el path en el que se encuentra tu terminal, el path de tu directorio hogar... son variables:

```bash
echo $USERNAME
echo $PATH
echo $LIBRARY_PATH
echo $PWD
echo $HOME
```

Puedes listar todas las variables que tu terminal maneja con el comando `export`:

```bash
export
```

De hecho, `export` o `set` también sirven para la definición de variables:

```bash
export varD=10
```

Puedes borrar las variables de la memoria de la siguiente manera:

```bash
unset varD
```

#### Bucles.

Hemos visto aquí un ejemplo en las secciones anteriores. Puedes hacer bucles en Bash del tipo secuencia, "haz mientras que...", "haz en caso de que...", etc. Vamos a ver un ejemplo de tipo secuencia y otro de tipo "haz mientras que...":

```bash
j=0
for i in $(seq 0 5 25)
do
   j=$(($j + 1))
   echo "El número $j de la serie es $i"
done
```

```bash
j=0
while [ $j -le 5 ]; do
   i=$(($j * 5))
   j=$(($j + 1))
   echo "El número $j de la serie es $i"
done
```

#### Condicion lógica *if*. <a class="anchor" id="if"></a>

También existen las condiciones lógicas. Veamos dos ejemplos de la sintaxis de la condición lógica "si ocurre esto haz esto otro". Nos auxiliaremos para el primero del comando `date`. Pruébalo antes:

```bash
date
```

`date` tiene muchas opciones, puedes checar `date --help` para entender qué significa:

```bash
date+"%u"
```

Podemos redirigir la salida de un comando a una variable en lugar de a `stdout`. Parecido a como la podíamos dirigir a un fichero de disco mediante `>`, pero esta vez a una variable:

```bash
dia_de_la_semana=`date +"%u"`
```

Hagamos ahora un ejemplo de estructura condicional con esta variable:

```bash
if [ $dia_de_la_semana -le 4 ]; then
    echo 'Muy bien. Es día laborable y estás trabajando.'
elif [ $dia_de_la_semana -eq 5 ]; then
    echo 'Es viernes!'
elif [ $dia_de_la_semana -le 7 ]; then
    echo 'Estás trabajando en fín de semana?'
else
    echo 'Tu semana tiene más de 7 días?'
fi
```

Ya estamos en condiciones de resolver algunas tareas sencillas.

#### Conversión de imágenes encontradas en un directorio. <a class="anchor" id="convert"></a>

Como primer ejemplo vamos a escribir unas líneas que ejecutar en la terminal para convertir los ficheros jpg de un directorio a pdf con unas pocas lineas de código.

En primer lugar descarga un paquete de imagenes jpg gratuitas que hemos recopilado para este tutorial:

```bash
wget https://github.com/uibcdf/Academia/raw/master/data/misc/free_images_jpg.tar.gz
```

Se trata de un archivo comprimido (tar.gz), si buscas en internet como descomprimirlo vas a encontrar algo como:

```bash
tar -zxvf free_images_jpg.tar.gz
```

Ahora vamos a situarnos en el directorio donde están las imágenes. Además, para ver que nuestro bucle opera solo sobre los ficheros jpg, vamos a crear tres ficheros allí que no deberían verse afectados.

```bash
cd free_images_jpg
touch foo1.txt foo2.png foo3.exe
ls
```

Hagamos un bucle para convertir las imágenes jpg a pdf. Usaremos el comando `convert` que puedes instalar con el paquete llamado `imagemagick`. Recuerda que si estás usando Ubuntu, basta el comando `sudo apt install imagemagick` para instalarlo. Desafortunadamente, para aprovechar todas sus funcionalidades, hay algo más. Por motivos de seguridad ImageMagick viene con la opción de tratar pdfs bloqueada, para resolverlo tendrás que seguir [las indicaciones dadas por un usuario en este foro](https://stackoverflow.com/a/52831300).

Ahora sí, ejecuta estas líneas de código Bash:

```bash
for filename in *.jpg; do
    fileprefix=`basename $filename .jpg`
    echo "Convirtiendo $fileprefix de jpg a pdf..."
    convert $filename $fileprefix.pdf
done
```

Verás que los archivos jpg se han convertido a pdf:

```bash
ls
```

Puedes abrir un pdf con por ejemplo el comando `evince`:

```bash
evince alpine-architecture-bridge-460373.pdf
```

No borres todavía la carpeta con estas imágenes. Van a ser de utilidad en la siguiente sección.

#### Listado de ficheros pesados.

Como segundo ejemplo hagamos un filtro para la lista de ficheros de una carpeta. El criterio para cribar la lista de ficheros será que el tamaño sea menor que cierto límite. Si descargaste, como se proponía en el ejemplo anterior, el paquete de imágenes jpg gratuitas, podemos trabajar sobre ese mismo directorio. Veamos un límite razonable para que tenga sentido:

```bash
du -sh *
```

Vemos que el límite de 1500K puede funcionar como filtro:

```bash
mi_filtro_de_tamaño=1500
for filename in *; do
    peso=`du $filename | awk '{print $1}'`
    if [ $peso -gt 1500 ]; then
        echo "      $filename ($peso K)"
    fi
done
echo "Hecho."
```

Por último, y para no acumular ficheros innecesarios, puedes borrar lo que hemos generado para este ejemplo y el anterior:

```bash
cd ../.
rm -r free_images_jpg free_images_jpg.tar.gz
```

#### Finalización de un proceso como gatillo para otro. <a class="anchor" id="gatillo"></a>

Como último ejemplo, hagamos un sencillo algoritmo de proceso que se dispara cuando otro acaba. Hagamos, como situación ilustrativa, que una terminal imprima un mensaje cuando el comando `less`, ejecutado en otra terminal, acabe.

Abre una terminal, colócala al izquierda de tu pantalla y ejecuta `less` sobre un fichero que vamos a crear:

```bash
echo "Este fichero es auxiliar" > foo.txt
less foo.txt
```

Ahora, sin cerrar `less`, abre otra terminal y colocala a la derecha de la pantalla. Sobre ella vamos a ejectuar unas líneas de código que ordenan a la terminal esperar a que no exista ningún proceso activo que contenga el texto 'foo.txt' para imprimir un mensaje. Copia estas lineas sobre la terminal derecha y ejecútalas.

```bash
less_vivo=0
while [ $less_vivo -eq 0 ]; do
    sleep 1
    ps aux | grep -v 'grep' | grep 'foo.txt' > /dev/null
    less_vivo=$?
    if [ $less_vivo -eq 1 ]; then
        echo "El proceso terminó!"
    fi
done
```

Verás que la terminal espera con el cursor parpadeante. Ahora, con las dos terminales a la vista, mira lo que sucede en la terminal derecha cuando seleccionas la terminal izquierda y presiona la tecla 'q' para salir de `less`.

## Editores de texto.

Hasta este punto, en este notebook, hemos realizado la mayoría de las creaciones y modificaciones de ficheros de texto con el comando `echo`. Esto no es el del todo común -ni útil-. Se ha hecho así para evitar el tema de los editores de texto hasta llegar a esta sección.

Aclaremos qué entendemos aquí por editor de texto. Editor de texto es una aplicación que sirve para el registro de texto en las unidades de memoria. Todos los editores que vamos a mencionar tienen el mismo efecto, y todos realizan la función que los define con el mismo resultado. En general no podemos adivinar con qué editor fue escrito un fichero. La diferencia entre editores está en la experiencia de usabilidad.

Si eres un usuario poco experimentado puede que comiences sientiéndote más cómodo con editores sencillos que cuentan con modo gráfico (una ventana en el escritorio y un explicito menú de opciones). Un editor con estas características que está instalados por defecto en tu distribución puede ser `gedit`. Otros editores, como `nano`, convirten la misma terminal en un sencilla ventana de edición con un menú cuyas opciones son visibles y de fácil entendimiento. Te recomiendo que pruebes todos los editores antes de elegir el más cómodo.

Para ayudarte a que comiences inmediatamente a tener un sencillo editor con el que empezar a trabajar, aquí tienes cómo se invocan desde la terminal cualquiera de los dos anteriores (y como se cierran):

```bash
gedit foo.txt # se cierra con el menú de la barra superior de la ventana
nano foo.txt # se cierra con la combinación de teclas 'ctrl'+'x'
```

Hasta aquí la parte más sencilla. Ahora, si no lo sabes ya, debes saberlo. El mundo de los editores de texto es un mundo ámplio y espinoso. La edición de textos es la herramienta principal y fundamental de un programador. ¿Has visto unos videos en youtube titulados algo así como ['Trabajadores rápidos nivel dios'](https://www.youtube.com/watch?v=RYK7fKsL9XQ)? La mayoría de programadores y científicos computacionales pasan una enorme cantidad de horas al cabo de la semana trabajando en el editor de textos, por eso alcanzan un [nivel de dominio y comunión con el editor que resulta asombroso](https://vimeo.com/53144573). Cuando trabajas así, quieres que la edición de un archivo sea un proceso ágil. Quieres conocer las combinaciones de teclas y atajos que te facilitan el trabajo. Quieres que el editor te facilite la vida y no te retarde innecesariamente en tu trabajo. Por ejemplo, puede parecerte una tontería aunque seguramente lo experimentarás: el uso del ratón resulta molesto porque retarda la velocidad de edición al separar continuamente una mano del teclado. [Se trata de alcanzar el modo de trabajo óptimo en el que casi la edición de un texto sucede a la misma velocidad que se piensa. ¿Te imaginas?](https://github.com/PhungLuan/docs/blob/master/Drew%20Neil%20-%20Practical%20Vim%20Edit%20Text%20at%20the%20Speed%20of%20Thought%2C%202nd%20Edition%20-%202015.pdf)

Así, porque el editor de textos junto con la terminal han sido las herramientas de trabajo principales, igual que se han desarrollado distintas distribuciones de Linux, existen, se mantienen y siguen apareciendo una gran variedad de editores de texto. Desde finales de los años ochenta, dos editores de uso libre han mantenido una historica pugna entre la comunidad de usuarios: Vim y Emacs. La comunidad ha estado durante años dividida entre seguidores defensores uno y otro. Es lo que se ha llamado [la guerra de los editores](https://en.wikipedia.org/wiki/Editor_war). En la última década, o puede que un poco más, han aparecido otros editores (gratuitos y de pago) estéticamente más atractivos, con funciones y experiencias de uso muy agradables, aunque no todavía con la versatilidad y la comunidad de usuarios que te da una trayectoria de más de tres décadas. Hagamos unos breves comentarios a estos editores de texto "más profesionales". Será tu tarea elegir uno y aprender a manejarlo.

Todos estos editores reconocen, por la extensión del fichero, distintos formatos como pueda ser un programa en python, un fichero escrito en markdown, un fichero html, etc. Y dependiendo de este reconocimiento implementan funcionalidades como el coloreado de sintaxis del lenguaje, la posibilidad de completar comandos con tabulador, la detección de errores en el programa, etc. Todos ellos pueden transformarse en autenticos IDEs (del inglés Integrated Development Environment) proporcionando los mismos servicios integrales para programación que plataformas como [Eclipse](https://www.eclipse.org/ide/), [Xcode](https://developer.apple.com/xcode/ide/) o [Netbeans](https://netbeans.org/).

### Vi o Vim
[Vim](https://www.vim.org/) y [Emacs](https://www.gnu.org/software/emacs/) son la pareja de editores de texto por excelencia en Linux. [Vim](https://www.vim.org/) está instalado por defecto en casi todas las distribuciones, al menos en su versión más ligera, sencilla y antigua: Vi.

Aprender a manejar Vim para alcanzar un nivel de trabajo cómodo y eficiente toma su tiempo. Puedes encontrar numerosas bromas en internet sobre la curva de aprendizaje de Vim. Pero, al igual que con Emacs, con un poco de adiestramiento la edición de textos -y la programación- se vuelve una tarea más rápida.

Vim tiene la peculiaridad de que trabaja con una filosofía de 'modos'. Está por ejemplo el 'modo insertar texto', o el modo 'comandos' o el modo 'seleccionar texto'. De nuevo, al principio puede parecer molesto, pero con la práctica se le encuentra el sentido.

Vim es casi completamente modificable y personalizable en su uso, hackeable. Como cualquiera de los editores de esta lista. Por eso, la mayoría de usuarios arrastran a lo largo de su vida un fichero donde se definen los atajos, combinaciones de teclas, funcionalidades, implementaciones y modificaciones al comportamiento nativo, realizadas por uno mismo o encontradas en foros de internet.

Vim es uno de los editores de texto para terminal que más rápido te permite abrir un fichero, hacer una pequeña edición, guardar y volver a la terminal.

### Emacs
[Emacs](https://www.gnu.org/software/emacs/) es el otro contendiente en la histórica guerra de editores de texto. 

Emacs, como Vim, también requiere un poco de paciencia al principio. Tras unas horas de práctica alcanzarás un nivel de uso que cubrirá de manera rápida tus necesidades más habituales, pero si quieres seguir aprendiendo y optimizando tu edición de textos, estos dos editores te ofrecen unas posibilidades inmensas. Sólo después de años de uso, si es que no te lo tomas de manera muy intensa, llegas a apreciar los límites de cada editor.

Emacs no trabaja desde una filosofía de 'modos' de edición. Emacs tiene un amplio repertorio de combinación de teclas y opciones de entrada de comandos que cubre casi cualquier necesidad. Además Emacs tiene en su nucleo una especie de sistema operativo que lo hace adaptable a cualquier necesidad. Con la posibilidad de implementar modificaciones para cualquier función. Por poner unos ejemplos sencillos que puedas entender, con emacs tienes la posibilidad de [visualizar por ejemplo un pdf](https://www.emacswiki.org/emacs/DocViewMode) o de [publicar un tweet en tu cuenta de twitter](https://www.emacswiki.org/emacs/TwitteringMode) sin salir del editor.

Vim o Emacs son dos muy buenos editores. Si no fuera así no hubieran sobrevivido tantos años en una comunidad tan exigente.

### Spacemacs o Spacevim

Han surgido varios intentos de editor de texto híbridos entre Vim y Emacs. Editores que puedan toman lo mejor de cada uno de ellos, o que te permiten personalizar el grado de "vimificación" o "emacsficación" con el que estás trabajando. Un ejemplo es [Spacemacs](http://spacemacs.org/), y más tarde [Spacevim](https://spacevim.org/). Spacemacs es un emacs con una filosofía de modos integrada como la de Vim. Puedes elegir dos sabores de uso, 'glory', con un universo de atajos y combinaciones de teclas similar al Emacs original y 'hell', con una experiencia de uso más parecida a Vim.

Su arranque, dado que carga muchas librerías, puede resultar un poco lento.

### Atom

[Atom](https://atom.io/) es un moderno editor de texto de uso libre con una estética más actual y unas funcionalidades que le pueden hacer competir con Vim o Emacs. Nació directamente en GitHub como un proyecto de editor moderno de uso libre para desarrolladores.

Atom no está instalado por defecto y puede que no lo encuentres en el repositorio de tu distribución de Linux. Pero lo puedes instalar en MacOs, Windows o Linux facilmente desde [su web](https://atom.io/).

### Sublime

[Sublime](https://www.sublimetext.com/) es un editor de uso no libre, de pago. La especial orientación de Sublime para la edición de código de programación y sus funciones como IDE, han hecho que gane en los últimos años una enorme popularidad entre profesionales del cómputo, programadores y usuarios avanzados.

<br>
<img src="https://imgs.xkcd.com/comics/real_programmers.png" width="550">
<br>

<br>
<img src="https://imgs.xkcd.com/comics/types_of_editors.png" width="550">
<br>

<br>
<img src="https://imgs.xkcd.com/comics/hottest_editors.png" width="250">
<br>


## El script.

Hemos visto como Bash es en realidad un lenguage de programación. También que esos comandos útiles listados en la sección ["La terminal y la sintaxis de Bash."](#La-terminal-y-la-sintaxis-de-Bash.) no son más que 'programas' ubicados en la carpeta `/bin`. Hemos ilustrado con ejemplos cómo la terminal resulta tan útil, o más, que trabajar con el entorno de escritorio. Y vamos a ver ahora otra tercera manera de operar con tu sistema operativo: el script.

A la terminal le podemos ofrecer ordenes de manera interactiva y secuencial, o podemos escribir esa lista de ordenes en un fichero y pedirle que las ejecute como un programa, línea a línea. Eso es un script: un fichero de texto plano que codifica secuencialmente la lista de ordenes que queremos ejecutar y que se ejecutan mediante la participación de un interpretador del fichero. En este caso el interpretador de Bash. Que dónde está ese interpretador:

```bash
which bash
``` 

Hagamos unos ejemplos sencillos:

```bash
echo `echo "Eres la más lista"` > autoestima
```

Espero que hayas corregido el género de la frase si prefieres que te traten en masculino. Ahora prueba a decirle a tu computadora que procese ese fichero con el interpretador `bash`:

```bash
bash autoestima
```

`autoestima` es un script sencillo, de una sola línea. Vamos a hacerlo un poquito más complicado antes de convertirlo en 'ejecutable'. Abre tu editor de texto y escribe las siguientes líneas:

```bash
#!/bin/bash

# Genero un número aleatorio entre el 1 y el 5
loteria=`shuf -i 1-5 -n 1`

# Según el valor del número aleatorio saco un mensaje por terminal
if [ $loteria -eq 1 ]; then
    echo "Eres la más lista"
elif [ $loteria -eq 2 ]; then
    echo "Eres la más guapa"
elif [ $loteria -eq 3 ]; then
    echo "Eres la más simpática"
elif [ $loteria -eq 4 ]; then
    echo "Eres la más intelegente"
else
    echo "Eres la más divertida"
fi
```

¿Has visto la primera línea? No reconoces nada conocido, ¿verdad?. Esta primera línea le dice a la computadora cúal es el interpretador que ha de leer el script para convertirlo a lenguage máquina, a operaciones. Si la primera línea no está, siempre podemos, como hicimos antes, invocar nosotros el intepretador con el comando `bash` -si el script es de Bash-. Pero queremos que nuestro fichero sea auto-ejecutable, y el usuario no tiene por qué saber que es de `bash` o `python` o `perl`, por decir alguno.

Ahora sí, hagamos que `autoestima` sea un ejecutable:

```bash
chmod +x autoestima
```

Nota que seguramente `autoestima` ha cambiado de color en la terminal. Los ficheros que no son directorios, ni alias o enlaces, ni ficheros comprimidos... son de un color distinto que tu script. Esto es porque ahora tiene permisos de ejecución. Mira el color con el que se lista en la terminal:

```bash
ls autoestima
```

Veremos más adelante qué significa el comando `chmod` en la sección ["Los permisos de los ficheros."](#Los-permisos-de-los-ficheros.). Ahora ya puedes ejecutar el script como un ejecutable, para ello tienes que invocarlo con el path absoluto o el path relativo precedido de un '.':

```bash
./autoestima
```

```bash
/home/diego/autoestima
```

Volveremos al script 'autoestima' más adelante, no lo borres todavía.

## Las extensiones de los archivos.

El nombre de un fichero usualmente lleva un sufijo precedido por un punto. Por ejemplo 'fichero.txt' o 'fichero.sh' o 'fichero.py'. Ese sufijo, denominado también extensión, sirve para indicar al usuario y al sistema qué naturaleza tiene el fichero (y con qué aplicación debe abrirse por defecto). Pero no pierdas de vista que no es nada más que parte del nombre del fichero y responde a un convenio.
Podemos crear un fichero de texto y llamarlo 'patata' o 'patata.txt', en ambos casos lo vas a poder leer con `less` o `more`. Podemos crear el fichero 'patata' o 'patata.sh' en el caso de un script de bash, y ambos comandos `bash patata` o `bash patata.sh` tendrán el mismo efecto. O podemos crear un script de python y llamarlo 'patata' o 'patata.sh' o 'patata.txt' o 'patata.py'... todos ellos podrán ser leidos por el interpretador `python` con el mismo efecto. Por último, puedes tomar el pdf 'patata.pdf' y llamarlo 'patata.odt' y el comando `evince patata.odt` abrirá el pdf igual que lo haría `evince patata.pdf`. Reitero, la extensión es sólo una parte del nombre, y tiene una función indicativa, no condiciona su contenido.

En la siguiente sección veremos que un fichero no es ejecutable por tener la extensión '.exe', si no por tener permisos de ejecución.

## Los permisos de los ficheros.

Un fichero tiene asociado desde su creación unos permisos, negados o validados, de escritura, lectura y ejecución; para el usuario propietario, el grupo propietario o para todos. Vamos a ver esto con detalle.

El comando `touch` crea un fichero vacío, que en este caso vamos a llamar 'asdf'.

```bash
touch asdf
```

Para conocer los permisos y los propietaros podemos recurrir al comando `ls` con la bandera `-l`:

```bash
ls -l asdf
```

Veremos una linea similar a esta:

```bash
-rw-r--r-- 1 diego diego 0 dic  3 21:08 asdf
```

En la salida del comando anterior podemos identificar, empezando por el final, el nombre del fichero, la fecha de su creación, el espacio que ocupa en disco ("0" porque está vacío) y dos veces 'diego', como usuario propietario y como grupo propietario. Despues vemos el número entero "1" que indica el número de enlaces -no relevante aquí-, y una secuencia de 10 caracteres:

- El primer carácter para un fichero normal suele ser '-'.
- Los siguientes tres caracteres 'rwx' indican permiso de lectura (r), escritura (w) y ejecución (x) para el usuario propietario. El permiso se indica como denegado para cada acción si en lugar de la letra correspondiente vemos un signo '-'.

- Los siguientes tres caracteres indican permiso de lectura, escritura y ejecución para el grupo propietario.

- Los últimos tres caracteres indican los mismos permisos pero para cualquier usuario.

Así, atendiendo a nuestro fichero 'asdf', vemos que tiene permisos de lectura y escritura para 'diego', y únicamente de lectura para cualquier otro usuario. Modifiquemos los permisos conociendo que en el siguiente comando la letra 'u' quiere decir usuario, 'g' quiere decir grupo y 'a' hace referencia a cualquier otro usuario. Vamos con `chmod` a dar permisos de ejecución para el usuario 'diego' y de escritura para cualquier otro.

```bash
chmod u+x asdf
chmod a+w asdf
```

Y aunque sea absurdo, vamos a quitarle los permisos de lectura al grupo propietario:

```bash
chmod g-r asdf
```

Veamos ahora la salida de `ls -l`:

```bash
-rwxr-xr-x 1 diego diego 0 dic  3 21:08 asdf
```

Por último, podemos cambiar el usuario o el grupo propietario con los comandos `chown` y `chgrp` (y con `sudo`):

```bash
sudo chown liliana asdf
sudo chgrp liliana asdf
```

Por última vez ejecuta `ls -l`:

```bash
-rwx-w-rw- 1 liliana liliana 0 dic  3 21:09 asdf
```

Antes de continuar con la siguiente sección es conveniente que borres el fichero 'asdf':
```bash
rm asdf
```

## Los enlaces simbólicos de fichero. <a class="anchor" id="ln"></a>

En Linux hay un tipo de fichero que únicamente sirve para apuntar a otro. Se llama enlace simbólico, funciona como un alias del fichero al que apunta y se declara con el comando `ln`. Veamos un ejemplo:

```bash
touch foo1
ln -s foo1 foo2
```

Hemos creado 'foo2' como enlace a 'foo1'. Puedes distinguir el original del enlace porque este último toma un color especial en la terminal:

```bash
ln -s foo?
```

También puedes saber a qué apunta un enlace con el comando `ls`:

```bash
ls -lah foo2
```

Así, cualquier modificación a 'foo2' será hecha en 'foo1':

```bash
echo 'Esta es una linea de texto' >> foo2
less foo1
```

De hecho, el enlace no tiene contenido y por lo tanto no ocupa memoria de disco. Puedes checar su tamaño con `du`:

```bash
du -sh foo2
```

Podemos hacer enlaces de cualquier tipo de fichero, incluidos directorios. Borremos los ficheros anteriores y hagamos un ejemplo con ficheros:

```bash
rm foo1 foo2
```

```bash
mkdir -p dir1/dir2/dir3
mkdir dirA
ln -s /home/diego/dir1/dir2/dir3 /home/diego/dirA/dir3 #nota que los paths deben ser absolutos
ls -lah dirA/dir3
touch dir1/dir2/dir3/nada
ls dirA/dir3
cd dirA/dir3
echo 'Con cien cañones por banda...' >> nada
less ../../dir1/dir2/dir3/nada
```

No podemos acabar esta sección sin responder algo que vienes preguntándote desde la generación del primer enlace simbólico: ¿Para qué la bandera `-s`? Hay dos tipos de enlaces, suaves o simbólicos (la `-s`) y rígidos. Los enlaces rígidos no los hemos tratado aquí. Los enlaces rígidos se declaran sin `-s` y tienen tres peculiaridades que los distinguen de los simbólicos. Primero, el original y el enlace deben estar en la misma partición. Segundo, no podemos hacer enlaces rígidos de directorios. Y tercero, si borramos el archivo original el enlace rígido sigue respaldando el contenido de dicho archivo, no queda huerfano. Al contrario del enlace simbólico, que queda sin contenido al borrar el archivo al que apunta.

## Los usuarios y los grupos.

Linux está diseñado desde su concepción para soportar sobre la misma máquina la actividad simultanea de varios usuarios. Esos usuarios tienen todos un número de identificación, un directorio hogar y una contraseña.

Tu número de identificación lo puedes encontrar con el siguiente comando:

```bash
id -u
```

Tu directorio hogar ya lo conoces, su path está en tu variable HOME:

```bash
echo $HOME
```

Tu contraseña la puedes cambiar con el comando `passwd`. Si quisieras hacerlo puedes ejecutar el comando en una terminal e introducir en primer lugar tu contraseña actual y luego la nueva.

```bash
passwd
```

Linux lleva el control de usuarios y sus características en el fichero '/etc/passwd'. Puedes echarle un ojo, si es la primera vez que lo haces vas a llevarte una sorpresa:

```bash
less /etc/passwd
```

¿Has encontrado tu usuario en esa lista? Hay muchos usuarios, ¿verdad? Hay usuarios que en realidad no son personas, no son usuarios reales. Se llaman demonios (en inglés *daemons*) y son aplicaciones que tienen un usuario virtual para realizar ciertas gestiones. Este hecho, que está en el nucleo del diseño del sistema Linux, es parte de lo que lo ha hecho tan eficiente con respecto a otros sistemas operativos.

Y además de usuarios, en Linux se definen grupos de usuarios. Esto es muy útil a la hora de gestionar acciones sobre conjuntos definidos de usuarios. Tu usuario, puede que todavía no lo sepas, pertenece a varios grupos. De hecho, tu usuario mismo define un grupo, con su número de identificación que seguramente será igual que el de usuario para para el registro de grupos. Puedes checarlo con el siguiente comando:

```bash
id -g
```

¿Y a que otros grupos perteneces? En el siguiente comando identificarás tu nombre e id de usuario, el nombre de tu usuario como grupo y su id, y la lista de grupos a los que perteneces:

```bash
id
```

¿Perteneces por ejemplo al grupo 'lpadmin'? Sólo los usuarios que pertenecen a ese grupo pueden hacer gestión de los recursos de impresión, como configurar la comunicación con una nueva impresora.

La lista de grupos se gestiona en casi toda distribución de Linux gracias al fichero '/etc/group':

```bash
less /etc/group
```

Por último, mira qué usuario está al comienzo de la lista de '/etc/passwd': root. En la siguiente sección abordaremos las cuestiones ¿Quién es root?, ¿Y quién además puede hacer tareas de gestión del sistema operativo? Te habrás dado cuenta de que en esta sección de usuarios y grupos no hemos dicho nada sobre cómo se crean. Es porque puede que no tengas permisos para realizar esas acciones. O sí.

## Root, el superusuario, y sudo. <a class="anchor" id="sudo"></a>

<img src="https://www.explainxkcd.com/wiki/images/b/b1/sandwich.png" width="250">

El usuario root, o superusuario, es el usuario definido en el sistema con permisos para realizar cualquier tarea. Es el usuario con la capacidad innata de administrar el sistema operativo. Hace un tiempo muchas distribuciones pedían a la hora de ser instaladas una contraseña para el usuario root. Suponiendo, claro, que la persona que instala el sistema operativo es el mismo que va a ejercer de administrador. Hoy en día, en el caso de Ubuntu por ejemplo, en la instalación se define un usuario con permisos de actuación "como si fuera" root. Es lo que se conoce como 'sudo'. Probablemente, si eres la persona que instaló el SO que estás usando y tu usuario es el primero que se creó, tu usuario tiene la capacidad de hacer `sudo`. De nuevo en el caso de Ubuntu, los usuarios con la capacidad de realizar tareas de administración como si fueran root deben pertenecer al grupo que lleva el nombre de 'sudo'. Puedes comprobar con el siguiente comando si perteneces a dicho grupo:

```bash
id
```

Si es el caso, puedes continuar de forma activa esta sección. Veamos por ejemplo que significa pertenecer al grupo 'sudo', o tener la capacidad de hacer `sudo`. Ejecuta el siguiente comando:

```bash
less /etc/shadow
```

Te dirá que no tienes permiso para ver su contenido. '/etc/shadow' contiene la encriptación de las contraseñas de los usuarios. Ahora prueba con el siguiente comando (pedirá tu contraseña de usuario):

```bash
sudo less /etc/shadow
```

En este caso estás ejecutando el comando `less` como si fueras root, como si fueras administrador, con plenos poderes para hacer cualquier cosa. Y ya sabes lo que le dijeron a Spiderman citando un discurso del expresidente estadounidense Franklin Delano Roosevelt: "... un gran poder conlleva una gran responsabilidad". Podrías por ejemplo generar un gran problema con el comando `sudo rm /etc/shadow`, o con el más desastroso de todos si no tienes copia respaldo de absolutamente todo: `sudo rm -r /*`.

Teniendo la posibilidad de ejecutar comandos con `sudo`, puedes, si tienes que realizar muchas tareas de administración que requieram ser superusuario, hacer uso del comando `su` para cambiar de tu usuario al usuario root. Antes de eso veamos que `su` también nos permite cambiar a cualquier otro usuario. Vamos a hacer un ejemplo de cambio a otro usuario antes de pasar a root. Primero vamos a crear un usuario nuevo que llamaremos 'thanos' desde la terminal:

```bash
sudo adduser thanos
```

Verás que pide que introduzcas la contraseña que usará 'thanos' además de otra información personal de caracter informativo -que puedes dejar en blanco presionando la tecla 'entrar'-. Ahora para comprobar que el usuario se ha creado satisfactoriamente hay muchas maneras. Por ejemplo, puedes cerciorarte de que su directorio hogar fue creado:

```bash
ls /home
```

Puedes también comprobar que su usuario aparece en el fichero '/etc/passwd':

```bash
less /etc/passwd | grep thanos
```

O puedes, porque tienes la capacidad de actuar como superusuario gracias al comando `sudo`, cambiarte por el...

```bash
sudo su thanos #la contraseña que pide es la de tu usuario... es sudo quien está asegurandose de que eres tu.
```

Et voilà! Ya eres thanos. Verás que el prompt cambió y ahora dice comienza con 'thanos@...' Puedes hacer cualquier cosa en la terminal y todo quedará registrado como 'thanos', porque de hecho, ahora mismo, eres 'thanos'. Pero 'thanos' no tiene permiso para usar `sudo`. Supongamos, únicamente como ejemplo de cómo puede hacerse, que queremos darle a 'thanos' permisos de superusuario. Ahora no tiene, prueba:

```bash
sudo less /etc/shadow
```

Sólo tu usuario, a través de `sudo`, y root pueden otorgarle ese poder. Así que sal de 'thanos' y vuelve a tu usuario, lo primero:

```bash
exit
```

¿Ya pone tu nombre de usuario en el prompt? Ahora ya puedes añadir a 'thanos' al grupo sudo. Siguiendo con el ejemplo de cómo se hace en Ubuntu:

```bash
sudo usermod -aG sudo thanos
```

Verás que ya pertenece al grupo privilegiado:

```bash
id thanos
```

Hagamos la prueba:

```bash
sudo su thanos   # sudo quiere saber si eres tu, es tu contraseña
sudo less /etc/shadow # sudo pide aquí la contraseña de thanos para asegurarse de que es él
```

De este modo le hemos dado a 'thanos' la posibilidad de modificar cualquier cosa en tu sistema operativo. Incluso, por ejemplo, de decidir qué usuario es aniquilado y qué usuario sobrevive. Pero antes de que él lo haga, borrémoslo a él para terminar el ejemplo. Para ello, sal de nuevo de 'thanos':

```bash
exit
```

Con tu usuario ahora elimina a 'thanos' y su directorio hogar:

```bash
sudo userdel thanos
sudo rm -r /home/thanos
```

Puedes comprobar, como hiciste antes, que 'thanos' ya no existe.

Por último, si tienes que realizar muchas gestiones de administración y no quieres estar a cada comando anticipándole el `sudo` puedes saltar al usuario root de este manera:

```bash
sudo su
```

Verás que el prompt ahora dice 'root@...'. Recuerda que siendo root tienes todo el poder, y una gran responsabilidad.

Para salir del superusuario root, basta con que hagas:

```bash
exit
```

## Los ficheros de configuración de usuario. <a class="anchor" id="configuracion_usuario"></a>

Los ficheros de configuración de cada usuario están ocultos en su directorio 'home'. ¿Cómo se oculta un archivo en Linux? Un archivo se oculta comenzando su nombre con un '.', y para listarlos y verlos hay que añadir a `ls` la bandera `-a` (del inglés *all*):

```bash
ls -a
.   .bash_history  .bashrc  .profile
..  .bash_logout   .cache   .gnupg
```

Es cierto que hay parámetros de configuración de un usuario que se encuentran en los ficheros del sistema. Porque se definen como opciones "por defecto" válidas para todo usuario. Pero en la jerarquía de los ficheros que definen el comportamiento de tu usuario, siempre tiene prioridad lo que puedas definir en tus ficheros. Hablaremos de los más importantes:

#### ~/.bashrc

Es el archivo más importante que tienes para definir el comportamiento de tu usuario. Cada vez que abres una terminal, este fichero se ejecuta. ¿No te lo crees? Vamos a hacer un prueba. Abre tu '.bashrc' con un editor para incluir al final del fichero estas tres lineas:

```
export mi_variable='tururú'
alias cuantos_ficheros_hay_en_esta_carpeta='ls -l | wc -l'
echo "Hola! Ya terminé de ejecutar el .bashrc"
```

Guarda, cierra el fichero y abre una nueva terminal. Verás que antes de colocar el primer prompt la terminal muestra el resultado del último comando que añadirmos al final de '.bashrc'. Ahora prueba que las otras dos líneas que añadimos se ejecutaron.

```bashrc
## Saca el contenido de la nueva variable
echo $mi_variable
```

```bashrc
## No hace falta que lo escribas todo, la tecla 'tab' completará el comando
cuantos_ficheros_hay_en_esta_carpeta
```

Ahora que ya viste en acción la función de este fichero, puedes volver a abrirlo y borrar esas lineas.

#### ~/.bash_aliases

Algunas distribuciones de Linux configuran la plantilla de '.bashrc' que se colocará en cada nuevo usuario. Puedes comprobar, como seguramente le sucede a tu '.bashrc', que incluye la siguiente instrucción:

```bash
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

Si leistes las secciones anteriores, puedes adivinar que lo que está haciendo ese segmento de código es comprobar si en tu directorio hogar existe el fichero '.bash_aliases', y si es así, lo ejecuta. Es una manera de que '.bashrc' no se haga inmensamente largo y puedas organizar la configuración de tu usario un poco. De este modo, las definiciones de alias las sacaremos de '.bashrc' y las pondremos en '.bash_aliases'. Y no, no hemos olvidad que todavía no dijimos nada aquí de qué es un alias, pero lo pudiste deducir de nuestro ejericio con '.bashrc'. Un alias es eso, un alias. Es renombrar un comando con otra cadena de caracteres para que pueda ser invocado de una manera más comoda, más rápida y más facil de recordar. 

Hay alias definidos casi en todas las distribuciones de Linux como son:

```bash
alias ls='ls --color=auto' # ls dará color a los ficheros según su naturaleza
alias ll='ls -alFh'        # ll listará todos los ficheros junto con permisos y tamaño en formato leible por humanos
alias la='ls -A'
alias l='ls -CF'
```

Te dejo como tarea acudir a internet, a `ls --help` o `man help` para averiguar el significado de los dos últimos alias.

#### ~/.profile
Este fichero es muy similar a './bashrc'. En realidad en algunas distribuciones como Ubuntu, este fichero se ejecuta antes. Este es el fichero que ordena ejecutar './bashrc' si es que lo tienes. Verás que './profile' contiene:

```bash
# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi
```

Este parrafo comprueba primero que la computadora tiene Bash instalado, y en ese caso busca que el usuario tenga un fichero '.bashrc'. Si esto último sucede, lo ejecuta.

Podemos usar '.profile' para la personalización de variables de entorno. Veremos un ejemplo de esto en la siguiente sección.

#### ~./bash_history

Este no es exactamente un fichero de configuración, pero le debemos reconocer mucha utilidad. `~/.bash_history` guarda la secuencia de los $N$ últimos comandos ejecutados por tu usuario. Como su nombre indica, es un histórico. Prueba antes que nada en tu terminal a mantener presionada la tecla 'ctrl' mientras pulsas varias veces la tecla 'p'. ¿No estás viendo los últimos comandos que realizaste?, ¿no estás caminando hacia atrás en tu historico? Prueba ahora otra cosa. Borra la linea que 'ctrl'+'p' dejó en la terminal y ahora haz 'ctrl'+'r'. ¿Te aparece algo así?

```bash
diego@nauta:~$ 
(reverse-i-search)`': 
```

Puedes ahora teclear una cadena de caracteres y que se buscarán de manera reversa en el histórico. Vamos a probar a ver cúal fue el último comando que empezaba con 'echo'. Teclea 'echo' si tu terminal dice `reverse-i-search`. ¿Ya salió? Ahora, con la tecla 'ctrl' presionada pulsas varias veces 'r', verás que aparecen la serie de comandos que contienen los caracteres 'echo' en búsqueda reversa del historico. Ya puedes borrar la linea que la búsqueda reversa te dejó.

Entonces, ¿dónde 'ctrl'+'p' o 'ctrl'+'r' encuentra tu historial de comandos?:

```bash
.bash_history
```

Pero este fichero tiene una cantidad de líneas limitada. Comprueba cual es la longitud, en cantidad de líneas, que tiene tu fichero:

```bash
wc -l
```

`wc` sirve también para contar la cantidad de caracteres de un fichero de texto:

```bash
wc -m .bash_history
```

Para modificar la cantidad de información que puede quedar registrada en tu histórico tendrás que editar las variables `HISTSIZE` e `HISTFILESIZE` en tu fichero '.bashrc'. Qué hace cada variable lo puedes encontrar en la documentación o foros como [este](https://stackoverflow.com/questions/19454837/bash-histsize-vs-histfilesize). En mi caso yo modifiqué el valor de esas variables para tener un histórico razonable en el que poder buscar los comandos que ejecuté en el pasado.

```bash
HISTSIZE=200000
HISTFILESIZE=200000
```

Por último y antes de pasar a la siguiente subsección, un consejo: 'ctrl'+'p' y 'ctrl'+'r' pueden hacer que tu interacción con la terminal sea más cómoda. Yo los uso con frecuencia para trabajar más ágil, ¿Para qué voy a teclear de nuevo el comando anterior?, ¿para qué vamos a teclear entero el comando que fué ejecutado hace unos minutos?

#### Otros ficheros

Distintas distribuciones de Linux organizan la información de distinta manera. Aquí estamos siendo un poco más fieles a la distribución Ubuntu porque es la que hemos recomendado para un usuario no experto que necesita un entorno de trabajo estable y productivo en el laboratorio. Puede que tengas otra distribución y veas ficheros como `.bash_profile` o `.bash_login`. En internet vas a encontrar fácilmente información sobre su función.

## Las variables de entorno.

Hemos hablado anteriormente de las variables en Linux. También de las variables de usuario como `HOME` o `PWD`. Estas últimas son variables de entorno. Son variables que definen el comportamiento de tu usuario y la terminal, en definitiva, el comportamiento del entorno Linux. Quizá las que debes de conocer de cara al trabajo que realizamos sean `PATH`, `LIBRARY_PATH` y `LD_LIBRARY_PATH`. Estas tres variables afectan a cómo interaccionas con el software y las librerías que vas a instalar para trabajar.

### PATH

`PATH` almacena, separados por el caracter ':', la lista de directorios en los que tu usuario buscará ejecutables (comandos). Prueba:

```bash
echo $PATH
```

¿Ves el directorio '/bin' en la lista? Tu usuario puede ejecutar `ls` o `echo` porque estos son comandos que encuentras en alguno de los directorios que tu usuario almacena en `PATH`:

```bash
ls /bin
```

### LIBRARY_PATH y LD_LIBRARY_PATH

Así como `PATH` contiene los sitios donde encontrar ejecutables, `LIBRARY_PATH` contiene la lista de lugares con librerías necesarias para compilar un ejecutable y `LD_LIBRARY_PATH` la lista de lugares con librerías dinámicas a las que cualquier programa o ejecutable puede acudir para realizar funciones concretas.

### Más variables de entorno?

Sin duda hay más variables de entorno, pero no tienes por qué conocerlas todas para ser un usuario avanzado. No es el propósito tampoco de este notebook hacer un repaso riguroso. Puedes encontrar información fácilmente en internet, y acudir a ella cuando se presente la ocasión y lo necesites.

Lo que sí debes saber es que estas variables pueden ser modificadas a conveniencia. Vamos a ver un ejemplo para que lo comprendas mejor. ¿Recuerdas el script 'autoestima'? Lo programamos y declaramos ejecutable en la sección ["El script."](#El-script.). Ahora vamos a colocar una copia de dicho script en alguno de los directorios de tu lista `PATH`. ¿Qué tal en el directorio '/usr/bin' o '/usr/local/bin'?:

```bash
cp autoestima /usr/bin/.
```

No funcionó, ¿verdad? Claro, no cualquier usuario puede alterar el contenido de '/usr/bin'. Necesitas permisos de administración, ¿si los tienes?

```bash
sudo cp autoestima /usr/bin/.
```

Ahora abre una terminal nueva e imagina... estás trabajando con la moral baja y necesitas una inyección de autoestima. ¡Ya puedes teclear con la terminal situada en cualquier directorio 'autoestima'!

```bash
autoestima
```

Borra mejor el script. Tu no lo necesitas...

```bash
sudo rm /usr/bin/autoestima
```

Pero para conseguir esto no hace falta que tengas permisos de administración, al fín y al cabo sólo quieres hacer algo que afecta a tu usuario. Y el mal uso de `sudo` puede ser un riesgo que afectará a todos en esa máquina. Vamos crear un directorio tuyo en el que todos los ficheros que ubiques allí serán interpretados por tu usuario como comandos y ejecutables:

```bash
mkdir /home/diego/mibin
```

Ahora mueve el script 'autoestima' a ese directorio:

```bash
mv autoestima ~/mibin/.
```

Sólo queda añadir el path '/home/diego/mibin' a la variable `PATH`.

Abre el fichero `.profile` o el `.bashrc` con tu editor e incluye al final de él algo como:

```bash
### Mis Paths

export PATH=$HOME/mibin:${PATH}

```

Cualquier terminal que abras a partir de ahora tendrá en su lista de lugares en los que encontrar ejecutables el path de tu directorio `mibin`. Abre una terminal nueva y prueba:

```bash
echo $PATH
```

Ya apareció ahí tu directorio 'mibin', ¿verdad? Pues ya puedes dejar que la computadora te suba la autoestima cuando quieras:

```bash
autoestima
```

## SSH y la conexión con otras máquinas. <a class="anchor" id="ssh"></a>

SSH, del inglés *Secure Shell*, es el protocolo de comunicación encriptado más común para interaccionar con otras computadoras. SSH te permite operar remótamente con otra máquina a través de tu terminal. Para ello el comando `ssh` necesita la IP de la máquina destino y el usuario registrado en esá máquina que usarás para acceder

```bash
ssh liliana@155.192.168.1
```

El comando anterior hace una llamada a la máquina 155.192.168.1 y le pide acceso como usuario 'liliana'. Acto seguido se nos pedirá la contraseña de liliana en esa máquina para despues licitar nuestra terminal con el mismo grado de operabilidad en la máquina destino como si de la local se tratase. De hecho, verás que el prompt cambia para indicar ahora el nombre ('hostname') de la máquina remota, y el usuario con el que operas:

```bash
liliana@nombre_máquina_remota:~$
```

Ya puedes, en remoto, ejecutar los comandos que necesites en ese máquina. Ahora, para cerrar la conexión y volver a tu máquina local:

```bash
exit
```

Puedes también copiar ficheros desde tu máquina local a la remota, y viceversa. Para ello el protocolo SSH dispone del comando `scp`. De manera similar a cómo opera `cp`, `scp` puede copiar un fichero local a una máquina remota:

```bash
scp /path/a/fichero/fuente usuario@ip:/path/de/destino/.
```

O de la máquina remota a la máquina local:

```bash
scp usuario@ip:/path/a/fichero/fuente /path/de/destino/.
```

### Puedes operar con hostnames en lugar de IPs

Las direcciones IP pueden tener definidas alias en tu máquina. De esta manera no hace falta que las memorices, basta con que las listes en el fichero '/etc/hots':

```bash
less /etc/hosts
```

¿Tienes una máquina a la que accedes habitualmente? Supongamos que se llama AllSpark y que su ip es la 999.999.999.999. Edita el fichero '/etc/hosts' con tu editor de textos y añade la siguiente linea:

```bash
999.999.999.999 allspark
```

Ya puedes emplear `ssh` y `scp` sustituyendo la ip de la máquina remota por su hostname. Por ejemplo:

```bash
ssh liliana@allspark
```

## Nota final.

El contenido de este documento es suficiente para comenzar. Ya sólo queda que a medida que vayas trabajando, poco a poco aprendas aquellos comandos que más usas. Al principio no hay que desesperarse, probablemente necesitarás varias veces volver a buscar qué comando servía para borrar un directorio, o qué comando servía para filtrar la salida de `less`... pero con un poco de paciencia irás familiarizandote con la terminal. Todos los usuarios estamos constantemente aprendiendo cosas nuevas y recordando otras. Pero pront se adquiere un nivel de uso que compensa sobradamente el tiempo invertido. Ahora, lo único importante es que hayas tenido un primer contacto para entener qué te puede ofrecer el uso de Linux.

---

# Dudas, problemas técnicos y soluciones. <a class="anchor" id="dudas"></a>

Para centralizar esas dudas, sugerencias o soluciones técnicas sobre el tema de este notebook, haz uso del siguiente canal:

[Foro Técnico: Linux](https://github.com/uibcdf/Academia/issues/9)


## Más recursos útiles 

Esto era sólo una guia introductoria. No es funcional documentarse o estudiar mucho sin antes comenzar a usar el sistema operativo Linux. Aprenderás de manera más solida si con el uso te van surgiendo necesidades a las que vas dando solución poco a poco. Pero si la computadora es tu herramienta de trabajo, es tu deber conocerla. Puedes encontrar -o contribuir añadiendo- más información útil en el siguiente listado.

### Documentación
https://en.wikipedia.org/wiki/List_of_Linux_distributions    
https://www.linux.com/    
https://www.linux.com/what-is-linux    
https://en.wikipedia.org/wiki/Linux    
https://www.linux.org/    
https://en.wikipedia.org/wiki/Unix_shell    
https://www.tldp.org/LDP/intro-linux/html/index.html    
https://www.linux.com/blog/learn/intro-to-linux/2018/4/linux-filesystem-explained   
https://www.tecmint.com/linux-file-system-explained/   

### Tutoriales y cursos gratuitos
http://swcarpentry.github.io/shell-novice-es/    
http://swcarpentry.github.io/shell-novice/    

### Webinars