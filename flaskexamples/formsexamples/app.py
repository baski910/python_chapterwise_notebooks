from flask import Flask, render_template
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

# pip install flask-wtf

app = Flask(__name__)

app.config['SECRET_KEY']='LongAndRandomSecretKey'

######################################################
#class GreetUserForm(FlaskForm):
#    username = StringField(label=('Enter Your Name:'))
#    submit = SubmitField(label=('Submit'))


######################################################
class GreetUserForm(FlaskForm):
    username = StringField(label=('Enter Your Name:'), 
                                   validators=[DataRequired(), Length(min=5)])
    submit = SubmitField(label=('Submit'))




@app.route('/', methods=('GET', 'POST'))
def index():
    form = GreetUserForm()
    if form.validate_on_submit():
        return f'''<h1> Welcome {form.username.data} </h1>'''
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run()



