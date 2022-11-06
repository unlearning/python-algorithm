# https://school.programmers.co.kr/learn/courses/30/lessons/120819

# 내 풀이
def solution(money):
    return [money // 5500, money % 5500]

# 다른 사람 풀이
def solution(money):
    return divmod(money, 5500)