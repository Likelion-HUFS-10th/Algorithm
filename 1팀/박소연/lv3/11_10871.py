# n, x 입력
# 정수 n개 입력 -> x보다 작은 수 입력받은 순서대로 출력
# 작은 수 넣을 배열 arr

arr = []
n, x = map(int, input().split())
a = list(map(int, input().split()))

for elem in a:
  if elem < x:
    arr.append(elem)

for elem in arr:
  print(elem, end=" ")