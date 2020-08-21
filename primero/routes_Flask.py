from flask import Flask 
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
	return 'Hola Mundo en español, no en ingles como los Yanquies'

@app.route('/params/<name>/<int:mio>/')
@app.route('/params/')
def paramas(name = 'Valor por default',mio = 'lagartija'): 
	return f'los parámetros son {name} y {mio}'

@app.route('/learning/<nam>/<lastname>/')
def otrasrutas(nam='Nombre',lastname='Apellido'):
	return 'hola {} {}, ¿como estas?'.format(nam, lastname)

if __name__== '__main__':
	app.run(debug=True, port=8000)