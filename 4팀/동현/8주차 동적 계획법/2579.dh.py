"""
맞는지 모르겠지만 수학적 귀납법 같이 해결..??
1부터 가정하며 n일 때를 찾아주는 방법
마지막 계단은 무조건 밟아야 함
마지막 계단 입장 -> 전전 계단 + 본인 or 전 계단 + 본인
"""
n = int(input())

stairs_score = []

for i in range(n):
    stairs_score.append(int(input()))

arr = [0] * (n+1)

if n == 1:
    print(stairs_score[0])
elif n == 2:
    print(stairs_score[0]+stairs_score[1])
elif n == 3:
    print(max(stairs_score[0]+stairs_score[2], stairs_score[1]+stairs_score[2]))
# elif n == 4:
#   print(max(stairs_score[1]+stairs_score[3], stairs_score[2]+stairs_score[3]))
else:
    arr[0] = stairs_score[0]
    arr[1] = stairs_score[0] + stairs_score[1]
    for i in range(2,n):
        arr[i] = max(arr[i-3] + stairs_score[i-1] + stairs_score[i], arr[i-2] + stairs_score[i])
    print(arr[n-1])