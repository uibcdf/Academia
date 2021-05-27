Source: \\
http://nglviewer.org/nglview/latest/

```bash
conda install nglview -c conda-forge
conda install nodejs

# No estoy seguro de que esta linea siga siendo funcional
# Tengo que probar sin jupyter_nbextensions_configurator y sin esta linea
jupyter-nbextension enable nglview --py --sys-prefix

# Con estas lineas funcionó con jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install jupyter-matplotlib
jupyter-labextension install nglview-js-widgets
```
----------------------

```bash
jupyter-labextension update --all
jupyter lab build
```
