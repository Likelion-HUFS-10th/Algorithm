start = int(input())
end = int(input())

lst = []
for num in range(start, end + 1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
                break
        if error == 0:
            lst.append(num)

if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)