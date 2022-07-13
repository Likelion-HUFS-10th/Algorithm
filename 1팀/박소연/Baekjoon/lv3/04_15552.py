# input 대신 sys 모듈의 stdin.readline 함수 사용
# for 시간단축

import sys

t = int(sys.stdin.readline()) # input이랑 똑같이 문자열로 입력

for i in range(t):
  a, b = map(int, sys.stdin.readline().split())
  print(a + b)

