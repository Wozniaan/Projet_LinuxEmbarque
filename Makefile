# Copie des fichiers v4l et servo-moteur sur carte SD
# NB. A réaliser directement à partir de la carte SD
installation:
	sudo cp servoMoteur/serveur_sm.py /media/c34d1c81-6826-4a82-841c-3acb16da6ded/root
	sudo cp camera/v4l2grab /media/c34d1c81-6826-4a82-841c-3acb16da6ded/root

# Communication avec la Raspberry
# NB. A réaliser depuis un terminal (client)
#     Vérifier que l'étape Configuration IP est OK
client:  
	python client_serveur_python/client.py
