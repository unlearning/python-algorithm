# 등수 매기기

# 내 풀이
def solution(score):
    answer = []
    total = [sum(i) for i in score]

    result = (sorted(total, reverse = True))
    results = []

    for i in total:
        results.append(result.index(i)+1)
    

    return results

# 다른 사람 풀이
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]