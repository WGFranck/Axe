#Vendredi 1 Février
import sys
from PyQt5 import QtGui, QtWidgets

def on_va_voir():
    global etat
    etat =  1
    print("ON")
    
def create_button(x, y, t, cb):
    global window
    xw = 15 + 55*x
    yw = 40 + 20*y
    button = QtWidgets.QPushButton(t, window)
    button.move(xw, yw)
    button.resize(55, 20)
    button.clicked.connect(cb)
    
def main():
    global window
    global etat
    etat = 0
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.resize(250, 150)
    window.setWindowTitle("Programme ISN")
    
    def key_operation(u):
        def real_key_operation():
            print("On a cliqué sur", u)
        return real_key_operation
    
    def key_relative():
        print("On a cliqué sur +/-")
        
    def key_point():
        print("On a cliqué sur .")
    
    def key_equal():
        print("On a cliqué sur =")
        
    def key_square_root():
        print("On a cliqué sur √")
    
    def key_all_clear():
        print("On a cliqué sur AC")
        
    def key_clear():
        print("on a cliqué sur C")
        
    def key_digit(n):
        def real_key_digit():
            print("On a cliqué sur", n)
        return real_key_digit
    
    
    create_button(0, 0, "C",   key_clear)
    create_button(1, 0, "AC",  key_all_clear)
    create_button(2, 0, "√",   key_square_root)
    create_button(3, 0, "=",   key_equal)
    create_button(0, 1, "7",   key_digit(7))
    create_button(1, 1, "8",   key_digit(8))
    create_button(2, 1, "9",   key_digit(9))
    create_button(3, 1, "+",   key_operation("+"))
    create_button(0, 2, "4",   key_digit(4))
    create_button(1, 2, "5",   key_digit(5))
    create_button(2, 2, "6",   key_digit(6))
    create_button(3, 2, "-",   key_operation("-"))
    create_button(0, 3, "1",   key_digit(1))
    create_button(1, 3, "2",   key_digit(2))
    create_button(2, 3, "3",   key_digit(3))
    create_button(3, 3, "*",   key_operation("*"))
    create_button(0, 4, ".",   key_point)
    create_button(1, 4, "0",   key_digit(0))
    create_button(2, 4, "+/-", key_relative)
    create_button(3, 4, "/",   key_operation("/"))    

    window.show()
    sys.exit(app.exec_())
    
main()
