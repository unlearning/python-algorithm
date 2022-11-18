# 진료순서 정하기

# 내 풀이
def solution(emergency):
    
    flist = sorted(emergency)
    flist.reverse()
    answer = {i:flist.index(i)+1 for i in emergency}

    return list(answer.values())

# 다른 사람 풀이
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]