# 중복 문자 제거
# 중복 문자를 제외하고 사전식 순서로 나열하라
# 사전식 순서 : 사전에서 가장 먼저 찾을 수 있는 순서
# ebcabc -> eabc / bcabc -> abc / cbacdcbc -> acdb

#-------------------------방법1----------------------------
# 스택 없이
# char가 스택에 이미 있고 뒤에 다시 반복돼서 나타나면 pop()해서 제거

input_char, stack = input(), []

for i in range(len(input_char)):
  if input_char[i] in stack:
    # 해당 순번 loop 넘어가고 다음 loop로
    continue
  # 1. stack 안에 값이 있고
  # 2. 현재 위치의 char이 stack의 top보다 작고
  # 3. 현재 위치에서 뒷 인덱스에 중복된 값이 있으면
  while stack and input_char[i] < stack[-1] and input_char[i:].count(stack[-1]) > 0:
    # stack 비우기 -> 뒤에 붙일 문자가 남아있는 문자들이니까
    stack.pop()
  stack.append(input_char[i])
print("".join(stack))

#-------------------------방법2----------------------------
# 스택에서 가능한 연산만 수행, 검색 기능은 seen 변수에서 실행

input_char, stack, seen = input(), [], set()

for i in range(len(input_char)):
  if input_char[i] in stack:
    continue
  while stack and input_char[i] < stack[-1] and input_char[i:].count(stack[-1]) > 0:
    # 사전상 순서가 안맞아서 뒤에 와야하고 중복도 있기 때문에 stack과 seen 둘 다에서 제거
    seen.remove(stack.pop())
  stack.append(input_char[i])
  seen.add(input_char[i])
print("".join(stack))