# https://school.programmers.co.kr/learn/courses/30/lessons/120892

# 내 풀이
def solution(cipher, code):
    return "".join(cipher[code-1::code]) # 리스트로 반환되는 줄..

# 다른 사람 풀이
def solution(cipher, code):
    return cipher[code-1::code]