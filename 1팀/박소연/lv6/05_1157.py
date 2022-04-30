# 가장 많이 사용된 알파벳 출력 -> 대소문자 구분X
# 1) 대문자로 변환
# 2) 들어간 알파벳 리스트 -> 중복제거
# 3) 카운트 리스트
# 4) for elem in 알파벳 리스트 -> count(elem) -> 카운트 리스트에 append
# 5) 카운트 리스트 max 구하기  -> 같은 값 있으면 ? 출력
# 6) 카운트가 max인 알파벳 출력

word = input().upper()
alphabet = list(set(word)) # 집합으로 형변환 -> 중복제거
cnt_arr = []
# alphabet = ["M", "I", "S", "P"]
# alphabet = ["Z", "A"]

for elem in alphabet:
  cnt = word.count(elem)
  cnt_arr.append(cnt)
# cnt_arr = [1, 4, 4, 1]
# cnt_arr = [2, 1]

if cnt_arr.count(max(cnt_arr)) > 1: # 최대값이 1보다 크면 = 가장 많이 사용된 알파벳이 여러개 존재
  print("?")
else:
  print(alphabet[cnt_arr.index(max(cnt_arr))])
# max(cnt_arr) = 2 -> cnt_arr.index(2) = 0 -> alphabet[0] = "Z"