from flask import Flask, request, render_template
from wtforms import Form, StringField, PasswordField, BooleanField


app = Flask( __name__, template_folder='template')

class RegistrationForm(Form):
    username = StringField('username')
    password = PasswordField('New Password')


@app.route('/register', methods=['GET','POST'])
def index():
    form = RegistrationForm()
    met = request.method
    print(request.method)
    if request.method == 'POST':
        data = request.form
        print(data)
        return render_template('register.html', form=form, data = data )
    return render_template('default.html',met=met)

"""
@app.route('/a', methods=['GET','POST'])
def login():
    logform = LoginForm()
    if request.method == 'POST':
        data = request.form
        print(data)
        return render_template('login.html', logform=logform )

"""

if __name__== '__main__':
	app.run(debug=True, port=8000)