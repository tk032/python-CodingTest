def solution(myString, pat):
    answer = 0
    new = ''
    for i in myString:
        if i == "A":
            temp = "B"
        else:
            temp = "A"
        new += temp
    if pat in new:
        answer = 1
    return answer