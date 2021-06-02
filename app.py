from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators
from conversor import Conversor

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
            conv = Conversor()
            mensagem = conv.converter(area)
            print("Área: {}", mensagem)
    
        if form.validate():
            flash('Medida informada: ' + area)
            flash(mensagem)
        else:
            flash('Atenção: informe um valor para ser convertido.')
    
        return render_template('conversor.html', form=form)

if __name__ == "__main__":
    app.run()
