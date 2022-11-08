# https://school.programmers.co.kr/learn/courses/30/lessons/120893

# 내 풀이
def flip(char):
    if char.isupper():
        return char.lower()
    return char.upper()

def solution(my_string):
    return "".join([flip(c) for c in my_string])

# 다른 사람의 풀이
def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])