# https://school.programmers.co.kr/learn/courses/30/lessons/120904

# 내 풀이
def solution(num, k):
    answer = str(num).find(str(k))
    return -1 if answer == -1 else answer + 1

# 다른 사람 풀이
def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1

def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1