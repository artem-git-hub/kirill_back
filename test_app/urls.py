from django.urls import path
from .views import SubjectListView, TestListView, QuestionListView, UserAnswerView

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('tests/<str:subject_code>/', TestListView.as_view(), name='test-list'),
    path('questions/<str:subject_code>/<str:test_code>/', QuestionListView.as_view(), name='question-list'),
    path('answers/<str:subject_code>/<str:test_code>/', UserAnswerView.as_view(), name='user-answer'),
]
