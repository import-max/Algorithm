def solution(n, m):
    mm = 0
    nn = 0
    r = 0
    if n > m:
        r = n % m
        if r == 0:
            mm = m
        else:
            while True:
                mm = m % r
                if mm == 0:
                    break
            return mm

    elif m > n:
        r = m % n
        if r == 0:
            mm = n
        else:
            while True:
                mm = n % r
                if mm == 0:
                    break
            return mm

    nn = (n * m) / mm
    a = []
    a.append(mm)
    a.append(nn)
    return a
