# Vendredi 18 Janvier
import sys
from PyQt5 import QtGui, QtWidgets

def on_va_voir():
    print("on a vu")

def main():
    app = QtWidgets.QApplication(sys.argv) #Définir application 
    window = QtWidgets.QWidget() # Créer fenêtre
    window.resize(250, 150) #Taille fenêtre
    button = QtWidgets.QPushButton("Bonjour", window) #Définir bouton appelé Bonjour
    button.clicked.connect(on_va_voir)# Quand le bouton est cliqué, lance la fonction on_va_voir
    window.show() #Afficher fenêtre
    sys.exit(app.exec_()) #Exécuter app
    
main()