def solution(my_string, is_suffix):
    reverse_my_string = my_string[::-1]
    reverse_is_suffix = is_suffix[::-1]
    answer = 0
    if reverse_is_suffix in reverse_my_string:
        if reverse_is_suffix[0] == reverse_my_string[0]:
            answer = 1
    return answer