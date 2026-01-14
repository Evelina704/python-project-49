import random


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    else:
        result = a * b

    question = f'{a} {operation} {b}'
    return question, str(result)


GAME_DATA = {
    'description': DESCRIPTION,
    'get_question_and_answer': get_question_and_answer,
}
