# coding: utf-8

import socket
import cv2
import numpy as np
import signal

def signal_terminate_handler(signum, frame):
    """ 
    Signal handler
    
    Permet de gerer la fermeture du socket lors d'une interruption volontaire du client
    """
    
    print "Received signal: {}. Fermeture de la connexion ".format(signum)
    connexion_avec_serveur.close()
    connexion_avec_serveur2.close()

signal.signal(signal.SIGTERM, signal_terminate_handler)
signal.signal(signal.SIGINT, signal_terminate_handler)

hote1 = "localhost" #adresse IP du client
port1 = 12800 #port d'acces au serveur 1 (servomoteur)
port2 = 12810 #port d'acces au serveur 2 (camera)
countImage = 1

""" connexion serveur servomoteur """
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote1, port1))
print("Connexion établie avec le serveur sur le port du servomoteur {}".format(port1))


"""connexion serveur camera """
connexion_avec_serveur2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur2.connect((hote1, port2))
print("Connexion établie avec le serveur sur le port du servomoteur {}".format(port2))



msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = raw_input("Entrer commande sous forme: moteur camera ou moteur: 1 pour rotation vers la gauche 2 pour rotation vers la droite, camera : s pour prendre la photo, x sinon\n")
    # Peut planter si vous tapez des caractères spéciaux
    if (msg_a_envoyer[0] != '1' and msg_a_envoyer[0] != '2') or (msg_a_envoyer[2] != "s" and msg_a_envoyer[2] != "x") or (msg_a_envoyer[1] != " ") or (len(msg_a_envoyer) > 3):
        print("Le format de la commande n'est pas bon")

    else:

        """communication serveur moteur """
        msg_a_envoyer_motor = msg_a_envoyer[0].encode()
        # On envoie le message
        connexion_avec_serveur.send(msg_a_envoyer_motor)
        msg_recu = connexion_avec_serveur.recv(1024)
        print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents


        """communication serveur camera """
        msg_a_envoyer_camera = msg_a_envoyer[2].encode()
        # On envoie le message
        connexion_avec_serveur2.send(msg_a_envoyer_camera)
        msg_recu = connexion_avec_serveur2.recv(40960000)
        print('Image ' + str(countImage) + ' recu')
        nparr = np.fromstring(msg_recu, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite('image' + str(countImage) + '.jpg',img_np)
        countImage = countImage + 1


print("Fermeture des connexions aux serveurs")
connexion_avec_serveur.close()
connexion_avec_serveur2.close()
