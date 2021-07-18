def solution(seoul):
    answer = ''
    if "Kim" in seoul:
        answer = seoul.index("Kim")
        answer = '김서방은 ' + str(answer) + '에 있다'
    return answer