<p style="text-align:left;">
   <a href="../README.md">Ir al menú anterior</a>
   <span style="float:right;">
        <a href="../Implementando/Implementando.md">Ir a la unidad anterior</a>
   </span>
</p>

-----


# Qué es SPHINX y cómo se documenta una libreria de python


<div class="alert alert-info" role="alert">
<strong>Info:</strong> Si crees que este notebook necesita algún cambio no dudes en <a href="../../../../UIBCDF-Academia/Como_contribuir/Como_contribuir.md" class="alert-link">contribuir a su desarrollo</a>.
</div>

<div class="alert alert-danger" role="alert">
<strong>En desarrollo:</strong> 0%
</div>

<br>

- [Dudas, problemas técnicos y soluciones](#dudas)
- [Más recursos útiles](#recursos)
    - [Documentación](#documentacion)
    - [Tutoriales, Webinars y cursos gratuitos](#tutoriales)

## La documentación de una librería

## Sphinx

Sphinx es una librería de python que nos permite crear documentación de otra librería de una manera
muy sencilla en distintos formatos: html, latex, pdf, etc.

```bash
conda install sphinx
```

### Numpy docstrings

Existe una guia oficial de numpydoc docstrings. (Este es el enlace)[https://numpy.org/devdocs/docs/howto_document.html].

#### Métodos

- Cómo se especifica bien el valor por defecto?
- Cómo se reporta la salida de un método. Se le pone nombre a las variables de salida aunque el
  nombre sólo sea una explicación... no un nombre de variable?
- Cuando un parametro es un numpy array de un shape determinado, cómo se especifica?

#### Examples

https://github.com/PyPSA/atlite/issues/38

https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting Equations.html

https://www.python.org/doc/essays/styleguide/

https://namingconvention.org/python/

https://mathjax.github.io/MathJax-demos-web/


#### Clases

Para conocer como documentar una clase podemos recurrir a (la sección indicada de la guía de
numpydoc docstrings)[https://numpy.org/devdocs/docs/howto_document.html#id12]

Veamos el siguiente ejemplo

```python



```

:return: A numpy array.
:rtype: numpy.ndarray (dtype=np.int)

según https://stackoverflow.com/questions/58994110/use-sphinx-to-document-a-numpy-array-dtype-within-the-rtype-field


### Google docstrings

### Napoleon

### Autosummary, ...

### Extensiones...
 Qué es?

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'numpydoc',
    'sphinx.ext.githubpages',
    'sphinxcontrib.bibtex',
    'nbsphinx'
]


---

## Dudas, problemas técnicos y soluciones. <a class="anchor" id="dudas"></a>

Para centralizar esas dudas, sugerencias o soluciones técnicas sobre el tema de este notebook, haz uso del siguiente canal:

[Foro Técnico: X](https://github.com/uibcdf/Academia/issues/X)


## Más recursos útiles <a class="anchor" id="recursos"></a>

Esto era sólo una guia introductoria. No es funcional documentarse o estudiar mucho sin antes comenzar a usar el sistema operativo Linux. Aprenderás de manera más solida si con el uso te van surgiendo necesidades a las que vas dando solución poco a poco. Si la computadora es tu herramienta de trabajo, es tu deber conocerla. Puedes encontrar -o contribuir añadiendo- más información útil en el siguiente listado.

### Documentación <a class="anchor" id="documentacion"></a>

https://brendanhasz.github.io/2019/01/05/sphinx.html   
https://developer.lsst.io/python/numpydoc.html    
https://realpython.com/documenting-python-code/    
https://python-sprints.github.io/pandas/guide/pandas_docstring.html   
https://docs.python-guide.org/writing/documentation/   
https://stackabuse.com/python-docstrings/   
https://www.datacamp.com/community/tutorials/docstrings-python   
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html    
https://numpydoc.readthedocs.io/en/latest/format.html     
https://realpython.com/courses/documenting-python-projects-sphinx-read-the-docs/    
https://pythonhosted.org/an_example_pypi_project/sphinx.html    
https://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/     
https://numpydoc.readthedocs.io/en/latest/

https://www.pythonforthelab.com/blog/documenting-with-sphinx-and-readthedocs/
https://www.pythonforthelab.com/blog/
https://numpydoc.readthedocs.io/en/latest/format.html
https://numpy.org/devdocs/docs/howto_document.html
https://nbsphinx.readthedocs.io/en/0.5.0/index.html

### Tutoriales, Webinars y cursos gratuitos <a class="anchor" id="tutoriales"></a>


<br>

<div style='text-align: right;'> <a href="../Testeo/Testeo.md">Ir a la siguiente unidad</a> </div>

-------
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/uibcdf/Academia">UIBCDF-Academia</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/uibcdf/Academia/graphs/contributors">UIBCDF Lab, autores y colaboradores</a> es material protegido bajo una licencia <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>


