n, m = map(int, input().split())
students = [0] * (n+1)
for s in range(n+1):
    students[s] = s

def find_leader(students, l):
    if students[l] != l:
        students[l] = find_leader(students, students[l])
    return students[l]
def union_team(x, y):
    lx = find_leader(students, x)
    ly = find_leader(students, y)
    if lx > ly:
        students[x] = ly
    else:
        students[y] = lx

def check_same_team(x, y):
    if students[x] == students[y]:
        return True
    else:
        return False

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_team(a, b)
    elif oper == 1:
        if check_same_team(a, b):
            print("YES")
        else:
            print("NO")