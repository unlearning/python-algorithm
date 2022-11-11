# https://school.programmers.co.kr/learn/courses/30/lessons/120834

# 내 풀이
def solution(age):
    return "".join(chr(int(i) + 97) for i in str(age))

# 다른 사람 풀이
def solution(age):
    return ''.join([chr(ord('a')+int(i)) for i in str(age)])

def solution(age):
    conv = {
        '0':'a',
        '1':'b',
        '2':'c',
        '3':'d',
        '4':'e',
        '5':'f',
        '6':'g',
        '7':'h',
        '8':'i',
        '9':'j'
    }
    return ''.join(conv[i] for i in str(age))

import string
def solution(age):
    return "".join(map(lambda v: string.ascii_lowercase[int(v)], str(age)))