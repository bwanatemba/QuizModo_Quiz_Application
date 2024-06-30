

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .models import QuizQuestion, QuizResult
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/quiz')
@login_required
def quiz():
    questions = QuizQuestion.query.all()
    return render_template('quiz.html', questions=questions)

@main.route('/submit_quiz', methods=['POST'])
@login_required
def submit_quiz():
    score = 0
    questions = QuizQuestion.query.all()
    for question in questions:
        selected_option = request.form.get(str(question.id))
        if selected_option == question.correct_option:
            score += 1
    result = QuizResult(user_id=current_user.id, score=score)
    db.session.add(result)
    db.session.commit()
    return redirect(url_for('main.result'))

@main.route('/result')
@login_required
def result():
    result = QuizResult.query.filter_by(user_id=current_user.id).order_by(QuizResult.timestamp.desc()).first()
    return render_template('result.html', result=result)
