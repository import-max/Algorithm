def solution(n):
    m = str(n)
    a = []
    for i in range(0,len(m)):
        a.append(m[i])
    a = list(map(int, a))
    s = 0
    for i in a:
        s += i
    return s