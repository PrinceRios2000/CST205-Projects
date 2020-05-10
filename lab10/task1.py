#Authors: Prince Rios and Alex Espinoza
#Date modified: 29 February 2020
#Description: First, we imported classes from QtWidgets that we need to complete the task. Next, we created a window class to create and display
#our window. After this, we created labels to display the required features in the GUI. We then created a dictionary that took in the string as
#colors for the key and the corresponding values are lists of the hex and rgb values of the color. After this, we used combo box.currentText
#to display the hex and rgb values for the selected color.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QComboBox

class Hex(QWidget):
	def __init__(self):
		super().__init__()
		self.UI()
		self.show()
	def UI(self):
		self.setGeometry(500, 200, 300, 100)
		self.setWindowTitle('Colors!')
		self.InitUI()
		self.show()

	def InitUI(self):
		vbox = QVBoxLayout()
		self.label1 = QLabel(self)
		self.label1.setText('CST 205 Color Exchange!')
		self.label2 = QLabel(self)
		self.label2.setText('RGB: ')
		self.label3 = QLabel(self)
		self.label3.setText('Hex: ')
		self.combo_box = QComboBox(self)
		hex_values = {
			"Red": [(255, 0, 0), "#FF0000"],
			"Green": [(0, 128, 0), "#008000"],
			"Blue": [(0, 0, 255), "#000FF"],
			"Orange": [(255, 165, 0), "#FFA500"],
			"Pink": [(255, 192, 203), "#FFC0CB"],
			"Vermillion": [(227, 66, 52), "#e34234"]
		}
		for key, value in hex_values.items():
			self.combo_box.addItem(key)
		self.combo_box.currentTextChanged.connect(self.comboChanged)
		vbox.addWidget(self.label1)
		vbox.addWidget(self.combo_box)
		vbox.addWidget(self.label2)
		vbox.addWidget(self.label3)
		self.setLayout(vbox)
		self.show()
	def comboChanged(self):
		hex_values = {
			"Red": [(255, 0, 0), "#FF0000"],
			"Green": [(0, 128, 0), "#008000"],
			"Blue": [(0, 0, 255), "#000FF"],
			"Orange": [(255, 165, 0), "#FFA500"],
			"Pink": [(255, 192, 203), "#FFC0CB"],
			"Vermillion": [(227, 66, 52), "#e34234"]
		}
		text = self.combo_box.currentText()
		self.label2.setText('RGB: ' + str(hex_values[text][0]))
		self.label3.setText('Hex: ' + hex_values[text][1])

app = QApplication(sys.argv)
hexa = Hex()
sys.exit(app.exec_())