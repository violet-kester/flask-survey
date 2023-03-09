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

    return render_template('question.html', question=survey.questions[q_num])

# @app.post('/answer')