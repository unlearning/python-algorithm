# 1.
def solution(str1, str2):
    if str1.count(str2) > 0:
        return 1
    else:
        return 2

# 2.
def solution(str1, str2):
    return 1 if str2 in str1 else 2