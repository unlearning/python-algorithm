# https://school.programmers.co.kr/learn/courses/30/lessons/120894

# 내 풀이
def solution(numbers):
    num_list = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    buffer = ""
    answer = ""
    for c in numbers:
        buffer += c
        if buffer in num_list:
            answer += num_list[buffer]
            buffer = ""
    return int(answer)

# 다른 사람 풀이
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)