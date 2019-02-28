
# -*- coding: utf-8 -*-            
"""
Created on Tue Jan 29 09:51:44 2019                        
                                                         
@author: louis                                             
"""                                                   
                                                           
import RPi.GPIO as GPIO                                  
import time                                                
import socket                                              
import signal                                                        
import sys                                                          
                                                      
                                                          

                                                         
GPIO.setmode(GPIO.BCM)                                     
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)                                    
                                                         
# Initialisation position                                
current_angle = 50                                        
angle_init = current_angle/10 + 5                          
pwm=GPIO.PWM(17,100)                                       
pwm.start(5)                                             
                                                                  
pwm.ChangeDutyCycle(angle_init)                                        
time.sleep(2) 

def signal_terminate_handler(signum, frame):
    """
    Signal handler
    
    Permet de gerer la fermeture du socket lors d'une interruption volontaire du serveur
    """
    
    print("Received signal: {}. Your server is terminated ".format(signum))
    client.close()
    socket_sm.close()
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_terminate_handler)
signal.signal(signal.SIGINT, signal_terminate_handler)
                                                    
hote = '' #adresse IP du serveur
port = 12820 #port d'acces au serveur du servomoteur

print"\n+----------/ ServoMoteur  Controlleur /----------+"
print"|                                                |"
print"| Le Servo doit etre branche au pin 11 / GPIO 17 |"
print"|                                                |"
print"+------------------------------------------------+\n"
                                 
             
""" acceptation de la connexion au client """

socket_sm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sm.bind((hote, port))         
socket_sm.listen(5) 
client, adress = socket_sm.accept()                    
print "{} connected".format(adress) 

""" communication avec le client """

choix = b""
                                
while choix != b"fin":             
    print "serveur microcontroller listening"            
                                                           
    choix = client.recv(255)
    print choix
    print type(choix)

    choix = choix.decode()
    print choix
    print type(choix)
    

    try:
        choix = int(choix)
    except ValueError:
        print "Oups, ce n est pas un int"

                         
    if (choix != 1 and choix != 2 ):           
        print "ERROR: expected 1 or 2, received {}".format(choix)

                                                           
    if (choix == 1) :                                      
        delta_angle = -10                                       
    elif(choix == 2):                                      
        delta_angle = 10                                        
    else:
        delta_angle = 0    
                                                       
    duree = 0                                            
    angleChoisi = (current_angle + delta_angle)/10 + 5  #increment de 5 degres a chaque fois
           
    if angleChoisi <= 6: #evite servomoteur en butee
        angleChoisi = 6                                   
    elif angleChoisi >= 25:                                       
        angleChoisi = 25                                               
    print angleChoisi   
                                              
    pwm.ChangeDutyCycle(angleChoisi)          
    time.sleep(duree)                                             
                                                                       
    current_angle += delta_angle 
    client.send(b"5 / 5")       

GPIO.cleanup() 
socket_sm.close()

try:
    client.close()
except SyntaxError:
    print "client does not exist yet"
