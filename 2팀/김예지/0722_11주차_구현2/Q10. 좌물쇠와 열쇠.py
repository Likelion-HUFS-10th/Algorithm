key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
N = len(key)

def turn_key():
  global key
  key_lst = []
  new_key = []
  for i in range(N):
    for j in range(N-1, -1, -1):
      key_lst.append(key[j][i])
    new_key.append(key_lst)
    key_lst = []
  key = new_key
  return key

print(turn_key())
print(turn_key())
print(turn_key())
print(turn_key())