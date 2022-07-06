# N개의 정수 중 min, max 구하기
# 첫 줄 : 정수 개수 N / 둘째 줄 : N개의 정수
# min, max 함수 : iterable 자료형(반복 가능한 데이터 타입 -> 리스트, 튜플, 문자열 등)의 min, max 반환

num = int(input())
num_list = list(map(int, input().split()))

print(min(num_list), max(num_list))