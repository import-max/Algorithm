def solution(arr):
    num = []
    num.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            continue
        else:
            num.append(arr[i])
    return num
