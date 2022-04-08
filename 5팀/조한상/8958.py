n = int(input())

for i in range(n):
    ox = input()
    score = 0
    sum = 0
    for j in ox:
        if j == 'O':
            score +=1
        else:
            score = 0;
        sum += score
    print(sum)