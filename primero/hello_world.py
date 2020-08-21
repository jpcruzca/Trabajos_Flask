from flask import Flask 
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
	return 'Hola Mundo en español, no en ingles como los Yanquies'

@app.route('/params')
def paramas():
	param1 = request.args.get('params1','No esta ese parametro')
	param2 = request.args.get('params2','No esta ese parametro') 
	return f'los parámetros son {param} y {param2}'

if __name__== '__main__':
	app.run(debug=True, port=8000)