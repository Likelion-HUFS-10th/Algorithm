new = ""
res = ""

a = str(input())
b = str(input())

for i in range(8):
	new += a[i] + b[i]

while (len(new) != 2):
	for i in range(1, len(new)):
		res += str(int(new[i]) + int(new[i-1]))[-1]
	
	new = res
	res = ""

print('%2s' % new)
