# 1. 
# day 8.\잘라서 배열로 저장하기 풀이와 동일

def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]

# 2.
import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()