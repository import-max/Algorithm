def solution(n):
    num = list(str(n))
    num.sort(reverse=True)
    l = "".join(num)
    return int(l)