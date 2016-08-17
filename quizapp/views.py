from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import *

NUM_QUESTIONS = 12

def index(request):

	# get the quiz in order to grab questions, answers, and create quiz attempt
	my_quiz = get_object_or_404(Quiz, name="Ultimate Quiz")

	# get the questions
	questions = get_list_or_404(Question, quiz=my_quiz)

	answers = {}
	
	# make a dictionary with keys as questions and values as a list of answers
	for each in questions:
		answer = get_list_or_404(Answer, question=each)
		answers[each] = answer 

	if request.method == 'POST':

		score = 0

		# POST is a submit, so create a quiz attempt
		quizAttempt = QuizAttempt.objects.create(quiz=my_quiz)

		for question in questions:

			answers2 = get_list_or_404(Answer, question=question)

			for answer in answers2:

				# if the answer is chosen, add it as an answer attempt on current quiz attempt. If its the correct answer, add to score
				if request.POST["question"+str(question.id)] == answer.answer_text:

					answerAttempt = AnswerAttempt.objects.create(quiz_attempt=quizAttempt, answer=answer, question=question)

					if answer.correct:
						score += 1


		# render the page, post boolean will tell us to show the score and retry button
		post = True
		return render(request, 'quizapp/index.html', {'answers':answers, 'score':score, "num_questions": NUM_QUESTIONS, "post":post})

	else:
		# render page normally (not a POST request)
		post = False
		return render(request, 'quizapp/index.html', {'answers':answers, "num_questions": NUM_QUESTIONS, "post":post})