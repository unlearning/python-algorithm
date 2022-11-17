# https://school.programmers.co.kr/learn/courses/30/lessons/120842

# 내 풀이
def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]

# 다른 사람 풀이
import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()