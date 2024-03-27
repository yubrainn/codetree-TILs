from collections import deque
n, m = map(int, input().split())

graph = {i:set([]) for i in range(1, n+1)}
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)

def bfs(node):
    que = deque([node])
    visited = set()
    while que:
        n = que.popleft()
        if n in visited:
            continue
        visited.add(n)
        que += graph[n] - visited
        # print(que)
    
    return visited

print(len(bfs(1))-1)