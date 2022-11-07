# https://school.programmers.co.kr/learn/courses/30/lessons/120826

# 내 풀이
def solution(my_string, letter):
    return my_string.replace(letter, "")

# 다른 사람 풀이
def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    return answer

def solution(my_string, letter):
    return ''.join([c for c in my_string if c != letter])