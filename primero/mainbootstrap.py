from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('templatebootstraps.html')

@app.route('/inicio/')
def inicio():
    return render_template('tem_sin_bootstrap.html')

if __name__=='__main__':
    app.run(debug=True, port=10000)