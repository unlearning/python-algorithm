# https://school.programmers.co.kr/learn/courses/30/lessons/120882

# 내 풀이
def solution(score):
    avg = [(a+b)/2 for [a, b] in score]
    return [sorted(avg, reverse=True).index(i)+1 for i in avg]

# 다른 사람 풀이
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]
