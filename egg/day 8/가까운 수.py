# 가까운 수

# 내 풀이
def solution(array, n):
    array.append(n)
    array.sort()
    answer = array.index(n)

    if array[answer] == array[-1] or array[answer] == array[0]:
        return (array[answer-1] if array[answer] == array[-1] else array[answer+1])
    
    else :
        if abs(n-array[answer+1]) == abs(n-array[answer-1]):
            return (array[answer-1])
        return (array[answer-1] if abs(n-array[answer+1]) > abs(n-array[answer-1]) else array[answer+1])

# 내 풀이
def solution(array, n):
    answer = []
    array.sort()
    max = 100

    for i in array:
        if abs(i - n) < max:
            max = abs(i-n)
            answer = i

    return answer

# 다른 사람 풀이
solution = lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]


