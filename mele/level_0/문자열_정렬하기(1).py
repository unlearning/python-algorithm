# https://school.programmers.co.kr/learn/courses/30/lessons/120850 

# 내 풀이
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])