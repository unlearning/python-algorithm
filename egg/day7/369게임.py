# 369 게임

# 첫 번째 내 풀이
def solution(order):
    count = 0
    answer = (str(order))

    for i in range(len(answer)):
        if answer[i] == "3" or answer[i] == "6" or answer[i] == "9":
            count += 1
    return count


# 다른 사람 풀이
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
