from collections import deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = deque([source])
        visited = [False] * n
        visited[source] = True
        
        while queue:
            curr = queue.popleft()
            
            if curr == destination:
                return True
                
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    
        return False
        