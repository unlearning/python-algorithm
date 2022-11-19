# https://school.programmers.co.kr/learn/courses/30/lessons/120853

# 내 풀이
def solution(s):
    memory = []
    answer = 0
    for i in s.split():
        if i == "Z" and memory:
            answer -= memory.pop()
        else:
            answer += int(i)
            memory.append(int(i))
    return answer

