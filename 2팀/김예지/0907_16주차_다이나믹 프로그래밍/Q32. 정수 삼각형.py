# 아래 수 기준으로 대각선 왼쪽 위에서 오는 경우, 대각선 오른쪽 위에서 오는 경우

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

for j in range(1, n):
    for i in range(0, len(array[j])):
        if i == 0:
            left_up = 0
        else:
            left_up = array[j-1][i-1]
        if i == len(array[j]) - 1:
            right_up = 0
        else:
            right_up = array[j-1][i]
        array[j][i] = array[j][i] + max(left_up, right_up)

print(max(array[n-1]))


