# 1.
import numpy as np

def solution(array):
    mv = np.median(array)
    return mv

# 2.
def solution(array):
    return sorted(array)[len(array) // 2]
