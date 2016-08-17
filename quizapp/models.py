from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Quiz(models.Model):
	pub_date = models.DateTimeField('date published')
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz)
    def __str__(self):
		return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    def __str__(self):
		return self.answer_text

class QuizAttempt(models.Model):
	pub_date = models.DateTimeField(auto_now_add=True)
	quiz = models.ForeignKey(Quiz)
	def __str__(self):
		return self.quiz.name

class AnswerAttempt(models.Model):
	quiz_attempt = models.ForeignKey(QuizAttempt)
	answer = models.ForeignKey(Answer)
	question = models.ForeignKey(Question)
	def __str__(self):
		return self.answer.answer_text


