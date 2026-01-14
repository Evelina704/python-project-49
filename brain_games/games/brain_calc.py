import random

RULE = 'What is the result of the expression?'


def generate_round():
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
