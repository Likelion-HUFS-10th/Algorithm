first_in = tuple(map(int, input().split()))[-1]
max_p, total_p = first_in

for _ in range(9):
	next_out, next_in = tuple(map(int, input().split()))
	total_p = total_p - next_out + next_in

	if total_p > max_p:
		max_p = total_p

print(max_p)
