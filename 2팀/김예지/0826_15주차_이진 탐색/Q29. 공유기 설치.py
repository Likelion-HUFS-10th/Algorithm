n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes = sorted(homes)
array = [i for i in range(min(homes), max(homes)+1)]

result = 0
def binary_search(array, homes, start, end):
    global result, c
    if c <= 0:
        return result
    mid = (start + end) // 2
    if array[mid] in homes:
        result = min(abs(min(homes)-array[mid]), abs(max(homes)-1-array[mid]))
        array[mid] = 'c'
        c -= 1
    else:
        binary_search(array, homes, start, end-1)
        binary_search(array, homes, start+1, end)

if c == 2:
    print(max(homes) - min(homes))
else:
    array[0] = array[max(homes)-1] = 'c'
    c -= 2
    binary_search(array, homes, min(homes), max(homes)-1)
    print(result)

