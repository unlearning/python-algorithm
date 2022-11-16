# 영어가 싫어요

# 내 풀이
def solution(numbers):
    answer = {
        "zero"  : "0",
        "one"   : "1",
        "two"   : "2",
        "three" : "3",
        "four"  : "4",
        "five"  : "5",
        "six"   : "6",
        "seven" : "7",
        "eight" : "8",
        "nine"  : "9"
    }

    number = ""
    result = ""

    for i in numbers:
        number += i
        if number in list(answer.keys()):
            result += answer[number]
            number = ""

    return int(result)

# 다른 사람 풀이
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    print(num, eng)
    return int(numbers)

