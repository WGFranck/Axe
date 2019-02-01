# Vendredi 25 Janvier
import sys
from PyQt5 import QtGui, QtWidgets

def on_va_voir():
    global etat
    etat =  1
    print("ON")
    
def off():
    global etat
    etat = 0
    print("OFF")
    
def info():
    global etat
    if etat == 0:
        print("Info: OFF")
    else:
        print("Info: ON")
    

def main():
    global etat
    etat = 0
    app = QtWidgets.QApplication(sys.argv) #Définir application 
    window = QtWidgets.QWidget() # Créer fenêtre
    window.resize(250, 150) #Taille fenêtre
    window.setWindowTitle("Programme ISN")
    button = QtWidgets.QPushButton("ON", window) #Définir bouton appelé ON

    buttonoff = QtWidgets.QPushButton("OFF", window)
    
    buttoninfo = QtWidgets.QPushButton("Info", window)
    
    button.move(20, 0) # X Pixels à droite, X en bas
    buttonoff.move (100,0)
    buttoninfo.move (80, 60)
    button.clicked.connect(on_va_voir)# Quand le bouton est cliqué, lance la fonction on_va_voir
    
    buttonoff.clicked.connect(off)
    
    buttoninfo.clicked.connect(info)
    window.show() #Afficher fenêtre
    sys.exit(app.exec_()) #Termine le programme avec un retour
    
main()