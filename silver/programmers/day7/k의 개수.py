# Q. if x.find(k) >= 1 → answer += 1 Why not? (x : str, k : str)

# 1.
# defaultdict(int) : 딕셔너리에 key 값이 존재하지 않아도 기본값 초기화 가능

# 풀이 (예 : i가 11일 경우, 두 번째 for 문 내에 print(str(n_1), n_2)를 추가하여 풀이 확인 추천)
# for n_1 in range(i, j + 1)
# → n_1 = 11
# for n_2 in str(n_1)
# → n_1 : 11, n_2 = 1
# d[n_2] += 1 
# → d[1] += 1

from collections import defaultdict

def solution(i, j, k):
    d = defaultdict(int)
    for n_1 in range(i, j + 1):
        for n_2 in str(n_1):
            d[n_2] += 1
    return d[str(k)]

# 2.
def solution(i, j, k):
    answer = sum([str(i).count(str(k)) for i in range(i, j + 1)]) # '11'.count('1') → 2
    return answer