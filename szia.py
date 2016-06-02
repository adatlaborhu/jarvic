from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import random

app = Flask(__name__)

question = {}
next_question = {}

@app.route('/start/')
def my_form_name():
    id = "/conv/" + str(random.randrange(1,100000000000000))
    return redirect(id, code=302)

@app.route('/start/', methods=['POST'])
def my_form_name_start():
    yourname = request.form['yourname']
    return render_template("tellmeyourname.html")

@app.route('/conv/<test>')
def my_form(test):
    question[test] = ""
    next_question[test] = ""
    return render_template("szia.html", test=test)

@app.route('/conv/<test>', methods=['POST'])
def my_form_post(test):

    if next_question[test]:
	question[test] = next_question[test]
	next_question[test] = request.form['next_question2']
	return render_template("szia.html", question=question[test], next_question=next_question[test], answer="hello", test = test)

    elif question[test]:
	next_question[test] = request.form['next_question']
	return render_template("szia.html", question=question[test], next_question=next_question[test], answer="hello", test = test)

    else:
	question[test] = request.form['question']
	return render_template("szia.html", question=question[test], answer="hello", test = test)

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')