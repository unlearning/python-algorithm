# https://school.programmers.co.kr/learn/courses/30/lessons/120849

# 내 풀이
def solution(my_string):
    return my_string.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")

# 다른 사람 풀이
def solution(my_string):
    return "".join([i for i in my_string if i not in "aeiou"])

# TODO: 이해해보기
import re
def solution(my_string):
    return re.sub(r"a|e|i|o|u", "", my_string)
