# 1.

def solution(array, n):
    answer = [] 
    array = sorted(array) # abs(n-i)가 같은 값이 여러 개일 때, 가장 작은 수가 나와야 하므로 sorted() ex. 10, 30
    for i in array:
        answer.append(abs(n-i))
    return array[answer.index(min(answer))]

# 2.
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer