from collections import deque

all = int(input())
answer = []
for _ in range(all):

    a = int(input())

    cvs = deque()
    h_x, h_y = tuple(map(int, input().split()))
    for _ in range(a + 1):
            k = tuple(map(int, input().split()))
            cvs.append(k)
    cnt = 0
    x_rst = 0
    y_rst = 0
    que = deque()
    cvs_check = [0 for _ in range(a)] + [1]
    cvs_check = deque(cvs_check)
    check = True

    while check == True :
        if cnt == 0:
            x_rst = h_x
            y_rst = h_y
        else:
            if len(que) == 0:
                answer.append("sad")
                check = False
                break
            x_rst, y_rst = que.popleft()
        for _ in range(len(cvs)):
            x, y = cvs[0]
            dis = abs(x - x_rst) + abs(y - y_rst)
            if dis <= 1000:
                que.append(cvs.popleft())
                target = cvs_check.popleft()
                if target == 1:
                    answer.append('happy')
                    check = False
                    break
                cnt += 1
            else:
                cvs.rotate(-1)
                cvs_check.rotate(-1)
                cnt += 1

for i in answer:
    print(i)
        
    








