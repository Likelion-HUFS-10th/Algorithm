import sys
input = sys.stdin.readline

n = int(input())
house = list(map(int, input().split()))
antenna = (n-1)//2
house.sort()
print(house[antenna])