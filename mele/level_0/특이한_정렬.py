# https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=python3

# 내 풀이
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x-n), -x))

# 다른 사람 풀이
from collections import defaultdict
def solution(numlist, n):
    diff_dict = defaultdict(list)
    for num in numlist:
        diff_dict[abs(num-n)].append(num)
    answer = []
    for diff, nums in sorted(diff_dict.items(), key=lambda v: v[0]):
        nums = sorted(nums)
        while nums:
            answer.append(nums.pop(-1))
    return answer

def solution(numlist, n):
    answer = []
    newlist = sorted([abs(i - n) for i in numlist])
    for el in newlist:
        if el + n in numlist:
            answer.append(el + n)
            numlist.remove(el + n)
        else:
            answer.append(n - el)
            numlist.remove(n - el)
    return answer
