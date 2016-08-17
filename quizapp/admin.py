from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(QuizAttempt)
admin.site.register(AnswerAttempt)