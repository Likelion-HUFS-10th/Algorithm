"""
n이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다.

	1. n에서 1을 뺀다.
	2. n을 k로 나눈다.

이 때, 2번 연산은 n이 k로 나누어떨어질 경우에만 실행가능하다.
"""

"""n, k = map(int, input().split())
cnt = 0

while n != 1:
	if n % k == 0:
		n //= k
	else:
		n -= 1
	
	cnt += 1

print(cnt)
"""

n, k = map(int, input().split())
cnt = 0

while True:
	target = (n // k) * k
	cnt += n - target
	n = target

	if n < k:
		break

	cnt += 1
	n //= k

cnt += n - 1

print(cnt)
