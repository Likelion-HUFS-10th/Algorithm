# 유효한 괄호
# okay에 없으면 스택에 push -> 스택에서 pop한 값이 okay에 키로 들어가 있지 않으면 False -> 그냥 빠져나오면 짝이 맞는 거니까 True 반환
# ()[]{}

def isValid(input_char):
  stack = []
  okay = {"(" : ")", "[" : "]", "{" : "}"}  
  for char in  input_char:
    if char in okay:
      stack.append(char)
    elif stack.pop() != okay[char]:
      return False
    return True

input_char = input()
print(isValid(input_char))

#-------------------------제출코드----------------------------
# stack에 아무 것도 없을 경우 예외처리 해야함
# 1. 짝이 맞음 -> T
# 2. 짝은 있는 문자열인데 순서가 틀림 -> F
# 3. 짝이 없는 문자열 -> F
# 3번 먼저 거르기 -> 2번 거르기

def isValid(self, s: str) -> bool:
  stack = []
  table = {"(" : ")", "[" : "]", "{" : "}"}

  for char in s:
    if char not in table:
      stack.append(char)
    elif not stack or stack.pop() != table[char]:
      return False
  return len(stack) == 0

s = input()
print(isValid(s))