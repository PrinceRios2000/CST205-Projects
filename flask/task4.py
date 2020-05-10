from flask import Flask, render_template
from PyQt5.QtWidgets import QPushButton
app = Flask(__name__)

@app.route('/template')

def hello():
	button = QPushButton()
	hex_values = {
		"Red": [(255, 0, 0), "#FF0000"],
		"Green": [(0, 128, 0), "#008000"],
		"Blue": [(0, 0, 255), "#000FF"],
		"Orange": [(255, 165, 0), "#FFA500"],
		"Pink": [(255, 192, 203), "#FFC0CB"],
		"Vermillion": [(227, 66, 52), "#e34234"]
	}
	return render_template('myTemplate.html', s_list = hex_values)