def even_numbers(low, high):
	num = []
	for i in range(low, high):
		if i % 2 == 0:
			print i
			num.append(i)
print even_numbers(2, 50)