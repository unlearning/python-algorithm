# https://school.programmers.co.kr/learn/courses/30/lessons/120888

# 내 풀이
def solution(my_string):
    answer = []
    for c in my_string:
        if c not in answer:
            answer.append(c)
    return "".join(answer)

# 다른 사람 풀이
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))