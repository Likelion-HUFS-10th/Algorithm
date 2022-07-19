s = "a"

def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1):  
        prev = s[:i]             
        cnt = 1
        sen = ''
        for j in range(i, len(s)+1, i): 
            if prev == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    sen += prev
                else:
                    sen += (str(cnt) + prev)
                prev = s[j:j+i]
                cnt = 1
        if cnt == 1:
            sen += prev
        else:
            sen += (str(cnt) + prev)
        result.append(len(sen))
    return min(result)

print(solution(s))