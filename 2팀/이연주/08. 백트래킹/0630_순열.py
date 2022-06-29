import sys
input = sys.stdin.readline

while True:
    try:
        answer = ''
        string, idx_origin = input().split()
        arr, arr_1, idx = list(string), list(string), int(idx_origin)
        n = len(string)
        cnt = 1
        for i in range(1, n+1):
            cnt *= i
        if idx > cnt:
            print(string, idx, "= No permutation")
        else:
            for i in range(n, 0, -1):
                cnt /= i
                if idx > cnt:
                    k = int(idx // cnt)
                    if idx % cnt == 0:
                        k -= 1                    
                    answer += arr[k]
                    idx = idx - (cnt * k)
                    arr.remove(arr[k])
                else:
                    answer += arr[0]
                    arr.remove(arr[0])
            answer += str(''.join(arr))
            print(string, idx_origin, "=", answer)
    except:
        break
