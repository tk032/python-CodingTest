def solution(number):
    answer = 0
    number_list = list(number)
    answer = sum(map(int,number_list)) % 9
    return answer