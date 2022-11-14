# 한 번만 등장한 문자

# 내 풀이
def solution(s):
    answer = ''

    answer = {i: s.count(i) for i in s}
    print(answer)
    return "".join(sorted([i for i,j in answer.items() if j == 1]))


# 다른 사람 풀이
from collections import defaultdict

def solution(s):
    s_dict = defaultdict(set)

    for v in set(s):
        s_dict[s.count(v)].add(v)
    return "".join(sorted(sorted(s_dict.items(), key=lambda v: v[0])[0][1]))

