T = int(input())
for i in range(T):
    p = input()               
    n = int(input())  
    arr = input().strip('[]')
    if(n == 0):  
        arr = []
    else:
        arr = list(map(int, arr.split(',')))
    rev = False
    front = 0
    rear = 0

    for func in p:
        try:
            if func == 'R':
                rev = not rev
            elif not rev:
                front += 1
            else:
                rear += 1
        except:
            print('error')
            break
    if True:
        if (front + rear) <= n:
            if not rev:
                arr = arr[front:n - rear]
                print(str(arr).replace(' ', ''))
            else:
                arr = arr[::-1][rear:n - front]
                print(str(arr).replace(' ', ''))
        else:
            print('error')