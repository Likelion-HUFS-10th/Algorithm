score = input()
score_list = list(map(int, score))
p = len(score) // 2

if sum(score_list[:p]) == sum(score_list[p:]):
    print('LUCKY')
else:
    print('READY')