n = int(input())

num_second = [0 for _ in range(n)]
result = 0

first = [
    input()
    for _ in range(n)
]

second = [
    input()
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if second[i] == first[j]:
            num_second[i] = j + 1
            
for i in range(n):
    for j in range(i + 1, n):
            if num_second[i] > num_second[j]:
                result += 1
                break
print(result)
