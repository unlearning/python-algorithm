# https://school.programmers.co.kr/learn/courses/30/lessons/120890

# 내 풀이
def solution(array, n):
    answer = array[0]
    for a in array:
        if abs(a - n) < abs(answer - n):
            answer = a
        elif abs(a - n) == abs(answer - n):
            answer = a if a < answer else answer
    return answer

# 다른 사람 풀이
import numpy
def solution(arr, n):
    a = numpy.array([abs(i-n) for i in arr])
    mini = numpy.where(a == min(a))[0]
    return min(arr[i] for i in mini)

def solution(array, n):
    cl = [abs(v - n) for v in array]
    mincl = min(cl)
    return min([array[i] if cl[i]==mincl else 9999 for i in range(len(cl))])
