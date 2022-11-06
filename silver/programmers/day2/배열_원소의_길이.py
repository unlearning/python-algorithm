# 1.
def solution(strlist):
    total = []
    for i in strlist:
        length = len(i)
        total.append(length)
    return total

# 2.
def solution(strlist):
    answer =[]
    for i in strlist:
        answer.append(len(i))
    return answer

# 3.
def solution(strlist):
    return [len(str) for str in strlist]

# 4.
def solution(strlist):
    return list(map(lambda v: len(v), strlist))