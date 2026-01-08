def solution(arr, idx):
    answer = -1
    for index, i in enumerate(arr):
        if index >= idx and i == 1:
            answer = index
            break
    return answer