# 내꺼 - 영단어 입력 받아 자음과 모음 구별하기 using 리스트 컴프리핸션

def selector(word):
  if word in ["a", "e", "i", "o", "u"]: return word + ": 모음"
  else: return word + ": 자음"

input_word = input()
result = [selector(n) for n in input_word]
print(result)

######################################################################
# 영준님 - 딕셔너리 key값 출력, value값 출력

animal = {"닭":"병아리", "개":"강아지", "곰":"능소니", "고등어":"고도리", "명태":"노가리", "말":"망아지", "호랑이":"개호주"}
parent = [x for x in animal.keys()]

while True:
  input_parent = input(f"{parent} 중 새끼 이름을 알고싶은 동물은? ")
  if input_parent == "끝": break
  elif input_parent in parent: 
    baby = animal[input_parent]
    print(f"<{input_parent}>의 새끼는 <{baby}>입니다.")
    continue
  else:
    print("그런 동물이 없습니다. 확인해 보세요")
    continue

######################################################################
# 호연님 - O(2^n), O(n^2) 수행시간 비교 -> import time
# 질문 : for문 반복 횟수가 작아서 똑같나?

import time

start = time.time()
for n in range(1, 20):
  2**n 
end = time.time()
print("O(2^n): ", end - start)

start = time.time()
for n in range(1, 20):
  n**2 
end = time.time()
print("O(n^2): ", end - start)

######################################################################
# 수윤님 - 반복문, 리스트 원소 값의 합

arr = [1]

while True:
  num = int(input("아샷추를 일주일 중 몇 번 드시겠습니까?"))
  if num < 0 or num > 8:
    print("그렇게는 못 먹어요")
    continue
  else:
    break

for i in range(num):
  input_cnt = int(input("먹을 아샷추의 개수를 입력하세요: "))
  arr.append(input_cnt)

arr_sum = sum(arr)
print("리스트에 입력받은 숫자의 합: ", arr_sum)
if arr_sum > 10:
  print("우웩 배가 아파요")
else:
  print("내일 또 먹어야지")

arr.append("배부르다")
print(arr)