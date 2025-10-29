def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(current_node):
        
        visited[current_node] = True
        
        for neighbor in range(n):
            if computers[current_node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    for i in range(n):
        if not visited[i]:
            dfs(i)       
            answer += 1 
            
    return answer