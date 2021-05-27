<center>
<img src="https://s3.amazonaws.com/cms.ipressroom.com/219/files/20149/544a60fef6091d588d000046_NVIDIA_CUDA_V_2C_r/NVIDIA_CUDA_V_2C_r_800845fc-6f2d-47cf-94bb-50f01f6c0ae9-prv.jpg" width="400">
</center>

---
`Nota: Si crees que este notebook necesita algún cambio no dudes en contribuir a su desarrollo.`

---

# ¿Qué es CUDA?

CUDA (del inglés *Compute Unified Device Architecture*) es la plataforma de software desarrollado por Nvidia -productor de GPUs- para que los lenguages de programación como C o C++ puedan comunicarse y dar instrucciones a la GPU. La GPU es la tarjeta gráfica de la computadora, del inglés *Graphics Processing Unit*. La GPU tiene una arquitectura que la hace altamente eficiente para los cálculos necesarios para ejecutar y mover un videojuego. La GPU es un dispositivo de cálculo con muchos más nucleos, unidades de procesamiento, que la CPU que está integrada en la placa madre de la computadora. Y un simulador de vuelo, un juego de futbol o de carreras de autos F1, una aventura gráfica en primera persona, son mundos virtuales con un realismo asombroso cuya evolución se calcula en tiempo real respondiendo inmediatamente a decisiones del jugador. Ahora imagina que pudieramos usar la GPU no para simular la física del coche, del avión, o de los objetos de ese mundo virtual en el que transcurre la historia del juego, sino para simular la física de una biomolécula. Esto es lo que han conseguido los programas de simulación de dinámica molecular con CUDA. CUDA incluye un compilador y permite que podamos desarrollar software que pueda ejecutar instrucciones no solamente en la CPU, sino también en la GPU. En lo que respecta a integrar la dinámica de un objeto físico en un mundo 3D, la GPU de tu computadora es probablemente decenas de veces más rápida que tu CPU.

Es por eso que necesitamos instalar CUDA en la computadora. Los programas que usaremos para simular y analizar la dinámica de biomoléculas se compilan para el uso de CUDA como puente hacia la GPU. Si no tuvieras CUDA, puedes simular con la CPU o haciendo uso de OpenCL con la GPU también, pero ahora nada tan rápido como usar CUDA en el software que vamos a manejar.

#### Nota
CUDA está diseñada para ser óptima con tarjetas gráficas de Nvidia. Puede trabajar también con tarjetas ATI/AMD, y seguramente con ese hardware la eficiencia de CUDA sea parecida a la de OpenCL. Los autores de este notebook no tiene nada particularmente a favor de ninguna empresa de hardware. Pero esta guía se ha redactado así porque en el laboratorio no tenemos actualmente tarjetas ATI/AMD.

# ¿Cómo se instala?

Instalamos cuda en el entorno de conda. Podemos hacerlo mediante [el paquete cudatoolkit del repositorio conda-forge](https://anaconda.org/anaconda/cudatoolkit), o mediante las distintas versiones de cuda que ofrece [el canal omnia](https://anaconda.org/omnia/repo?sort=_name&sort_order=asc).

Lo haremos de la primera manera:

```bash
conda install -c conda-forge cudatoolkit
```

En el momento de escribir este notebook, la versión de cuda ofrecida en conda-forge es la 9.2, y la última versión de openmm está correctamente preparada ella. Lo podemos checar en la salida del siguiente comando:
```bash
conda list | grep cuda
```
```bash
cudatoolkit               9.2                           0  
openmm                    7.3.0           py36_cuda92_rc_1    omnia
```

La versión de cuda debe ser compatible con el driver de nvidia instalado en tu sistema. La versión del driver instalado, así como el modelo de la tarjeta que tenemos en la computadora, puede ser conocida por ejemplo al ejecutar en tu terminal de linux el comando:

```bash
nvidia-smi
```

En mi caso la salida de este comando me dice que tengo el driver 390.77 para mi tarjeta Quadro M2000:

```
Thu Jan  3 17:56:01 2019       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 390.77                 Driver Version: 390.77                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Quadro M2000        Off  | 00000000:03:00.0  On |                  N/A |
| 56%   41C    P8     9W /  75W |   1590MiB /  4042MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1617      G   /usr/lib/xorg/Xorg                            59MiB |
|    0      1661      G   /usr/bin/gnome-shell                          54MiB |
|    0      1856      G   /usr/lib/xorg/Xorg                           412MiB |
|    0      2037      G   /usr/bin/gnome-shell                         325MiB |
|    0      4046      G   /proc/self/exe                               663MiB |
+-----------------------------------------------------------------------------+
```

Como puedo ver en [la lista de compatibilidad entre versiones de drivers de nvida y versiones de CUDA](https://docs.nvidia.com/deploy/cuda-compatibility/index.html#binary-compatibility), mi driver necesita ser actualizado si quiero trabajar con CUDA 9.2 a una versión mayor o igual que la 396.26.

Explicaremos aquí como esta actualización puede ser facilmente hecha en el caso de estar trabajando con la distribución Ubuntu 18.04 LTS.

### Actualización del driver de nvidia

Podemos antes de nada checar en [la correspondiente página web de nvidia](https://www.nvidia.com/Download/index.aspx?lang=es) cúal es el último driver compatible con tu tarjeta gráfica y tu sistema operativo. En mi caso, escogiendo [en dicha página](https://www.nvidia.com/Download/index.aspx?lang=es) las opciones correspondientes a mi GPU y mi sistema operativo: Quadro > Quadro Series > Quadro M2000 > Linux 64-bit > Linux Long Lived Driver; el driver sugerido para trabajar es el 410.93.

Para instalar el driver añadimos el repositorio mantenido por ubuntu para los drivers de nvidia:
```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
```

Si hacemos antes que nada una actualización de los paquetes disponibles en los repositorios veremos que nuestro gestor de paquetes ya nos propone una actualización del driver, aunque todavía a una versión un poco conservadora (en mi caso a la 390.87 y no a la 410.93).

```bash
sudo apt update
sudo apt list --upgradable
```
Por precaución, y por no dar el salto a la 410.93 de una vez, corremos la actualización de paquetes:

```bash
sudo apt upgrade
```

Por último instalamos la versión más actualizada que nvidia nos recomienda, compatible con CUDA 9.2 (en mi caso la 410.93):

```bash
sudo apt install nvidia-driver-410
```

Probablemente el comando anterior no ha instalado nada. Puede abstenerse abstenerse de realizar la instalación debido a que las dependencias sugeridas son críticas y has de ordenar instalarlas a mano. Esta fue mi salida:

```
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 nvidia-driver-410 : Depends: libnvidia-gl-410 (= 410.78-0ubuntu1~gpu18.04.1) but it is not going to be installed
                     Depends: nvidia-dkms-410 (= 410.78-0ubuntu1~gpu18.04.1) but it is not going to be installed
                     Depends: nvidia-kernel-source-410 (= 410.78-0ubuntu1~gpu18.04.1) but it is not going to be installed
                     Depends: libnvidia-decode-410 (= 410.78-0ubuntu1~gpu18.04.1) but it is not going to be installed
                     Depends: libnvidia-encode-410 (= 410.78-0ubuntu1~gpu18.04.1) but it is not going to be installed
                     Depends: nvidia-utils-410 (= 410.78-0ubuntu1~gpu18.04.1) but it is not going to be installed
                     Depends: xserver-xorg-video-nvidia-410 (= 410.78-0ubuntu1~gpu18.04.1) but it is not going to be installed
                     Depends: libnvidia-cfg1-410 (= 410.78-0ubuntu1~gpu18.04.1) but it is not going to be installed
                     Depends: libnvidia-ifr1-410 (= 410.78-0ubuntu1~gpu18.04.1) but it is not going to be installed
                     Recommends: libnvidia-decode-410:i386 (= 410.78-0ubuntu1~gpu18.04.1)
                     Recommends: libnvidia-encode-410:i386 (= 410.78-0ubuntu1~gpu18.04.1)
                     Recommends: libnvidia-ifr1-410:i386 (= 410.78-0ubuntu1~gpu18.04.1)
                     Recommends: libnvidia-fbc1-410:i386 (= 410.78-0ubuntu1~gpu18.04.1)
                     Recommends: libnvidia-gl-410:i386 (= 410.78-0ubuntu1~gpu18.04.1)
E: Unable to correct problems, you have held broken packages.
```

Así que incluyo en la orden de instalación las dependencias y recomendaciones:

```bash
sudo apt install nvidia-driver-410 libnvidia-gl-410 nvidia-dkms-410 nvidia-kernel-source-410 libnvidia-decode-410 libnvidia-encode-410 nvidia-utils-410 xserver-xorg-video-nvidia-410 libnvidia-cfg1-410 libnvidia-ifr1-410 libnvidia-decode-410:i386 libnvidia-encode-410:i386 libnvidia-ifr1-410:i386 libnvidia-fbc1-410:i386 libnvidia-gl-410:i386
```

Si el comando de instalación procede sin sugerir ninguna otra dependencia o recomendación que interrumpa el proceso, en cuyo caso habría que volver a incluirla, al final de la instalación se debe reiniciar la computadora.

Podemos, despues de la reinicialización del sistema operativo, comprabar que el driver de nvidia fue actualizado ejecutando de nuevo `nvidia-smi`:

```bash
nvidia-smi
```
En mi caso vemos que hemos actualizado el driver al 410, ya podré usar CUDA 9.2 sin problemas:

```
Thu Jan  3 19:04:55 2019       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 410.78       Driver Version: 410.78       CUDA Version: 10.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Quadro M2000        Off  | 00000000:03:00.0  On |                  N/A |
| 56%   44C    P0    25W /  75W |    844MiB /  4042MiB |      1%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1620      G   /usr/lib/xorg/Xorg                            58MiB |
|    0      1666      G   /usr/bin/gnome-shell                          54MiB |
|    0      1859      G   /usr/lib/xorg/Xorg                           359MiB |
|    0      2039      G   /usr/bin/gnome-shell                         198MiB |
|    0      2751      G   ...quest-channel-token=4063427587344960568   167MiB |
+-----------------------------------------------------------------------------+
```

# Dudas de uso, problemas técnicos y soluciones.

Para centralizar esas dudas técnicas sobre el tema de este notebook o proponer soluciones o sugerencias más técnicas que queremos encontrar en el futuro comentadas y visibles para todos, haz uso del siguiente canal:

[Foro Técnico: CUDA](https://github.com/uibcdf/Academia/issues/11)

# Más recursos útiles 

El propósito de este notebook es ser un documento únicamente introductorio. Puedes encontrar -o contribuir añadiendo- más información útil en el siguiente listado:

## Documentación
https://www.nvidia.com/     
https://docs.nvidia.com/     
https://www.nvidia.com/Download/index.aspx?lang=es    
https://docs.nvidia.com/deploy/cuda-compatibility/index.html#binary-compatibility
https://www.linuxbabe.com/ubuntu/install-nvidia-driver-ubuntu-18-04    
https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux    
https://www.cyberciti.biz/faq/ubuntu-linux-install-nvidia-driver-latest-proprietary-driver/    
