# 배열 회전시키기

# 첫 번째 내 풀이
def solution(numbers, direction):
    answer = 0
    result = []
    if direction in "right":
        answer = (numbers.pop(len(numbers)-1))
        result.append(answer)
        for i in numbers:
            result.append(i)
        return result
        
    else :
        answer = (numbers.pop(0))
        numbers.append(answer)
        return numbers

a = [1,2,3]
print(solution(a, "right"))

# 다른 사람 풀이
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
