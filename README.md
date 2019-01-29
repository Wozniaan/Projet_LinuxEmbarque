# Projet_LinuxEmbarque

Étudiants :
- Maria Luiza Costa Vianna
- Alexandre Houdeville
- Jalal Matar
- Louis Valery
- Anne-Laure Wozniak

## Buildroot
Buildroot est un ensemble de Makefile permettant d'automatiser le processus de build d'une distribution Linux embarquée.

Dans le cadre de ce projet, une tarball Buildroot est disponible via une image Docker [ici](https://github.com/pblottiere/embsys/tree/master/labs/rpi3/docker), sous le nom "buildroot-video". La tarball contient le système d'exploitation précompilé permettant notamment le support de la caméra sur la Raspberry Pi 3.
On vérifie que c'est le cas en s'assurant que les options ```BR2_PACKAGE_RPI_FIRMWARE_X``` et ```BR2_PACKAGE_LIBV4L``` sont activées dans le fichier de configuration de Buildroot (fichier ```embsys_defconfig```).

## Flashage de la carte SD

### Docker
```
$ sudo docker pull pblottiere/embsys-rpi3-buildroot-video
```
### Flashage

```
$ sudo dd if=sdcard.img of=/dev/sdb
```

## Installation de V4L



## Compilation et installation 

