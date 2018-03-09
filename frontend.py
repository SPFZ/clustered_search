import requests
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

class SearchForm(FlaskForm):
    search = StringField('Search for:', validators=[DataRequired()])
    submit = SubmitField('Run')

@app.route("/", methods=('GET', 'POST'))
def search():
    form = SearchForm()
    if form.validate_on_submit():
        payload = {'search_string': request.form['search']}
        response = requests.get('http://localhost:5001/search', 
                                params=payload).json()
        print(response)
        return render_template('frontend.html.tpl', 
                            search=response['search_string'],
                            results=response['results'],
                            form=form)
    else:
        return render_template('frontend.html.tpl', form=form)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)