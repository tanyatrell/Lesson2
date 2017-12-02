'''Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] 
пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". 
Подсказка: используйте метод list.pop()
Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
'''

names_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] 

from copy import copy
names_copy = copy(names_list)

while names_copy:
    current_name = names_copy.pop()
    if current_name == 'Валера':
        print('Валера нашелся')
        break

names_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] 
from copy import copy
names_copy = copy(names_list)   

def find_name(name):
    while names_copy:
        current_name = names_copy.pop()
        if current_name == name:
            print('{} нашелся'.format(name))
            break


result = find_name('Саша')
print(names_copy)
