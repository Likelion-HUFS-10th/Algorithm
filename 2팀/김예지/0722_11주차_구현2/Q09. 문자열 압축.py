def solution(s):
  s_lst = list(s)
  min_length = len(s_lst)
  num_cnt = 0

  if len(s_lst) % 2 == 0:
    cut = len(s_lst) // 2
  else:
    cut = (len(s_lst) - 1) // 2

  for num in range(1, cut+1):
    start = 0
    end = num
    new_lst = []
    for i in range(len(s_lst) // num):
      new_lst.append(''.join(s_lst[start:end]))
      start = end
      end += num

    origin_s = new_lst[0]
    length = len(s_lst)
    num_cnt = 0
    for i in range(1, len(new_lst)):
      next_s = new_lst[i]
      if origin_s == next_s:
        if num_cnt == 0:
          length -= (num - 1)
          num_cnt += 1
        else:
          length -= num
      else:
        num_cnt = 0
        origin_s = new_lst[i]
      if length < min_length:
        min_length = length

  return min_length

# print(solution(s:=input()))
