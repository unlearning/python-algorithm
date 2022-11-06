# 1.
def solution(s1, s2):
    count = 0 
    for i in s1:
        for j in s2:
            if i == j:
                count += 1
    return count

# 2.
def solution(s1, s2):
    return len(set(s1) & set(s2)) # 집합 연산자 &(and)