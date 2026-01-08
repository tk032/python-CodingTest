def solution(arr):
    answer = 0
    check = 0
    for i, arr_1 in enumerate(arr):
        for j, arr_2 in enumerate(arr_1):
            if arr[i][j] == arr[j][i]:
                check += 1

    if check == len(arr)**2:
        answer = 1
    return answer