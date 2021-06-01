from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'conversor_hectare_nada_secreto'

class ReusableForm(Form):
    area = TextField('Área:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            area=request.form['area']
            print("Área: {}", area)
    
        if form.validate():
        # Save the comment here.

            flash('Medida informada: ' + area)
        else:
            flash('Error: All the form fields are required.')
    
        return render_template('conversor.html', form=form)

if __name__ == "__main__":
    app.run()
