#Authors: Prince Rios and Alex Espinoza
#Date modified: 21 February 2020
#Description: This code imports sys, Image, and other necessary classes. Then, a class is created representing
#a window. After this, the window is given a size. Next, a label and push button is created. Next, box layouts are created and the label and push
#button are added to this layout. At the end of the ui method, the window is shown.
import sys
from PyQt5.QtWidgets import (QApplication, QHBoxLayout,
QLabel, QPushButton, QVBoxLayout, QWidget)
class Button(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()
	def init_ui(self):
		self.setGeometry(0,0,600,600)
		self.setWindowTitle('Lab 8- Task 4')
		self.button1 = QPushButton('Push me')
		self.button2 = QPushButton('Push me')
		self.label = QLabel('Button has not been pushed')
		first_box = QHBoxLayout()
		first_box.addWidget(self.label)
		first_box.addStretch()
		second_box = QVBoxLayout()
		second_box.addWidget(self.button1)
		second_box.addWidget(self.button2)
		second_box.addLayout(first_box)
		self.setLayout(second_box)
		self.button1.clicked.connect(self.btn_click)
		self.show()
	def btn_click(self):
		self.label.setText('Button clicked')
app = QApplication(sys.argv)
window = Button()
sys.exit(app.exec_())