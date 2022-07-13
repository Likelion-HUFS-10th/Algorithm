# for문 -> 입력받은 수 만큼 돌기
# a, b 쌍 arr에 append -> 입력받은 수 만큼 for문
# arr[i][0] + arr[i][1] 출력

num = int(input())
arr = []

for i in range(num):
  a, b = map(int, input().split())
  arr.append([a, b])

for i in range(num):
  print(arr[i][0] + arr[i][1])