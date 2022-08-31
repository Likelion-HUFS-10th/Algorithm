# 강의 n개, 블루레이 m개(크기 최소화)
# start와 end점 잡기
#  블루레이 1개일 때 -> 전체합 -> sum(블루레이)
#  블루레이 n개 일 때 -> 한 개의 합 -> n-1
# 블루레이 크기 모두 같아야함 -> 기준이 되는 블루레이는 강의합들보다 작게 되면 x
# 예시 전체합 45, 한 개 최대합 9 -> 블루레이 3으로 나눈 값 기준 잡기 -> 15 15 15
#  12345/67/8/9 4개로 나뉨
#  16으로 했을 때 -> 똑같음 -> 17로 하면 12345/67/89 나뉨


n, m = map(int, input().split())
lec = list(map(int, input().split()))

start = 0
end = sum(lec)
result = 0

while start <= end:
    blue_num = 1
    lec_sum = 0
    mid = (start+end) // 2
    for i in range(n):
        if lec_sum + lec[i] <= mid:
            lec_sum += lec[i]

        else:
            blue_num += 1
            lec_sum = 0
            lec_sum += lec[i]

    if blue_num <= m:
        end = mid - 1
        result = mid

    else:
        start = mid + 1

print(result)
