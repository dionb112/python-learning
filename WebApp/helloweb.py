# My first python webserver using flask
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/displayform')
def display_form():
    return render_template('first.html')


@app.route('/processform', methods=['POST'])
def process_form():
    with open('webapp.log', 'a') as logf:
        print(request.form['thename'], file=logf)
        print(request.form['theage'], file=logf)
        print(request.form['thelocation'], file=logf)
        print('----------------------------', file=logf)
    return render_template('thanks.html',
                            the_name=request.form['thename'], 
                            the_title='Thanks!')


app.run(debug=True)
