'''
문자열 배열을 받아 애너그램 단위로 그룹핑하라.

입력
["eat", "tea", "tan", "ate", "nat", "bat"]

출력
[
    ["ate", "eat", "tea"],
    ["nat", "tan"], 
    ["bat"]
]
'''
def groupAnagrams(strs: list) :
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())

