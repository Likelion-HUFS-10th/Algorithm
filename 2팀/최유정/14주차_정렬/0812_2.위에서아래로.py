n = int(input())
numlist = []
for _ in range(n):
    numlist.append(int(input()))

numlist.sort(reverse=True)
print(*numlist)