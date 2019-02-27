# Copie des fichiers v4l et servo-moteur sur carte SD
# NB. A réaliser directement à partir de la carte SD
installation:
	sudo cp servoMoteur/serveur_sm.py /media/c34d1c81-6826-4a82-841c-3acb16da6ded/root
	sudo cp camera/v4l2grab /media/c34d1c81-6826-4a82-841c-3acb16da6ded/root

# Lancement de v4l2grab et prise de photo "à la main"
# NB. A réaliser depuis un terminal série connecté à la RPI3 (gtkterm)
v4l2:
	modprobe bcm2835-v4l2
	cd /root
	./v4l2grab -d /dev/video0 -o img.jpg

# Communication avec la Raspberry
# NB. Vérifier que l'étape Configuration IP est OK
# A lancer depuis 3 terminaux différents
serveur1:
	python client_serveur_python/server.py
serveur2:
	python client_serveur_python/server2.py
client:  
	python client_serveur_python/client.py
