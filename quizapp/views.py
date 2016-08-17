from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import *

NUM_QUESTIONS = 12

def index(request):

	my_quiz = get_object_or_404(Quiz, name="Ultimate Quiz")

	questions = get_list_or_404(Question, quiz=my_quiz)

	answers = {}
	
	for each in questions:
		answer = get_list_or_404(Answer, question=each)
		answers[each] = answer 

	if request.method == 'POST':

		score = 0

		quizAttempt = QuizAttempt.objects.create(quiz=my_quiz)

		for question in questions:

			answers2 = get_list_or_404(Answer, question=question)

			for answer in answers2:
				
				if request.POST["question"+str(question.id)] == answer.answer_text:

					answerAttempt = AnswerAttempt.objects.create(quiz_attempt=quizAttempt, answer=answer, question=question)

					if answer.correct:
						score += 1



		post = True
		return render(request, 'quizapp/index.html', {'answers':answers, 'score':score, "num_questions": NUM_QUESTIONS, "post":post})

	else:
		post = False
		return render(request, 'quizapp/index.html', {'answers':answers, "num_questions": NUM_QUESTIONS, "post":post})