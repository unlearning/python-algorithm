# https://school.programmers.co.kr/learn/courses/30/lessons/120885

# 내 풀이
def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

# 다른 사람 풀이
def solution(bin1, bin2):
    return format(int(bin1,2) + int (bin2,2), 'b')