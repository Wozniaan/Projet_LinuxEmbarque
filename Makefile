#Copie des fichiers v4l et servo-moteur sur Raspberry
installation:
	sudo cp servoMoteur/serveur_sm.py /media/c34d1c81-6826-4a82-841c-3acb16da6ded/root
	sudo cp camera/avecSocket/v4l2grab /media/c34d1c81-6826-4a82-841c-3acb16da6ded/root

#Lancement de v4l2grab et prise de photo "à la main"
#(depuis un terminal sur la rpi3)
v4l2:
	modprobe bcm2835-v4l2
	cd /root
	./v4l2grab -d /dev/video0 -o img.jpg

#Communication avec raspberry
#	python client_serveur_python/server.py
#	python client_serveur_python/server2.py
client:  
	python client_serveur_python/client.py
