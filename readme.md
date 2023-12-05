# Documentation for kirill_back

## Overview

**This Django application provides an API for managing subjects, tests, questions, and user answers. It is designed to support educational testing scenarios.**

## Requirements and starting

Установить:  
- docker
- docker-compose

Запуск:
1) Клонировать репозиторий и войти в директорию
2) Выполнить команду: `sudo docker-compose up --build`  
  
p.s.: Запуститься в этом окне терминала, будет работать до закрытия этого окна  

## Endpoints
### 1. Subjects

GET `/subjects/`  
Retrieve a list of subjects.  

- Example Response:  

```json
[
	{
		"name": "History",
		"code": "history"
	},
	{
		"name": "Russian",
		"code": "russian"
	}
]
```

POST `/subjects/`  
Create a new subject.  

- Example Request:  

```json
{	
	"name": "Предмет",
	"code": "sub"
}
```

### 2. Tests

GET `/tests/<subject_code: str>/`  
Retrieve a list of tests for a specific subject.  

- Example Response:  

```json
[
	{
		"name": "Важный тест",
		"code": "very_test"
	},
	{
		"name": "ЫВДЛАОЫЛДВАО",
		"code": "asdfjasdf"
	}
]
```


POST `/tests/<subject_code: str>/`   
Create a new test for a specific subject.  

- Example Request:  

```json
{	
	"name": "ТЕСТ",
	"code": "TEST"
}

```


### 3. Questions

GET `/test/<subject_code: str>/<test_code: str>/`  
Retrieve a list of questions for a specific test.  

- Example Response:  

```json
[
	{
		"question_id": 1,
		"question": "да?",
		"answer": "да"
	},
	{
		"question_id": 2,
		"question": "кккккккккккккккккк",
		"answer": "нет"
	}
]
```

POST `/test/<subject_code: str>/<test_code: str>/`  
Add new questions to a specific test.  

- Example Request:  

```json
[
	{
		"question": "да?",
		"answer": "да"
	},
	{
		"question": "кккккккккккккккккк",
		"answer": "нет"
	}
]
```


### 4. User Answers
POST `/answers/<subject_code: str>/<test_code: str>/`  
Submit user answers for a specific test.  

- Example Request:  

```json
[
	{
		"question_id": 1,
		"answer": "ага"
	},
	{
		"question_id": 2,
		"answer": "неа"
	}
]
```

- Example Response:

```json
[
	{
		"question_id": 1,
		"its_true": true
	},
	{
		"question_id": 2,
		"its_true": false
	}
]
```

## Ссылки по которым ты уже можешь посмотреть что-нибудь:

GET: http://127.0.0.1:8000/test_app/subjects/  

POST: http://127.0.0.1:8000/test_app/subjects/  
body:
```json
{
  "name": "Название предмета",
  "code": "asadasdas"
}
```

GET: http://127.0.0.1:8000/test_app/tests/russkii/  

POST: http://127.0.0.1:8000/test_app/subjects/  
body:
```json
{
    "name": "какой-то тест",
    "code": "test_code"
}
```

GET: http://127.0.0.1:8000/test_app/questions/russkii/test_po_punktuacii/  

POST: http://127.0.0.1:8000/test_app/questions/russkii/test_po_punktuacii/  
body:
```json
[
	{
		"question": "вопрос?",
		"answer": "да"
	},
	{
		"question": "не вопрос",
		"answer": "да"
	}
]
```

POST: http://127.0.0.1:8000/test_app/answers/russkii/test_po_punktuacii/  
body:
```json
[
	{
		"question_id": 1,
		"answer": "31"
	},
	{
		"question_id": 2,
		"answer": "91"
	}
][
	{
		"question": "вопрос?",
		"answer": "да"
	},
	{
		"question": "не вопрос",
		"answer": "да"
	}
]
```

## Админка:  
Логин: `superman`  
   
Пароль: `123`  