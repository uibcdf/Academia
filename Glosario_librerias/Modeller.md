
Hay que pedir licencia gratuita para uso no comercial:    
https://salilab.org/modeller/registration.html    

Para incluir la variable (clave de licencia):

```bash
vim $CONDA_PREFIX/lib/modeller-9.20/modlib/modeller/config.py
```

```bash
license = r'MODELLERKEY'
```

```bash
conda config --add channels omnia # si no está ya
conda config --add channels salilab
conda install modeller
```

El canal omnia tiene una copia del paquete en su repositorio de anaconda. Este paquete puede estar todavía no actualizado si salilab colgó un modeller nuevo recientemente. Pero la copia de omnia es suficiente para el propósito de nuestro laboratorio.

