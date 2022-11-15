# Q. answer = ''.join(spell) → if answer == sorted(i) Why not?

# else문 생략 후 def 함수 기준 return문 들여쓰기 맞추기
def solution(spell, dic):
    for i in dic:
        if sorted(spell) == sorted(i): 
            return 1
    return 2

# 1.
from collections import Counter

def solution(spell, dic):
    answer = 0
    for i in dic:
        if len(Counter(spell) - Counter(i)) == 0: # Counter({'z': 1, 'd': 1, 'x': 1}), Counter({'d': 1, 'z': 1, 'x': 1})
            answer = 1
            break
        else:
            answer = 2
    return answer

# 2.
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2