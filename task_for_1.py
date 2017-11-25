'''Создать список с оценками учеников разных классов 
школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.'''

all_scores = [
{'school_class': '4a', 
'scores': [3,4,4,5,2]}, 
{'school_class': '4б', 
'scores': [5,5,4,5,3]},
{'school_class': '4в', 
'scores': [3,5,2,4,4]}]

result_school =0 
result_class = 0

def avr_list(a_list):
    a_sum = 0
    for l in a_list:
        a_sum = a_sum + l
    return a_sum/len(a_list)

for each in all_scores:
    result = avr_list(each.get('scores'))
    result_class = result_class + result
    print('Средняя по классу {}: {}'.format(each.get('school_class'),result))

result_school = result_class/3
print('Средняя по школе: {}'.format(result_school))

