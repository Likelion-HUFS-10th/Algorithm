import sys
t = int(sys.stdin.readline())

for i in range(t):
    a,b = sys.stdin.readline().split()
    for i in range(len(b)):
        print(b[i]*int(a), end="")
    print("\n")


