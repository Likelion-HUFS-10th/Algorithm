# n = int(input())

# coins = 0

# a = n // 5
# res = n

# if n == 1 or n == 3:
# 	print(-1)

# elif n % 5 == 0:
# 	print(n // 5)

# else:
# 	while res != 0:
# 		res = n - (5 * a)

# 		if res % 2 == 0:
# 			coins += a
# 			coins += (res // 2)
# 			print(coins)
# 			break
		
# 		else:
# 			a -= 1


# ---------------------------------

n = int(input())

def f(n):
	five = n // 5
	remain = n % 5

	while five >= 0:
		if remain % 2 == 0:
			return five + (remain // 2)
		
		five -= 1
		remain += 5
	
	return -1

print(f(n))