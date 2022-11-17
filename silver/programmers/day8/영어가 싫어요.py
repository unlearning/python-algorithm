# 1.
def solution(numbers):
    answer = {
        'one' : '1', 'two': '2', 'three': '3',
        'four' : '4', 'five' : '5', 'zero' : '0',
        'six' : '6', 'seven' : '7', 'eight' : '8',
        'nine' : '9'
    }
    for i in answer.keys(): # 처음부터 하나씩 보므로, 후반 값을 인식 못함 ex. nineone
        numbers = numbers.replace(i, answer[i])
    return int(numbers)

# 2.
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)