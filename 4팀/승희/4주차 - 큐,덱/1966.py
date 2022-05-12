"""
target_idx 에 내가 알아내고 싶은 문서의 인덱스를 담음
항상 pop이 되는 것은 0번째의 문서 (가장 중요도가 높으면 pop되고 사라짐, 높은게 아니라면 pop 되고 맨 뒤에 붙음)
0번째의 문서가 가장 중요도가 높다면 pop 되고 횟수가 늘어남 (횟수가 늘어나는 때는 이때뿐)
만약 내가 pop 한 문서가 내가 알아내고 싶은 target_idx 였다면 break 하고 cnt 출력
target_idx 가 아니었다면 알아내고 싶은 문서가 하나 앞으로 갔을 것이기에 idx-=1

0번째 문서가 가장 중요도가 높은 것이 아니라면 popleft 하고 이를 맨 뒤에 붙이기
만약 내가 지금 보고 있는 문서가 내가 알아내고 싶은 문서였다면 target_idx를 맨 뒤로 업데이트
알아내고 싶은 문서가 아니었다면 하나 앞으로 밀려났을 것이기에 idx -=1
"""
from collections import deque

testcase = int(input()) #테스트케이스의 수

for _ in range(testcase):
    n,m = map(int,input().split()) #n은 문서의 개수 / m은 궁금한 문서의 위치
    documents = deque(list(map(int,input().split())))
    target_idx = m
    cnt=0
    while True:
        if documents[0]==max(documents):
            documents.popleft()
            cnt+=1
            if target_idx==0:
                break
            else:
                target_idx -=1
        else:
            deleted_document = documents.popleft()
            documents.append(deleted_document)
            if target_idx==0:
                target_idx = len(documents)-1
            else:
                target_idx-=1
    print(cnt)
