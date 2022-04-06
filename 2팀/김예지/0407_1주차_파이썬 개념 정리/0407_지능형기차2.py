sum = 0
best = sum

for i in range(10):
    str = input()
    sum -= int(str.split(" ")[0])
    sum += int(str.split(" ")[1])
    if sum > best:
        best = sum
        
print(best) 