from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_questions():
    return render_template('home.html', questions=story.prompts)

@app.route('/story')
def show_story():
    answers = request.args
    text = story.generate(answers)
    return render_template('story.html', story=text)