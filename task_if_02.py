'''Написать функцию, которая принимает на вход две строки.
Если строки одинаковые, возвращает 1.
Если строки разные и первая длиннее, возвращает 2.
Если строки разные и вторая строка 'learn', возвращает 3.'''

def my_func(line1, line2):
	line1 = str(line1)
	line2 = str(line2)
	if line1 == line2:
		return 1
	elif line1 > line2:			
		return 2
    elif line2 == ('learn'):
        return 3

line1 = ('python')
line2 = ('learn')
result = print(my_func(line1, line2))
