from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from .models import QuizQuestion
from . import db

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@login_required
def admin_panel():
    return render_template('admin.html')

@admin.route('/add_question', methods=['GET', 'POST'])
@login_required
def add_question():
    if request.method == 'POST':
        question = request.form.get('question')
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')
        option4 = request.form.get('option4')
        correct_option = request.form.get('correct_option')
        new_question = QuizQuestion(question=question, option1=option1, option2=option2, option3=option3, option4=option4, correct_option=correct_option)
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('admin.admin_panel'))
    return render_template('add_question.html')
