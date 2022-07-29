from collections import deque

u = []
new = []
final = []

def solution(p):
  p = deque(list(p))
  if not p:
    return ''.join(final)

  dict = {"(" : 0, ")" : 0}
  while p:
    n = p.popleft()
    dict[n] += 1
    u.append(n)
    if dict["("] == dict[")"]:
      break

  if u[0] == "(" and u[-1] == ")":
    for i in u:
      final.append(i)
    u.clear()
    solution(p)

  else:
    final.append("(")
    u.pop(0)
    u.pop()
    for i in range(len(u)):
      if u[i] == "(":
        u[i] = ")"
      else:
        u[i] = "("
    for i in u:
      new.append(i)
    u.clear()
    solution(p)
    final.append(")")
    for i in new:
      final.append(i) 
  return ''.join(final)

# p = ")("
# print(solution(p))