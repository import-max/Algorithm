def solution(n):
    num = list(str(n))
    num.reverse()
    l = []
    for i in num:
        l.append(int(i))
    return l