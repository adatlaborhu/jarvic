from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import random
from jarvic import answering
from jarvic import mlwords
from jarvic import save_next_question

app = Flask(__name__)

question = {}
next_question = {}
answer = ""

@app.route('/start/')
def my_form_name():
    id = "/conv/" + str(random.randrange(1,100000000000000))
    return redirect(id, code=302)

@app.route('/conv/<convnumb>')
def my_form(convnumb):
    question[convnumb] = ""
    next_question[convnumb] = ""
    return render_template("jarvic.html", convnumb=convnumb)

@app.route('/conv/<convnumb>', methods=['POST'])
def my_form_post(convnumb):
    global answer

    if next_question[convnumb]:
	prev_answer = answer
	question[convnumb] = next_question[convnumb]
	next_question[convnumb] = request.form['next_question2']
	mlwords(prev_answer,next_question[convnumb])
	save_next_question(next_question[convnumb])
	answer = answering(next_question[convnumb])
	return render_template("jarvic.html", question=question[convnumb], next_question=next_question[convnumb], answer=answer, prev_answer=prev_answer, convnumb = convnumb)

    elif question[convnumb]:
	prev_answer = answer
	next_question[convnumb] = request.form['next_question']
	mlwords(prev_answer,next_question[convnumb])
	save_next_question(next_question[convnumb])
	answer = answering(next_question[convnumb])
	return render_template("jarvic.html", question=question[convnumb], next_question=next_question[convnumb], answer=answer, prev_answer=prev_answer, convnumb = convnumb)

    else:
	question[convnumb] = request.form['question']
	answer = answering(question[convnumb])
	return render_template("jarvic.html", question=question[convnumb], answer=answer, convnumb = convnumb)

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')