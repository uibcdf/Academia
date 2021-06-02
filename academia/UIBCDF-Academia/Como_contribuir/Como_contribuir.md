<div style='text-align: right;'> <a href="../README.md">Regresar</a> </div>

-----
<br>


# Cómo contribuir a desarrollar UIBCDF-Academia.

<div class="alert alert-info" role="alert">
<strong>Info:</strong> Si crees que este notebook necesita algún cambio no dudes en <a href="Como_contribuir.md" class="alert-link">contribuir a su desarrollo</a>.
</div>

<div class="alert alert-danger" role="alert">
<strong>En desarrollo:</strong> 0%.
</div>

<br>


## Implementando cambios en el repositorio central

Supongamos que has detectado un error y lo quieres corregir, o consideras que la explicación no es clara, quieres añadir un párrafo, o conoces documentación o tutoriales que quieres compartir en la lista del fin
al de un notebook. Edita lo que quieras en el notebook y cuando consideres que está listo reinicialo y ejecútalo de principio a fin. Despúes compromete los cambios y haz un 'Pull Request' (PR en la jerga de Git)
. Veamos esto paso a paso.

### Si no tienes permisos de edición

En este caso lo más probable es que hayas decidido hacer tu propio fork del repositorio. En ese caso puedes recurrir a la página web de github de tu fork, o puedes solicitar el 'Pull Request' haciendo uso de la 
[web del repositorio de academia](https://github.com/uibcdf/Academia).

Antes, asegurate de ciertas cosas. Si has estado jugando con tu fork de Academia necesitamos que los cambios relativos a tus pruebas de aprendizaje no estén entre la lista de modificaciones que vas a compartir. 
Es muy conveniente que hayas estado jugando en una rama creada para tal propósito, o que si has estado modificando 'master' deshagas los cambios que no quieres compartir. Si tienes el 'master' limpio y actualiza
do, te sugerimos que hagas una nueva rama y la empujes a tu fork central de GitHub.

Con el `master` del clon local de tu fork limpio crea una rama para tu modificación o modificaciones:

```bash
git checkout -b nombre_de_la_rama # usa un nombre que la identifique
```

Ahora empuja tu rama a tu repositorio del fork:

```bash
git push origin nombre_de_la_rama
```

Ya puedes en local hacer los cambios que quieres subir y comprometerlos en esa rama:

```bash
git commit -a -m 'descripción breve de cambios'
git push origin nombre_de_la_rama
```

Para despues hacer el 'Pull Request' haciendo uso de la [web del repositorio de academia](https://github.com/uibcdf/Academia). Haz click en 'New Pull Request':


<br>
<center>
<img src="pr.png" width="700">
</center>
<br>

Haz click entonces la opción 'compare across forks' en el botón derecho para su comparación con el `master`, y elige tu repositorio y la rama que quieres fusionar con el `master` del repositorio original de Academia:

<br>
<center>
<img src="choose_fork_branch_pr.png" width="550">
</center>
<br>

Documenta tu PR dando un poco de información sobre los cambios que has realizado para que podamos discutir su aceptación. Tu solicitud será revisada y evaluada por todos su aprobación.

Puedes tener un poco más información sobre este proceso [aquí](https://help.github.com/articles/creating-a-pull-request/).

### Si tienes permisos de edición

En este caso, si optaste por hacer un 'fork' del repositorio central en tu usuario, la sección anterior describe el procedimiento más adecuado para hacer un 'Pull Request' (PR en la jerga de Git).

Si en lugar de eso hiciste un clon del repositorio de Academia en el grupo UIBCDF de Github y has estado jugando con tu clon local necesitamos que los cambios relativos a tus pruebas no estén entre la lista de modificaciones que vas a compartir. Deshaz los cambios, pídele a git que vuelva a la versión original, o directamente haz un nuevo clon donde tu quieras:

```bash
cd ~/Projects/
git clone git@github.com:uibcdf/Academia Academia_limpia
cd Academia_limpia
```

Con el clon limpio crea una rama para tu modificación o modificaciones:

```bash
git checkout -b nombre_de_la_rama # usa un nombre que la identifique
```

Ahora empuja tu rama al repositorio central:

```bash
git push origin nombre_de_la_rama
```

Ya puedes en local hacer los cambios que quieres subir y comprometerlos en esa rama:

```bash
git commit -a -m 'descripción breve de cambios'
git push origin nombre_de_la_rama
```

Para despues hacer el 'Pull Request' haciendo uso de la [web del repositorio de academia](https://github.com/uibcdf/Academia). Haz click en 'New Pull Request':

<br>
<center>
<img src="pr.png" width="700">
</center>
<br>

Elige entonces tu rama en el botón derecho para su comparación con el `master`:

<br>
<center>
<img src="choose_branch_pr.png" width="550">
</center>
<br>

Documenta tu PR dando un poco de información sobre los cambios que has realizado, para su aceptación.
Tu solicitud será vista y discutida por todos hasta su aprobación.

Puedes tener un poco más información sobre este proceso [aquí](https://yangsu.github.io/pull-request-tutorial/) o [aquí](https://help.github.com/articles/creating-a-pull-request/).

#### Ayuda

En caso de que necesites más información a propósito de cómo implementar cambios o interaccionar con el repositorio remoto, puedes visitar la unidad de [introducción a GitHub](GitHub.ipynb). Si has tenido algún problema técnico puedes compartirlo con nosotros en [el foro de GitHub del panel de este repositorio](https://github.com/uibcdf/Academia/issues/3), allí centralizamos los problemas y soluciones para que la experiencia se acumule de manera visible para todos.





<br />

-------
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/uibcdf/Academia">UIBCDF-Academia</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/uibcdf/Academia/graphs/contributors">UIBCDF Lab, autores y colaboradores</a> es material protegido bajo una licencia <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

