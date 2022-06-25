import sys
from math import factorial
input = sys.stdin.readline

def solve(string, idx):
	global cnt

	if len(st) == idx:
		cnt += 1

		if cnt == n:
			return string
	
	for i in st:
		if not i in string:
			res = solve(string + i, idx+1)
			if res:
				return res
	
while True:
	try:
		st, n = input().split()
		n = int(n)

		if factorial(len(st)) < n:
			print(st, n, "=", "No permutation")
		
		else:
			cnt = 0
			print(st, n, "=", solve("", 0))

	except:
		quit()