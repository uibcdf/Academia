# Caso práctico de creación de documentación con Sphinx para una librería de Python

Veamos un sencillo caso de creación de documentación para una librería de python con Sphinx.
Dado que vamos a comenzar de cero, en primer lugar crearemos el código en un nuevo repositorio de GitHub.

## Creación del proyecto en GitHub

## Elección del nombre

Elijamos en primer lugar el nombre del nuevo proyecto. ¿Qué tal por ejemplo "Proyecto_Cayetano"?
Vamos a hacer uso de GitHub para publicar en internet nuestra documentación y nuestro código, al
acceso de cualquiera.

## ¿Por qué en GitHub?

Podríamos crear con git un repositorio local y luego servir la documentación html en una página web
privada o haciendo uso del servicio gratuito [ReadTheDocs](https://readthedocs.org/), pero GitHub
como veremos también nos permite "servir" nuestras páginas html públicamente en internet a la vez
que nos hace de repositorio remoto de nuestro proyecto.

## Creación del repositorio

Como se ha descrito en otra unidad de Academia, vamos a crear en primer lugar el repositorio remoto
de nuestro proyecto. Accede a la web de tu usuario en GitHub y crea el repositorio
"Proyecto_Cayetano" (como se indica aquí).





Podríamos ir a la web de nuestro usuario en GitHub para crear allí el nuevo repositorio y luego
clonarlo en nuestra computadora. Pero dado que puede que ya sepas resolver la creación de un nuevo
repositorio de esa manera, hagamoslo al reves. Vamos a crear en primer lugar una carpeta en nuestra computadora para el proyecto. Esta carpeta será declarada como nuevo
repositorio de git -en este momento únicamente "local"-.

```bash
mkdir Proyecto_Cayetano
cd Proyecto_Cayetano
git init
```

Añadamos un breve fichero README.md como primer archivo del repositorio:

```bash
touch README.md
```

Edita su contenido añadiendo un par de lineas como por ejemplo:

```
# Proyecto Cayetano

Un proyecto falso para ilustrar cómo se documenta una librería de python con Sphinx
```

Ahora pídele a git que añada el fichero README.md a su listado de ficheros seguidos y compromete el
cambio con un comentario cualquiera:

```bash
git add README.md
git commit -a -c "Primer fichero del repositorio"
```

Ahora declaremos que este proyecto de git tiene un origen remoto en nuestra web de GitHub, en mi
caso https://github.com/dprada, con el mismo nombre "Proyecto_Cayetano":

```bash
git remote add origin https://github.com/dprada/Proyecto_Cayetano.git
```

Y ahora empujemos nuestra rama main del repositorio local al remoto:

```bash
git push origin main
```

El comando anterior te pedirá por linea de comandos el nombre de usuario y contraseña de tu perfil
en GitHub. En el caso de que hayas activado la autenticación por doble factor (2FA) en la
configuración de tu usuario encontraras que, aun introduciendo correctamente usuario y contraseña,
el comando arroja un error. Para resolverlo debes generar un token como se indica [aquí](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line), [aquí](https://medium.com/@ginnyfahs/github-error-authentication-failed-from-command-line-3a545bfd0ca8) o
[aquí](https://mycyberuniverse.com/how-fix-fatal-authentication-failed-for-https-github-com.html).

