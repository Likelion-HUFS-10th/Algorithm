n = int(input())
total = []
for _ in range(n):
    age,name = input().split()
    age= int(age)
    total.append((age,name))

total.sort(key = lambda x : x[0])

for i in total:
    print(i[0],i[1])