from itertools import product
from collections import deque

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
# user_id에 있는걸 별표로 변경 후 비교하기

def star(b):
    star = []
    for i in range(len(b)):
        if b[i] == '*':
            star.append(i)
    return star

def change(star, u):
    new_u = list(u)
    for s in star:
        new_u[s] = '*'
    new_u = ''.join(new_u)
    return new_u


def solution(user_id, banned_id):
    result = [[] for _ in range(len(banned_id))]
    for b in range(len(banned_id)):
        s = star(banned_id[b])
        for u in range(len(user_id)):
            if len(banned_id[b]) == len(user_id[u]):
                new_u = change(s, user_id[u])
                if new_u == banned_id[b]:
                    result[b].append(user_id[u])

    answer = deque(product(*result))
    an = []
    while answer:
        a = answer.pop()
        if len(a) != len(set(a)):
            continue
        else:
            a = list(a)
            a.sort()
            if a not in an:
                an.append(a)
    return len(an)

print(solution(user_id, banned_id))