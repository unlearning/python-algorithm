# 컨트롤 제트

# 내 풀이
def solution(s):
    answer = s.split()
    result = []
    total = []

    for i in answer:
        if i == "Z":
            result.append(answer[answer.index(i)-1])
            result.append(answer[answer.index(i)])
            answer.remove(i)
    total = list(set(answer) - set(result))
    
    return sum([int(i) for i in total])


print(solution("10 Z 20 Z 1"))
