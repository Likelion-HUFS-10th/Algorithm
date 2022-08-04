def check(u): #올바른지에 대한 판별
    p_list = []
    for par in u:
        if par == '(': p_list.append(par)
        else:
            if p_list != []: p_list.pop()
            else: return False
    return True

def divide(p):
    start = 0
    end = 0
    for i in range(len(p)):
        if p[i] == '(': start += 1
        else: end += 1
        if start == end: return p[:i+1], p[i+1:]

def solution(p):
    answer = ''
    if p == "":
        return ""
    u, v = divide(p)
    if check(u): return u + solution(v)
    else:
        answer += ('(' + solution(v) + ')')
        for p in u[1:len(u)-1]:
            if p == '(': answer += ')'
            else: answer += '('
    return answer

p = ')('
print(solution(p))