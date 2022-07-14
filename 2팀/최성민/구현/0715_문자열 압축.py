s = "a"

n = len(s) // 2
result = 1e9

if len(s) == 1:
	result = 1

for i in range(1, n+1):
	temp = ""
	cnt = 1

	for j in range(0, len(s), i):
		if s[j:j+i] == s[j+i:j+2*i]:
			cnt += 1
			continue

		else:
			temp += str(cnt) + s[j:j+i] if cnt >= 2 else s[j:j+i]
			cnt = 1
	
	result = min(result, len(temp))


print(result)