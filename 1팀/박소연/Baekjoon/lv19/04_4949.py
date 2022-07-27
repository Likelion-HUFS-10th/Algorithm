# 균형잡힌 세상
# 괄호 짝 판단하기
# 입력 종료조건 : "."
# 딕셔너리에 왼쪽 괄호 넣기 -> 입력 값이 key에 있으면 스택에 넣기 -> value이면 top이랑 짝 맞는지 확인 하고 스택 pop

####################################### 왜 오답? ##############################################
# input_spot = True
# vps = {"(" : ")", "[" : "]"}

# while input_spot:
#   input_sen = input()
#   answer="yes"

#   if input_sen == ".":
#     input_spot = False
#     break
#   else:
#     stack = []
#     for elem in input_sen:
#       if elem == ".":
#         break
#       elif elem in list(vps.keys()):
#         stack.append(elem)
#       # 3.0 이상에서는 list로 감싸줘야 함(안그러면 type: dict_values)
#       elif elem in list(vps.values()):
#         if stack and elem == vps[stack[-1]]:
#           stack.pop()
#         else:
#           answer="no"
#           break
#     print(answer)

####################################### 정답 ##############################################
input_spot = True
vps = {"(" : ")", "[" : "]"}

while input_spot:
  input_sen = input()
  answer="yes"
  # 종료 조건
  if input_sen == ".":
    input_spot = False
    break
  stack = []
  for elem in input_sen:
    # vps의 key에 속하면 = 왼쪽 괄호면 스택에 추가
    if elem in list(vps.keys()):
      stack.append(elem)
    # 3.0 이상에서는 list로 감싸줘야 함(안그러면 type: dict_values)
    # 오른쪽 괄호면 스택의 top과 비교 후 같으면 pop 다르면 짝이 안맞는거니까 no
    elif elem in list(vps.values()):
      if stack and elem == vps[stack[-1]]:
        stack.pop()
      else:
        answer="no"
        break
  print(answer if not stack else "no")
  