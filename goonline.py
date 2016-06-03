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
prev_question = {}
prev2_question = {}
prev3_question = {}
prev4_question = {}
answer = ""
prev_answer = ""
prev2_answer = ""
prev3_answer = ""
prev4_answer = ""

@app.route('/start/')
def my_form_name():
    id = "/conv/" + str(random.randrange(1,100000000000000))
    return redirect(id, code=302)

@app.route('/conv/<convnumb>')
def my_form(convnumb):
    question[convnumb] = ""
    prev_question[convnumb] = ""
    prev2_question[convnumb] = ""
    prev3_question[convnumb] = ""
    prev4_question[convnumb] = ""

    return render_template("jarvic.html", convnumb=convnumb)

@app.route('/conv/<convnumb>', methods=['POST'])
def my_form_post(convnumb):
    global answer
    global prev_answer
    global prev2_answer
    global prev3_answer
    global prev4_answer

    if prev3_question[convnumb]:
	prev4_answer = prev3_answer
	prev3_answer = prev2_answer
	prev2_answer = prev_answer
	prev_answer = answer
	prev4_question[convnumb] = prev3_question[convnumb]
	prev3_question[convnumb] = prev2_question[convnumb]
	prev2_question[convnumb] = prev_question[convnumb]
	prev_question[convnumb] = question[convnumb]
	question[convnumb] = request.form['question']
	mlwords(prev_answer,question[convnumb])
	save_next_question(question[convnumb])
	answer = answering(question[convnumb])
	return render_template("jarvic.html",
				question=question[convnumb], 
				prev_question=prev_question[convnumb],
				prev2_question=prev2_question[convnumb], 
				prev3_question=prev3_question[convnumb], 
				prev4_question=prev4_question[convnumb], 
				answer=answer, prev_answer=prev_answer, 
				prev2_answer=prev2_answer, 
				prev3_answer=prev3_answer, 
				prev4_answer=prev4_answer, 
				convnumb = convnumb)


    elif prev2_question[convnumb]:
	prev3_answer = prev2_answer
	prev2_answer = prev_answer
	prev_answer = answer
	prev3_question[convnumb] = prev2_question[convnumb]
	prev2_question[convnumb] = prev_question[convnumb]
	prev_question[convnumb] = question[convnumb]
	question[convnumb] = request.form['question']
	mlwords(prev_answer,question[convnumb])
	save_next_question(question[convnumb])
	answer = answering(question[convnumb])
	return render_template("jarvic.html",
				question=question[convnumb], 
				prev_question=prev_question[convnumb],
				prev2_question=prev2_question[convnumb], 
				prev3_question=prev3_question[convnumb], 
				answer=answer, prev_answer=prev_answer, 
				prev2_answer=prev2_answer, 
				prev3_answer=prev3_answer, 
				convnumb = convnumb)

    elif prev_question[convnumb]:
	prev2_answer = prev_answer
	prev_answer = answer
	prev2_question[convnumb] = prev_question[convnumb]
	prev_question[convnumb] = question[convnumb]
	question[convnumb] = request.form['question']
	mlwords(prev_answer,question[convnumb])
	save_next_question(question[convnumb])
	answer = answering(question[convnumb])
	return render_template("jarvic.html",
				question=question[convnumb],
				prev_question=prev_question[convnumb],
				prev2_question=prev2_question[convnumb],
				answer=answer,
				prev_answer=prev_answer,
				prev2_answer=prev2_answer,
				convnumb = convnumb)

    elif question[convnumb]:
	prev_answer = answer
	prev_question[convnumb] = question[convnumb]
	question[convnumb] = request.form['question']
	mlwords(prev_answer,question[convnumb])
	save_next_question(question[convnumb])
	answer = answering(question[convnumb])
	return render_template("jarvic.html", question=question[convnumb], prev_question=prev_question[convnumb], answer=answer, prev_answer=prev_answer, convnumb = convnumb)

    else:
	question[convnumb] = request.form['question']
	answer = answering(question[convnumb])
	return render_template("jarvic.html", question=question[convnumb], answer=answer, convnumb = convnumb)

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')