def solution(a, b):
    c = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a+1):
            c += i
        return c
    elif a < b:
        for i in range(a, b+1):
            c += i
        return c
