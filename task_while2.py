'''Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”'''

def ask_user():
    while True:
        answer = input('Как дела? ')
        if answer == 'Хорошо':
            break


result = ask_user()

def get_answer():
    while True:
        answer = input('Как дела? ')
        if answer == 'Хорошо':
            break