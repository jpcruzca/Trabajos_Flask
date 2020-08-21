"""
Esta aplicacion dice Hola mundoS

instalar otro editor de texto más veloz para este tipo de desarrollos
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	 return 'esta es otra cadena de texto'
   

if __name__=='__main__':
    app.run()