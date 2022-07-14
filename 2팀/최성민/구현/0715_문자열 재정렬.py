n = input()

_str = ""
_int = 0

for i in n:
	if i.isalpha():
		_str += i
	
	else:
		_int += int(i)


print("".join(sorted(_str)) + str(_int))