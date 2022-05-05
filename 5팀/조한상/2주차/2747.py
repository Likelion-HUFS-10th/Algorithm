n= int(input())
i, j = 0, 1
for x in range(n):
    i ,j = j, i+j
print(i)