# https://school.programmers.co.kr/learn/courses/30/lessons/120816

# 내 풀이
def solution(slice, n):
    return (n - 1) // slice + 1

# 다른 사람 풀이
def solution(slice, n):
    return (n + slice - 1) // slice
  
def solution(slice, n):
    return -(-n//slice)