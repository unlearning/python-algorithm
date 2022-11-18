# 외계어 사전

# 내 풀이
def solution(spell, dic):
    answer = 2
    count = 0

    for i in dic:
        for j in spell:
            if j in i:
                count += 1
        if count == len(spell):
            answer = 1
        count = 0

    return answer

# 다른 사람 풀이
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2