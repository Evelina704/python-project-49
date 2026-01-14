from brain_games.cli import welcome_user


ROUNDS_COUNT = 3


def run(game):
    name = welcome_user()
    print(game['description'])

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game['get_question_and_answer']()
        print(f'Question: {question}')
        answer = input('Your answer: ').strip()

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
