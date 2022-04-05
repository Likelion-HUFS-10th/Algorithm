n = int(input())

for i in range(n):
	b = format(int(input()), 'b')

	for index, j in enumerate(b[::-1]):
		if int(j):
			print(index, end=" ")
	
	print()
