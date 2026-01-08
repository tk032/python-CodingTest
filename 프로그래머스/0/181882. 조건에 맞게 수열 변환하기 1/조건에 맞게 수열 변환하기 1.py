def solution(arr):
    answer = []
    for index, i in enumerate(arr):
        if i >= 50 and i % 2 == 0:
            arr[index] = i / 2
        if i < 50 and i % 2  == 1:
            arr[index] = i * 2
    answer = arr
    return answer