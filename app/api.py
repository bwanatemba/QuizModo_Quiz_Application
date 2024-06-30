from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from .models import QuizQuestion, QuizResult
from . import db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class QuizQuestionResource(Resource):
    def get(self):
        questions = QuizQuestion.query.all()
        return jsonify([question.to_dict() for question in questions])

    def post(self):
        data = request.get_json()
        new_question = QuizQuestion(
            question=data['question'],
            option1=data['option1'],
            option2=data['option2'],
            option3=data['option3'],
            option4=data['option4'],
            correct_option=data['correct_option']
        )
        db.session.add(new_question)
        db.session.commit()
        return jsonify(new_question.to_dict())

class QuizResultResource(Resource):
    def get(self):
        results = QuizResult.query.all()
        return jsonify([result.to_dict() for result in results])

api.add_resource(QuizQuestionResource, '/questions')
api.add_resource(QuizResultResource, '/results')
