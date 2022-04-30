# 문자열 -> 공백을 기준으로 단어 구분
# map 함수 -> 공백 기준으로 리스트 저장

arr = list(map(str, input().split()))

print(len(arr))