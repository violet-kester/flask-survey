from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES = []

@app.get('/')
def get_start():
    """ loads homepage with name of survey and start btn """

    return render_template("survey_start.html", survey_title=survey.title,
                           survey_instructions=survey.instructions)


@app.post('/begin')
def get_first_question():
    """ on start btn click, redirect to first question """

    return redirect('/questions/0')


@app.get('/questions/<int:q_num>')
def get_question(q_num):
    """ shows question form """

    return render_template('question.html', question=survey.questions[q_num], q_num=q_num)


@app.post('/answer')
def display_next_question():
    """ redirects to next question or thank you pg. """

    RESPONSES.append(request.form['answer'])
    q_num = int(request.form['q_num'])

    # redirects to thank you pg. after last question
    if q_num >= len(survey.questions) - 1:
        return redirect("/completion")

    # go to next question
    next_q_num = q_num + 1
    next_q_url = f'/questions/{next_q_num}'

    return redirect(next_q_url)


@app.get('/completion')
def get_thank_you():
    """ loads thank you page with q's and a's """

    survey_length = len(survey.questions)

    return render_template('completion.html', survey=survey, survey_length=survey_length, responses=RESPONSES)