'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.

입력
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


출력
"ball"
'''

# def mostCommonWord(paragraph: str, banned : list) -> str:
#     para_lst = paragraph.lower().split()
#     para_redced = list(set(para_lst)).pop('hit')
#     cnt = []
#     for i in para_redced:
#         word_cnt = para_lst.count(i)
#         cnt.append(word_cnt)
#     return para_redced[cnt.index(max(cnt))]
import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
paragraph = paragraph.isalnum()
para_lst = list(set(paragraph.lower().split(" ")))
print(paragraph)

# para_lst = list(set(paragraph.lower().split(" ")))
# cnt = []
# for i in para_lst:
#     if i not in banned:
#         each_cnt = 0


#     else:
#         continue
# print(cnt)

    
    



'''
#1. 리스트 컴프리헨션, Counter 객체 사용
import collections
def mostCommonWord(self, paragraph: str, banned: list) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    
    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]
'''

