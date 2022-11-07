# https://school.programmers.co.kr/learn/courses/30/lessons/120818

# 내 풀이
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price

# 다른 사람 풀이2
def solution(price):
    discount_rates = {
        500000: 0.8,
        300000: 0.9,
        100000: 0.95,
        0: 1
    }
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
