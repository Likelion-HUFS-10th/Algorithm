#------------
def possible(answer):
  for x, y, stuff in answer:
    if stuff == 0:
      if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
        continue
      else:
        return False
    elif stuff == 1:
      if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or [x-1, y, 1] in answer or [x+1, y, 1] in answer:
        continue
      else:
        return False
  return True

def check(build_frame):
  answer = []
  for frame in build_frame:
    x, y, stuff, operate = frame
    if operate == 0:
      answer.remove([x, y, stuff])
      if not possible(answer):
        answer.append([x, y, stuff])
    elif operate == 1:
      answer.append([x, y, stuff])
      if not possible(answer):
        answer.remove([x, y, stuff])
  return sorted(answer)

# build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
# print(check(build_frame))