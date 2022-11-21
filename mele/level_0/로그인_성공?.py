# https://school.programmers.co.kr/learn/courses/30/lessons/120883

# 내 풀이
def solution(id_pw, db):
    for [id, pw] in db:
        if id == id_pw[0]:
            if pw == id_pw[1]:
                return 'login'
            return 'wrong pw'
    return 'fail'

# 다른 사람 풀이
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"