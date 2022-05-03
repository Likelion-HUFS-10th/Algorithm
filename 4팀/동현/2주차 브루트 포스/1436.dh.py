N = int(input())
number = 0
answer = 0
while True:
    if '666' in str(number): 
        answer += 1
        if answer == N:
            print(number)
            break
        number += 1
    else:
        number += 1