import pyfiglet
import colorama
import time
import random
import os

nameOfUser = input("Saisir votre nom svp: \n")

"""
111111111111111111111111111111111
Fonts names:
font = "digital"
font = "bulbhead"
font = "bubble"
font = "dotmatrix"
font = "alligator"
font = "letters"
font = "isometric1"
font = "doh"
font = "banner3-D"
font = "alphabet"
font = "5lineoblique"
font = "3x5"
font = "3-d"
font = "slant"
font='5lineoblique'
font='Calibri'
111111111111111111111111111111111
"""
  
result = pyfiglet.figlet_format("Geeks For Geeks", font = "digital")
result2 = pyfiglet.figlet_format(nameOfUser, font = "banner3-D")
print(result)
print(result2)


couleur = list(vars(colorama.Fore).values())

def pr214():
    print('11111111111111         111111111111111111           11111111111111111111      1111111      11111111                  ')
    print('1111111111111111       11111111111111111111         11111111111111111111      1111111      11111111                  ')
    print('11111111111111111      111111111111111111111        11111111111111111111      1111111      11111111                  ')
    print('111111     111111      111111          11111                      111111      1111111      11111111                  ')
    print('111111     111111      111111          11111                      111111      1111111      11111111                  ')
    print('111111     111111      111111          11111                      111111      1111111      11111111         111111   ')
    print('1111111111111111       11111111111111111111         11111111111111111111      1111111      11111111         111111   ')
    print('111111111111111        1111111111111111111          11111111111111111111      1111111      11111111111111111111111   ')
    print('1111111111111          11111111111111111            11111111111111111111      1111111      11111111111111111111111   ')
    print('111111                 111111   1111111             111111                    1111111      11111111111111111111111   ')
    print('111111                 111111     111111            111111                    1111111                      1111111   ')
    print('111111                 111111       111111          111111                    1111111                      1111111   ')
    print('111111                 111111         111111        11111111111111111111      1111111                      1111111   ')
    print('111111                 111111           111111      11111111111111111111      1111111                      1111111   ')


    

#function permettant d'afficher le contenu de cette 
def affichage():
    for i in range(100):   
        time.sleep(0.001)
        #j'affiche et je change la couleur du contenu
        print(random.choice(couleur),"11"*65)
    #le systeme patiente 3 secondes avant d'effacer l'écran avec cls
    time.sleep(3)    
    os.system('cls')

    for i in range(20):
        #j'affiche et je change la couleur du contenu de la fonction pr214
        print(random.choice(couleur),pr214())   
        # time.sleep(0.1)
        # os.system('cls')

affichage()
