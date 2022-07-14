n = input()

m = len(n) // 2

if sum(map(int, n[:m])) == sum(map(int, n[m::])):
	print("LUCKY")
else:
	print("READY")