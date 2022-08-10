n = int(input())
state = list(map(int, input().split()))
money = int(input())

left = 0
right = max(state)

while right >= left:
    mid = (left + right) // 2
    answer = 0
    for budget in state:
        if budget > mid:
            answer += mid
        else:
            answer += budget

    if answer > money:
        right = mid - 1
    else:
        left = mid + 1 
    print(left, right, answer)
print(right)
