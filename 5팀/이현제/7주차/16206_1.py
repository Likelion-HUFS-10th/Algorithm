n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort(key=lambda x: (x % 10, x))
result = 0

def ten(target):
    target_str = str(target)
    target_ten = int(target_str[-2])
    return target_ten

for i in range(n):
    target = arr[i]

    if m == 0 and target % 10 != 0:
        break
    if target < 10:
        continue
    ten_number = ten(target)
    
    if m - ten_number >= 0:
        if target - (ten_number * 10) == 0:
            m -= ten_number - 1
            result += ten_number
        else:
            m -= ten_number
            result += ten_number

    else:
        if target - (ten_number * 10) == 0 and ten_number == m + 1:
            m -= ten_number -1
            result += ten_number
        else:
            result += m
            m = 0

print(result)