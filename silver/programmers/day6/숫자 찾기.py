# 1.
def solution(num, k):
    s_num = str(num)
    s_k = 0
    if str(k) in s_num:
        s_k = s_num.find(str(k))
        return s_k + 1
    elif str(k) not in s_num:
        return -1

# 2.
def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1
