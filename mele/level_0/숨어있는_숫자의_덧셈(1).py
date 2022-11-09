# https://school.programmers.co.kr/learn/courses/30/lessons/120851

# 내 풀이
def solution(my_string):
    return sum(int(c) for c in my_string if c.isdigit())

# 다른 사람 풀이
def solution(my_string):
    answer = 0
    for c in my_string:
        try:
            answer += int(c)
        except:
            continue
    return answer