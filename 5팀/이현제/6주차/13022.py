a = list(input())
pointer = 0
word_cnt = 0
word_cnt_resister = 0

box = ['w','o','l','f']
box_pointer = 0

while pointer < len(a):
    print(f'pointer : {pointer} word_count: {word_cnt} w_rs:{word_cnt_resister} bp: {box_pointer}')
    if a[pointer] == box[box_pointer]:
        word_cnt += 1
        pointer += 1
    else:
        box_pointer += 1
        box_pointer = box_pointer % 4

        if a[pointer] != box[box_pointer]:
            print('0')
            quit()
        elif box_pointer >= 2 and word_cnt != word_cnt_resister:
            print('0')
            quit()
        else:
            word_cnt_resister = word_cnt
            word_cnt = 1
            pointer += 1

if box_pointer == 3 and word_cnt == word_cnt_resister:
    print('1')
else:
    print('0')




