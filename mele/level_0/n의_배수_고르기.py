# https://school.programmers.co.kr/learn/courses/30/lessons/120905

# 내 풀이
def solution(n, numlist):
    return [i for i in numlist if i % n == 0]

# 다른 사람의 풀이
def solution(n, numlist):
    answer = []
    for item in numlist:
        if item%n == 0:
            answer.append(item)
    return answer