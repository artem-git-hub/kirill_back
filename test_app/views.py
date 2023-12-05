from rest_framework import generics, status
from rest_framework.response import Response
from .models import Subject, Test, Question, UserAnswer
from .serializers import SubjectSerializer, TestSerializer, QuestionSerializer, UserAnswerSerializer

class SubjectListView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TestListView(generics.ListCreateAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        subject_code = self.kwargs['subject_code']
        return Test.objects.filter(subject__code=subject_code)

class QuestionListView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        subject_code = self.kwargs['subject_code']
        test_code = self.kwargs['test_code']
        return Question.objects.filter(test__subject__code=subject_code, test__code=test_code)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        questions_data = request.data
        subject_code = self.kwargs['subject_code']
        test_code = self.kwargs['test_code']

        # Добавьте код для сохранения вопросов и ответов в базу данных
        # Пример:

        test = Test.objects.get(subject__code=subject_code, code=test_code)

        for question_data in questions_data:
            question_text = question_data['question']
            answer = question_data['answer']

            question = Question.objects.create(test=test, question_text=question_text, answer=answer)

        return Response({"status": "success"})

class UserAnswerView(generics.CreateAPIView):
    serializer_class = UserAnswerSerializer

    def create(self, request, *args, **kwargs):
        subject_code = kwargs['subject_code']
        test_code = kwargs['test_code']

        try:
            user_answers_data = request.data
            if not isinstance(user_answers_data, list):
                raise ValueError("Invalid data format. Expected a list.")

            # Перебираем ответы пользователя
            user_answers = []
            for user_answer_data in user_answers_data:
                if not isinstance(user_answer_data, dict):
                    raise ValueError("Invalid answer format. Expected a dictionary.")

                question_id = user_answer_data.get('question_id')
                answer = user_answer_data.get('answer')

                if question_id is not None and answer is not None:
                    # Получаем вопрос из БД
                    question = Question.objects.get(id=question_id)

                    # Сравниваем ответ пользователя с ответом в БД
                    is_correct = question.answer == answer

                    # Сохраняем ответ пользователя в БД
                    UserAnswer.objects.create(
                        question=question,
                        user_answer=answer
                    )

                    user_answers.append({
                        'question_id': question_id,
                        'its_true': is_correct
                    })

            return Response(user_answers, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

