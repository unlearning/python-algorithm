# 1.
# i를 증가시키면서 n이 될 때까지 반복
# 케이스마다 2로 나누어질 경우, i = 2
# 아닐 경우, i = 3
# map(int, set(answer)) : 중복을 제거한 뒤, int형으로 변환
# sorted(list(map(int, set(answer)))) : iterable 객체를 list로 변환 후, 오름차순 정렬

def solution(n):
    i = 2
    answer = []
    while i <= n:
        if n % i == 0:
            n = n / i
            answer.append(i)
        else:
            i += 1
    return sorted(list(map(int, set(answer))))