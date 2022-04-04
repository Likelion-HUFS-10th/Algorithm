train = [
    list(map(int, input().split()))
    for _ in range(10)
]
train_now = 0
train_board = []
for i in range(10):
    num_board = train[i][1] - train[i][0]
    train_now += num_board
    train_board.append(train_now)

print(max(train_board))