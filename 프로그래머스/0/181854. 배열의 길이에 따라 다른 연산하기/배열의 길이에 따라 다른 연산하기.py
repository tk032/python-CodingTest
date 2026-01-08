def solution(arr, n):
    answer = []
    for index, i in enumerate(arr):
        if len(arr) % 2 == 1:
            if index % 2 == 0:
                answer.append(i+n)
            else:
                answer.append(i)
                
        elif len(arr) % 2 == 0:
            if index % 2 == 1:
                answer.append(i+n)
            else:
                answer.append(i)
    return answer