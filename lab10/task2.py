#Authors: Prince Rios and Alex Espinoza
#Date: 29 February 2020
#Description: This program uses a window class that uses a combo box and labels to display the required features.
#Next, using the currentTextChanged method to signal when the user has selected a different color. There is a button added
#that, when clicked, displays the selected color.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QMainWindow, QFrame
from task2window import NewWindow
from PyQt5.QtGui import QColor
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
		self.button = QPushButton(self)
		self.button.setText('See color')
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
		vbox.addWidget(self.button)
		self.setLayout(vbox)
		self.button.clicked.connect(self.btn_clicked)
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
	def btn_clicked(self):
		hex_values = {
			"Red": [(255, 0, 0), "#FF0000"],
			"Green": [(0, 128, 0), "#008000"],
			"Blue": [(0, 0, 255), "#000FF"],
			"Orange": [(255, 165, 0), "#FFA500"],
			"Pink": [(255, 192, 203), "#FFC0CB"],
			"Vermillion": [(227, 66, 52), "#e34234"]
		}
		self.window1 = QMainWindow()
		self.window1.setWindowTitle('Task 2')
		text = self.combo_box.currentText()
		selected_color = QColor(hex_values[text][0][0], hex_values[text][0][1], hex_values[text][0][2])
		self.frame = QFrame(self.window1)
		self.frame.setStyleSheet('QWidget { background-color: %s}' % selected_color.name())
		self.window1.show()
		# self.ui = NewWindow()
		# self.ui.initUI()
app = QApplication(sys.argv)
hexa = Hex()
sys.exit(app.exec_())