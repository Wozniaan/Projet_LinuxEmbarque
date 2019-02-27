# coding: utf-8 

import socket
import signal
import sys

def signal_terminate_handler(signum, frame):
    """
    Signal handler
    
    Permet de gerer la fermeture du socket lors d'une interruption volontaire du serveur
    """
    
    print "Received signal: {}. Your server is terminated ".format(signum)
    connexion_avec_client.close()
    connexion_principale.close()
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_terminate_handler)
signal.signal(signal.SIGINT, signal_terminate_handler)

hote = '' #adresse IP du serveur
port = 12830 #port d'acces du serveur

""" acceptation de la connexion au client """
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

""" communication avec le client """
msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    print(msg_recu.decode())
    connexion_avec_client.send(b"5 / 5")

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
