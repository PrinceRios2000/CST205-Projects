#Authors: Prince Rios and Alex Espinoza
#Date: 4 March 2020
#Description: This code imports the flask class from the flask library. Then, creates a flask application followed by the route()
#function to connect the URL to the word hello. Finally, a function is created to print Hello world from Flask in the website.
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')

def hello():
	return 'Hello world from Flask'

#@app.route('/template')
#
#def template():
#	return render_template('myTemplate.html')
