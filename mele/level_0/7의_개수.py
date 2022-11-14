# https://school.programmers.co.kr/learn/courses/30/lessons/120912

# 내 풀이
def solution(array):
    return "".join(str(array)).count("7")

# 다른 사람 풀이
def solution(array):
    return str(array).count('7')

def solution(array):
    answer = sum([str(i).count("7") for i in array])
    return answer

from functools import reduce
def solution(array):
    return reduce(lambda x,y: x+y, map(lambda x: str(x), array)).count('7')