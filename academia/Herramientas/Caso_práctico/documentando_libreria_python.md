# Qué es SPHINX y cómo se documenta una libreria de python

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


-----
## Otras fuentes:

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

