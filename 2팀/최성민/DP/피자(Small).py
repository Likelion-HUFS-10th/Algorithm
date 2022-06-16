n = int(input())

a, b = 1, 0

for i in range(2, n+1):
	b = a + b
	a = i

print(b)