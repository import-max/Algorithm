def solution(n):
    answer = ''
    for i in range(0, n):
        if n % 2 == 0:
            answer = '수박' * int(n/2)
        else:
            answer = '수박' * int(n/2) + '수'
    return answer
