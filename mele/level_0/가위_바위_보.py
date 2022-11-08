# https://school.programmers.co.kr/learn/courses/30/lessons/120839

# 내 풀이
def solution(rsp):
    answer = {
        "2": "0",
        "0": "5",
        "5": "2",
    }
    return "".join(answer[c] for c in rsp)

