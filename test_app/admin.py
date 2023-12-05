from django.contrib import admin
from .models import Subject, Test, Question, UserAnswer


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass