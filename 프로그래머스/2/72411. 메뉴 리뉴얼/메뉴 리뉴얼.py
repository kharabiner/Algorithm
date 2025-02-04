from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    count = defaultdict(int)
    for i in range(len(orders)):
        for j in range(i + 1, len(orders)):
            abc = {chr(x):0 for x in range(65, 91)}
            for char in orders[i]:
                abc[char] += 1
            for char in orders[j]:
                abc[char] += 1
            key_string = ''.join([key for key, value in abc.items() if value == 2])
            
            for length in course:
                for combo in combinations(key_string, length):
                    combo_str = ''.join(combo)
                    count[combo_str] += 1 
    
    print(count)
    
    for c in course:
        filtered_items = {k: v for k, v in count.items() if len(k) == c}
        if filtered_items:
            max_value = max(filtered_items.values())
            for k, v in filtered_items.items():
                if v == max_value:
                    answer.append(k)
    
    
    answer = sorted(answer)
    
    return answer


