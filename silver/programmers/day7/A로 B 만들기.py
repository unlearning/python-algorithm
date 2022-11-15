# 1.
from collections import Counter

def solution(before, after):
    if Counter(before) == Counter(after):
        return 1
    else:
        return 0

# 2. 순서와 무관하게 동일한 문자(열) 비교 → sorted
def solution(before, after):
    before = sorted(before)
    after = sorted(after)
    if before == after:
        return 1
    else:
        return 0

# Q. X
def solution(before, after):
    for i in before:
        if i in after:
            return 1
        else:
            return 0