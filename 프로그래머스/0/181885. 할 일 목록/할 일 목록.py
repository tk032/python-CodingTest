def solution(todo_list, finished):
    answer = []
    for index, i in enumerate(finished):
        if not i:
            answer.append(todo_list[index])
    return answer