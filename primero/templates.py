from flask import Flask 
from flask import request
from flask import render_template
 	
app = Flask(__name__)

@app.route('/<int:num>')
def index(num = 0):
	return render_template('tmpt.html',age=num)


@app.route('/user/<name>/<int:age>')
def apellidos(name='Juan', age = '0'):
	my_list = [1,2,3,5,'texto']
	return render_template('idex.html',name = name, list = my_list, age=age)

@app.route('/user/otro/')
def routes():
	return 'esta es otra dirección'

if __name__== '__main__':
	app.run(debug=True, port=8000)