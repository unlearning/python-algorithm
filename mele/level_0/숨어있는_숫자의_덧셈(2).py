# https://school.programmers.co.kr/learn/courses/30/lessons/120864

# 내 풀이
def solution(my_string):
    answer = 0
    buffer = ""
    for c in my_string:
        if c.isdigit():
            buffer += c
        else:
            answer += int(buffer) if buffer else 0
            buffer = ""
    answer += int(buffer) if buffer else 0
    return answer

# 다른 사람 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

import re
def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])
    # return sum(map(int, re.findall(r"\d+", my_string)))