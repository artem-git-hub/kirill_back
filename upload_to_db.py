import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kirill_back.settings')
django.setup()

from test_app.models import Subject, Test, Question

def add_subjects():
    subjects_data = [
        {"name": "История", "code": "istoria"},
        {"name": "Русский", "code": "russkii"},
    ]

    for subject_data in subjects_data:
        Subject.objects.create(**subject_data)

def add_tests():
    subject_russkii = Subject.objects.get(code="russkii")

    tests_data = [
        {"name": "Тест по грамматике", "code": "test_po_grammatike", "subject": subject_russkii},
        {"name": "Тест по пунктуации", "code": "test_po_punktuacii", "subject": subject_russkii},
    ]

    for test_data in tests_data:
        Test.objects.create(**test_data)

def add_questions():
    test_po_punktuacii = Test.objects.get(code="test_po_punktuacii")

    questions_data = [
        {"question_text": "Сколько точек в предложении 'Дылдвы ываы ыв ываф фаф вфв ыв.'", "answer": "3", "test": test_po_punktuacii},
        {"question_text": "Сколько запятых в предложении 'Дылдвы ываы, ыв ываф фаф вфв ыв.'", "answer": "91", "test": test_po_punktuacii},
    ]

    for question_data in questions_data:
        Question.objects.create(**question_data)

if __name__ == "__main__":
    add_subjects()
    add_tests()
    add_questions()

    print("Data populated successfully!")
