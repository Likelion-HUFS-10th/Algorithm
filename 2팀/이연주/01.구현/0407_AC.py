def solution(n, cmds, arr):
    rev = False
    for cmd in cmds:
        if cmd == 'R':
            rev = not rev
        else:
            if arr:
                delete_idx = 0 if rev == False else -1
                del arr[delete_idx]
            else:
                print('error')
                return
    if rev == True:
        arr.reverse()
    print('[' + ','.join(arr) + ']')


T = int(input())

for _ in range(T):
    cmds = list(input())
    n = int(input())
    input_arr = input().lstrip('[').rstrip(']')
    arr = [] if input_arr == '' else list(input_arr.split(','))
    solution(n, cmds, arr)
