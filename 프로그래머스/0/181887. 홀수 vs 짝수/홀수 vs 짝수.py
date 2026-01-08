def solution(num_list):
    answer = 0
    odd = num_list[::2]
    even = num_list[1::2]
    if sum(odd) >= sum(even):
        answer = sum(odd)
    else:
        answer = sum(even)
    return answer