def solution(strArr):
    answer = []
    ad_index = []
    for index, i in enumerate(strArr):
        if 'ad' in i:
            ad_index.append(index)
    for index, i in enumerate(strArr):
        if index not in ad_index:
            answer.append(i)
    
    return answer