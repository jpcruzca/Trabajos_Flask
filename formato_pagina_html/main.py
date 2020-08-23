from flask import Flask, render_template, request
from wtforms import Form, StringField, PasswordField, BooleanField

app = Flask('__main__',template_folder='templates')

class RegistrationForm(Form):
    username = StringField('Username')
    password = PasswordField('New Password')
    opinion = BooleanField('¿Que dices?')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route1')
def route1():
    return render_template('route1.html')

@app.route('/route2')
def route2():
    return render_template('route2.html')

@app.route('/route3', methods=['GET','POST'])
def route3():
    form = RegistrationForm()
    data=''
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template('route3.html',form=form)


if __name__=='__main__':
    app.run(port=5000,debug=True)
