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

result_school = 0 
sum_classes = 0
all_scores_sum = 0
result = 0
len_list = 0

def sum_list(a_list):
    a_sum = 0
    for l in a_list:
        a_sum = a_sum + l
    return a_sum

for m in all_scores:
    new_list = m.get('scores')
    result = sum_list(new_list)/len(new_list)
    len_list = len_list + len(new_list)
    all_scores_sum = all_scores_sum + sum_list(new_list)
    print('Средняя по классу {}: {}'.format(m.get('school_class'),result))
    


result_school = round(all_scores_sum/len_list, 1)
print('Средняя по школе: {}'.format(result_school))

