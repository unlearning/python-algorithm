# 1.
def solution(array, n):
    answer = []
    for i in array:
        answer.append(abs(n - i))
        print(answer)
        print(answer.index(min(answer)))
    return answer[answer.index(min(answer))] # Q.

print(solution([3, 10, 28], 20))