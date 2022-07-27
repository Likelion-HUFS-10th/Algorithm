n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def solution(n, build_frame):
    answer = []
    for b in build_frame:
        if b[3] == 1: # 설치
            answer.append([b[0], b[1], b[2]])
            if not check(answer):
                answer.remove([b[0], b[1], b[2]])
        if b[3] == 0: #삭제
            answer.remove([b[0], b[1], b[2]])
            if not check(answer):
                answer.append([b[0], b[1], b[2]])
    answer.sort()

    return answer


def check(answer):
    for i in answer:
        if i[2] == 0: #기둥
            if i[1] == 0 or ([i[0], i[1]-1, 0] in answer) or ([i[0]-1, i[1], 1] in answer) or ([i[0], i[1], 1] in answer):
                continue
            return False
        if i[2] == 1:
            if ([i[0]+1, i[1]-1, 0] in answer) or ([i[0], i[1]-1, 0] in answer) or (([i[0]-1, i[1], 1] in answer) and ([i[0]+1, i[1], 1] in answer)):
                continue
            return False
    return True

print(solution(n, build_frame))