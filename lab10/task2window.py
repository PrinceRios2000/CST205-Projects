import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QFrame
from PyQt5.QtGui import QColor
class NewWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.show()
	def initUI(self):
		self.setGeometry(500, 200, 300, 100)
		self.setWindowTitle('Color')
		self.label = QLabel(self)
		selected_color = QColor(0, 0, 255)
		self.frame = QFrame(self)
		self.frame.setStyleSheet('QWidget { background-color: %s}' % selected_color.name())
		self.label.setText('sped')
		self.show()
app = QApplication(sys.argv)