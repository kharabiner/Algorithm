def solution(str1, str2):
    string_list = []
    
    for s1, s2 in zip(str1, str2):
        string_list.append(s1)
        string_list.append(s2)
        
    answer = ''.join(string_list)
    return answer


