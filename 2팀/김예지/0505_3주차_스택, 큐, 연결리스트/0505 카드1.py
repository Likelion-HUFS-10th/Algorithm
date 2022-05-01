# 2161 카드1

# by oneself
import sys
input = sys.stdin.readline

N = int(input())
queue = []

for i in range(1, N+1):
    queue.append(i)
final = []
while len(queue) != 1:
    final.append(queue[0])
    queue.pop(0)
    queue.append(queue[0])
    queue.pop(0)
    
final.append(queue[0])
final_int = [str(i) for i in final]
print(" ".join(final_int))