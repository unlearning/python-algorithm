# 1.
# keypoint
# 1차원 배열 in/not in 2차원 배열 (O)
# but, 1차원 배열의 요소 in/not in 2차원 배열 (X)
# ex. id_pw[0] in db (X)
# ex. id_pw[0] in db[0] (O)

def solution(id_pw, db):
    answer = ["login", "wrong pw", "fail"]
    if id_pw in db:
        return answer[0]
    else:
        for idx in range(len(db)):
            if id_pw[0] in db[idx]:
                if id_pw[1] not in db[idx]:
                    return answer[1]
        return answer[2]

# 2.
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]): # Q.
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

# 3.
# ex. id_pw, db
# ["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

def solution(id_pw, db):
    answer = ''
    a, b = id_pw[0], id_pw[1]
    for pk, pw in db:
        # print(pk,pw) : rardss 123 yyoom 1234 meosseugi 1234
        if pk == a and pw == b:
            return "login"
    for pk, pw in db:
        if pk == a:
            return "wrong pw"
    return "fail"