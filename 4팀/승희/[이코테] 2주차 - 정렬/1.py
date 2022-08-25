n = int(input()) #수열에 속해 있는 수의 개수
arr = [
    int(input())
    for _ in range(n)
]

arr.sort(reverse=True)

print(arr)