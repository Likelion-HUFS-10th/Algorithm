N = 4
stages = [4,4,4,4,4]

def solution(N, stages):
    answer = []
    stage = {}
    rest = len(stages)
    for i in range(N):
        stage[i+1] = 0
    for s in stages:
        if s in stage: stage[s] += 1
        else: continue
    for i in range(1, N+1):
        rest -= stage[i]
        if stage[i] == 0 or rest == 0:
            continue
        stage[i] = stage[i] / rest
    for key, value in sorted(stage.items(), key=lambda x:x[1], reverse=True):
        answer.append(key)
    return answer

print(solution(N, stages))