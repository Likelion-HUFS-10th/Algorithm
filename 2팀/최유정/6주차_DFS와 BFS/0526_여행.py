from collections import defaultdict

def solution(tickets):
    dict = defaultdict(list)

    for ticket in tickets:
        dict[ticket[0]].append(ticket[1])

    for key in dict.keys():
        dict[key].sort()
#위랑 같은 코드
# def solution(tickets):
#     dict = {}
#     for ticket in tickets:
#         if ticket[0] in dict:
#             dict[ticket[0]].append(ticket[1])
#         else:
#             dict[ticket[0]] = [ticket[1]]

#     for i in dict:
#         dict[i].sort()

    start = ['ICN']
    answer = []

    while start:
        a = start[-1]
        if a not in dict or len(dict[a]) == 0:
            answer.append(start.pop())
        else:
            start.append(dict[a].pop(0))

    answer.reverse()
    return answer




tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))
