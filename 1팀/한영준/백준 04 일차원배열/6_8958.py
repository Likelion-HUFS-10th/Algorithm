n = int(input())

for _ in range(n):
    cnt = 1
    ox = list(input())
    score = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            score += cnt
            cnt += 1
        else : 
            cnt = 1
    
    print(score)
