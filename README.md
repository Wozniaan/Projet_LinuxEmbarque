# Projet_LinuxEmbarque

Étudiants :
- Maria Luiza Costa Vianna
- Alexandre Houdeville
- Jalal Matar
- Louis Valery
- Anne-Laure Wozniak

## Flashage de la carte SD

### Buildroot
Buildroot est un ensemble de Makefile permettant d'automatiser le processus de build d'une distribution Linux embarquée.

Dans le cadre de ce projet, une tarball Buildroot est disponible via une image Docker [ici](https://github.com/pblottiere/embsys/tree/master/labs/rpi3/docker), sous le nom "buildroot-video". La tarball contient le système d'exploitation précompilé qui sera embarqué sur la carte Raspberry Pi 3. Ce système supporte notamment la caméra que l'on souhaite manipuler. Afin de pouvoir interagir avec la caméra, on utilisera l'API de [V4L](https://linuxtv.org/downloads/v4l-dvb-apis/uapi/v4l/v4l2.html).

On peut vérifier que tout est correctement configuré en s'assurant que les options `BR2_PACKAGE_RPI_FIRMWARE_X`  et `BR2_PACKAGE_LIBV4L` sont activées dans le fichier de configuration de Buildroot (fichier `/configs/embsys_defconfig`). Pour cela, il faudra cependant ouvrir au préalable un conteneur à l'aide de Docker et extraire la tarball.

### Docker
Pour accéder au système précompilé, on utilise Docker. Il s'agit d'un logiciel libre permettant la mise en oeuvre de conteneurs (environnements) de façon à isoler des applications (ici, notre système précompilé). Le kernel partage alors les ressources du système hote et intéragit avec chacun des conteneurs en fonctionnement. Docker se distingue ainsi d'une machine virtuelle qui isole un système et dispose de ses propres ressources.

![IMG_Docker](https://www.docker.com/sites/default/files/d8/2018-11/docker-containerized-and-vm-transparent-bg.png)
source : https://www.docker.com/

Commandes :
```
$ sudo docker pull pblottiere/embsys-rpi3-buildroot-video
$ sudo docker run -it pblottiere/embsys-rpi3-buildroot-video /bin/bash
# cd /root
# tar zxvf buildroot-precompiled-2017.08.tar.gz
```
Concrètement, on récupère l'image Docker puis on crée un conteneur. Ensuite, on extrait le système.
On peut alors réaliser les vérifications sur les fichiers de configuration. Comme le système est précompilé, cela signifie que nous n'avons pas besoin de faire la configuration et le build à la main (`make embsys_defconfig`, `make menuconfig` et `make`). On peut passer directement au flashage.

### Flashage

Afin de flasher la carte SD qui sera insérée dans la Raspberry Pi 3, on doit tout d'abord créer une image :
```
$ docker cp <container_id>:/root/buildroot-precompiled-2017.08/output/images/sdcard.img .
```
On peut alors flasher la carte avec la commande :
```
$ sudo dd if=sdcard.img of=/dev/sdb
```
**NB.** Ici, la carte SD est considéré comme le seconde disque dur (nommé `/dev/sdb` par convention).

A l'issue de cette opération, la carte SD comporte normalement deux partitions.
On peut alors copier `start_x.elf` et `fixup_x.dat` depuis le conteneur sur la 1ère partition de la carte SD et modifier le fichier `config.txt` de la 1ère partition de la carte SD pour ajouter :
````
start_x=1
gpu_mem=128
````
La configuration et le flashage de la carte SD est terminé.

## Installation de V4L



## Compilation et installation 

