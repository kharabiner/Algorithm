def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    for word in goal:
        print(word)
        if cards1 and cards1[0] == word:
            cards1.pop(0)
        elif cards2 and cards2[0] == word:
            cards2.pop(0)
        else:
            answer = 'No'
            break
    
    return answer