# https://school.programmers.co.kr/learn/courses/30/lessons/120869

# 내 풀이
def solution(spell, dic):
    for word in dic:
        step = 0
        for c in spell:
            if c in word # and word.count(c) == 1: # if ["a","b"] & ["abb"] -> False
                step += 1
        if step == len(spell):
            return 1
    return 2

# 다른 사람 풀이
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

import itertools
def solution(spell, dic):
    return int(bool(list(set(map("".join, list(itertools.permutations(spell)))) & set(dic)))) or 2

def is_make(word, spells):
    for spell in spells:
        if spell not in word:
            return False
    return True
def solution(spell, dic):
    return 1 if list(filter(lambda word: is_make(word, spell) , dic)) else 2

from collections import Counter
def solution(spell, dic):
    for word in dic:
        counter=Counter(word)
        if set(spell)==set(counter.keys()):
            return 1
    return 2