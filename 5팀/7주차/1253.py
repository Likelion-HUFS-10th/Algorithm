n = int(input())
a = list(map(int, input().split()))
result = []
one = 0
two = 1
target = 0

while one < n - 1:
    print(result)
    if (target == one or target == two) and two == n - 1 and target == two:
            one += 1
            two = one + 1
            target = 0
            if one == n - 1:
                break

    if target == one or target == two:
        target += 1
        continue

    if a[one] + a[two] == a[target]:
        result.append(target)
        target += 1
        if target == n:
            two += 1
            target = 0
            if two == n:
                one += 1
                two = one + 1
    else:
        target += 1
        if target == n:
            two += 1
            target = 0

print(len(set(result)))