n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))
a.append(0)
result = 0
target = 0
left = 0
right = 1
target =  a[left] + a[right]
while right <= n:
    if a[left] == m:
        result += 1
        left += 1
        right = left + 1
        if right > n:
            break   
        target = a[left] + a[right] 
    elif target < m:
        right += 1
        if right > n:
            break
        target = target + a[right]
    elif target > m:
        left += 1
        right = left + 1
        if right > n:
            break       
        target = a[left] + a[right]
    elif target == m:
        result += 1
        left += 1
        right = left + 1
        if right > n:
            break
        target = a[left] + a[right]
print(result)
