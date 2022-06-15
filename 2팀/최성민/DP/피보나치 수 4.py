n = int(input())

a = 0
b = 1

for _ in range(n):
	a, b = b, a+b

print(a)

# ------------------------------
# 나쁜 코드

n = int(input())
arr = [0] * (10001)
arr[0] = 0
arr[1] = 1

for i in range(2, n+1):
	if arr[i] == 0:
		arr[i] = arr[i-1] + arr[i-2]

print(arr[n])
