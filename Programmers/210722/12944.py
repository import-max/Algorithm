def solution(arr):
    sum = 0
    for n in arr:
        sum = sum + n
    return int(sum) / len(arr)