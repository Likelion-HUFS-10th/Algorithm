# 알파벳 리스트 -> list(range(97, 123)) -> 아스키 코드 a:97, z:122
# find() 함수
# 1) 어떤 찾는 문자가 문자열 안에서 첫번째에 위치한 순서 숫자로 출력
# 2) 없는 경우 -1 출력

s = input()
alphabet = list(range(97, 123))

for elem in alphabet:
  print(s.find(chr(elem)))