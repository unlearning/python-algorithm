# https://school.programmers.co.kr/learn/courses/30/lessons/120825

# 내 풀이
def solution(my_string, n):
    return "".join(c * n for c in my_string)

# 다른 사람 풀이
def solution(my_string, n):
    answer = ''
    for m in my_string:
        answer += (m * n)
    return answer