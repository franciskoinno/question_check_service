import requests
import datetime
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('question.html')

@app.route('/', methods=['POST'])
def my_form_post():
    if request.form['submit_button'] != 'submit':
        question = request.form['question']
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        data = {'question': question, 'A': a, 'B': b, 'C': c, 'D': d}
        if len(question) < 1 or len(a) < 1 or len(b) <1 or len(c) < 1 or len(d) < 1:
            return render_template('question.html',service_on="Please complete the form")
        try:	
            r = requests.post('http://web2:5000/check', json=data)
            return render_template('question.html', predict_content=r.text,service_on="Checking system response:")
        except:
            return render_template('question.html',service_on="Cannot connect to checking service!!!!!!!!!!")
    else:
        return "Question created!!!!"
app.run(host='0.0.0.0', debug=True)
