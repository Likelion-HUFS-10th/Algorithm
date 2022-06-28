n = int(input())
list = [0, 1]

if n == 0:
    print(list[0])
elif n == 1:
    print(list[1])
else:
    for i in range(n-1):
        list.append(list[i] + list[i+1])
print(list[n])