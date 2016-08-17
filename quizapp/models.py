from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Main Quiz has date to define it and a name
class Quiz(models.Model):
	pub_date = models.DateTimeField('date published')
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

# a question belongs to a quiz and has text that is the question itself
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz)
    def __str__(self):
		return self.question_text

# answers are attached to questions, and can be the correct answer
class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    def __str__(self):
		return self.answer_text

# An attempt at the quiz. Each time the quiz is completed a new attempt is logged
class QuizAttempt(models.Model):
	pub_date = models.DateTimeField(auto_now_add=True)
	quiz = models.ForeignKey(Quiz)
	def __str__(self):
		return self.quiz.name

# these are the attempted answers, they relate to real answers and a real question, and are attached to a specific quiz attempt
class AnswerAttempt(models.Model):
	quiz_attempt = models.ForeignKey(QuizAttempt)
	answer = models.ForeignKey(Answer)
	question = models.ForeignKey(Question)
	def __str__(self):
		return self.answer.answer_text


