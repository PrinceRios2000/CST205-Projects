#Authors: Prince Rios and Alex Espinoza
#Date modified: 21 February 2020
#Description: This code imports sys, Image, and other necessary classes. Then, an application is created and a window is also created.
#After this, the window is given a size. Next, a label and Pixmap is created to create an image label. At the end the image is shown. 
import sys
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(0,0,600,600)
window.setWindowTitle('Lab 9 Task 3')
label = QLabel(window) 
my_image = QPixmap('kobe.png')
label.setPixmap(my_image)
label.move(0, 0)
window.resize(my_image.width(),my_image.height())
label.show()
window.show()
sys.exit(app.exec())
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# app = QApplication(sys.argv)
# class MainWindow(QMainWindow):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('CST 205 Main Window')
# mainWin = MainWindow()
# mainWin.show()
# status = app.exec_()
# sys.exit(status)