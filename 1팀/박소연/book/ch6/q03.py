# 로그 재정렬
# 1. 가장 앞부분은 식별자
# 2. 문자가 숫자보다 앞에
# 3. 문자가 동일할 경우 식별자 순으로, 식별자는 순서에 영향X
# 4. 숫자 로그는 입력 순으로
# 1차 정렬: 숫자, 문자 구별 -> 숫자는 뒤로 붙이기
# 2차 정렬: 문자열 정렬 -> 리스트 요소를 쪼개서 두번째 인덱스 기준으로 정렬해야함 -> lambda

# 1. sort& sorted 차이
# sort : 리스트 자체를 정렬 -> 리스트 값이 바뀜, 반환값은 None -> alist = a.sort() XXXXX
# sorted : 새로운 정렬된 리스트 반환 -> 리스트 자체 값이 바뀌는건X, 반환값은 새로 정렬된 리스트

# 2. lambda 표현식 : 간단한 함수를 쉽게 선언하는 방법
# lambda 매개변수들 : 식 ex) lambda x: x+10
# 람다는 이름이 없어서 할당해준 후에 호출 ex) plus_ten = lambda x: x+10 -> plus_ten(1)
# (lambda x:x+10)(1) <- 이런식으로도 호출 가능하긴 함
# ** 표현식 안에 새 변수 만들 수 없음! -> 외부에서 선언한 변수를 사용하는 건 ok

def reorderLogFiles():
  text, number = [], []
  logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
  for elem in logs:
    if elem.split()[1].isdigit():
      number.append(elem)
    else:
      text.append(elem)
  text.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 식별자를 제외한 문자열 [1:]을 키로 정렬 -> 동일한 경우 후순위로 식별자 [0]
  print(text + number)
  
reorderLogFiles()

#-------------------------정답코드----------------------------
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#       letters, digits = [], []
#       for log in logs:
#         if log.split()[1].isdigit():
#           digits.append(log)
#         else:
#           letters.append(log)
#       letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
#       return letters + digits

#-------------------------제출코드----------------------------
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         text, number = [], []
#         for elem in logs:
#             if elem.split()[1].isdigit():
#                 number.append(elem)
#             else:
#                 text.append(elem)
#         text.sort(key=lambda x: (x.split()[1:], x.split()[0]))
#         return text+number