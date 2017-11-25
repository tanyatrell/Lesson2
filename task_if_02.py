def my_func(line1, line2):
	line1 = str(line1)
	line2 = str(line2)
	if line1 == line2:
		return 1
	elif line1 > line2:
			if line2 == ('learn'):
				return 3			
			return 2

line1 = ('python')
line2 = ('learn')
result = print(my_func(line1, line2))
