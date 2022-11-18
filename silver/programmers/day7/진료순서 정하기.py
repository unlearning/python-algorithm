# 1.
def solution(emergency):
    a_d = []
    s_answer = sorted(emergency, reverse=True)
    answer = [i for i in range(1, len(s_answer) + 1)]
    dic = dict(zip(s_answer, answer))
    for i in emergency:
        for j in dic:
            if i == j:
                a_d.append(dic[i])                
    return a_d

# 2.
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

# 3.
def solution(emergency):
    e = sorted(emergency,reverse=True)
    return [e.index(i)+1 for i in emergency]