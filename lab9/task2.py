#Authors: Prince Rios and Alex Espinoza
#Date: 20 February 2020
#Description: This code imports sys and also uploads the QApplication, QWidget, and QLabel classes 
#from the PyQt5 bindings. Then, an application and window is created. Through the use of the QLabel method, the window is given a label.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Lab 9 Task 2')
window.setGeometry(0,0,600,600)
label = QLabel(window)
label.setText('Prince Rios and Alex Espinoza')
window.show()
sys.exit(app.exec())
