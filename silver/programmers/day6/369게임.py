# 1.
def solution(order):
    clap = [3,6,9]
    count = 0

    for i in list(map(int, str(order))):
        if i in clap:
            count += 1
    return count

# 2.
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
