# 금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력
# 대소문자 구분X, 마침표, 쉼표도 무시
# para.remove(banned_arr[0]) -> .remove("값")는 가장 먼저 발견된 요소만 지워줌
# 전처리 미흡해서 통과 못한 테스트 케이스 있음 -> ex)a, a, a, a, b,b,b,c, c

input_para = input()
para = "".join( x.lower() for x in input_para if x not in ",.")
banned = input()
banned_arr = []
banned_arr.append(banned)

para = list(para.split())
para = [ para[i] for i in range(len(para)) if para[i] not in banned_arr ]

cnt_arr = []
cnt_arr = [ para.count(para[i]) for i in range(len(para)) ]
print(para[cnt_arr.index(max(cnt_arr))])

#-------------------------답안코드1----------------------------
# 데이터 전처리 작업 필요
# re.sub 정규식 섞어쓰기 -> ^ == not / \w == 단어 문자
# import re 필요 -> re.sub（정규 표현식, 대상 문자열 , 치환 문자
# re.sub(r"[^\w]", " ", paragraph) -> r"" : 문자를 있는 그대로 판단 / " " : 공백으로 대체 / paragraph : paragraph에서

# words = [word for word in re.sub(r"[^\w]", " ", paragraph).lower().split() if word not in banned]
# Counter 객체 사용 -> 개수 세는 모듈

#-------------------------제출코드----------------------------
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#       words = [word for word in re.sub(r"[^\w]", " ", paragraph).lower().split() if word not in banned]
#       cnt_arr = []
#       cnt_arr = [ words.count(words[i]) for i in range(len(words)) ]
#       return words[cnt_arr.index(max(cnt_arr))]