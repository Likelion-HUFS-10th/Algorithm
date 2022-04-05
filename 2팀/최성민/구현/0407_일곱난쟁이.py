height = [int(input()) for _ in range(9)]
wrong = []

for i in range(len(height)):
	wrong.append(height[i])
	for j in range(i+1, len(height)):
		wrong.append(height[j])
		
		if sum(height) - sum(wrong) == 100:
			break
		
		wrong.pop()
	if len(wrong) == 2:
		break

	else:	wrong.pop()

for i in wrong:
	height.remove(i)

height.sort()

for i in height:
	print(i)










# def minus(idx, cnt):
# 	print(height)
# 	if sum(height) == 100:
# 		if cnt == 7:
# 			return height
	
# 	if idx > 8:
# 		return
	
# 	height.append(wrong[idx])
# 	minus(idx+1, cnt+1)
# 	height.pop()

# 	minus(idx+1, cnt)

# answer = minus(0, 0)


# [23, 19, 10, 15, 25, 8, 13]