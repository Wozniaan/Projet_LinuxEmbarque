
# -*- coding: utf-8 -*-            
"""
Created on Tue Jan 29 09:51:44 2019                        
                                                         
@author: louis                                             
"""                                                   
                                                           
import RPi.GPIO as GPIO                                  
import time                                                
import socket                                              
                                                         
                                                          
                                                         
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

                                                    
hote = ''
port = 12800

print"\n+----------/ ServoMoteur  Controlleur /----------+"
print"|                                                |"
print"| Le Servo doit etre branche au pin 11 / GPIO 17 |"
print"|                                                |"
print"+------------------------------------------------+\n"
                                 
print"Comment controler le Servo ?"
             
                         
socket_sm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sm.bind((hote, port))         
socket_sm.listen(5) 
client, adress = socket_sm.accept()                    
print "{} connected".format(adresse) 

                                 
while True:             
    print "serveur microcontroller listening"            
                                                           
    choix = client.recv(255) 
                             
    if (int(choix) != 1 or int(choix) != 2 ):           
        print "ERROR: expected 1 or 2, received {}".format(choix)
#    choix = int(input("1. aller à gauche\n2. pour aller à droite\n"))
                                                           
    if (choix == 1) :                                      
        delta_angle = -5                                       
    elif(choix == 2):                                      
        delta_angle = 5                                        
                                                           
    duree = 0                                            
    angleChoisi = (current_angle + delta_angle)/10 + 5  #increment de 5 degré à chaque fois
           
    if angleChoisi <= 6: #evite servomoteur en butee
        angleChoisi = 6                                   
    elif angleChoisi >= 25:                                       
        angleChoisi = 25                                               
    print angleChoisi   
                                              
    pwm.ChangeDutyCycle(angleChoisi)          
    time.sleep(duree)                                             
                                                                       
    current_angle += angle 
          
GPIO.cleanup() 
socket_sm.close()
client.close()