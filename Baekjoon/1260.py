# 1260 - DFS와 BFS
from collections import deque
import sys

# DFS
d_visited = []
def dfs(n):
    d_visited.append(n)
    # 방문하지 않은 정점인 경우 방문
    for i in graph[n]:
        if i not in d_visited:
            dfs(i)
            
# BFS
b_visited = []
def bfs(n):
    queue = deque([n])
    b_visited.append(n)
    
    while queue:
        q = queue.popleft()
        # 방문하지 않은 정점인 경우 방문 후 큐에 추가
        for i in graph[q]:
            if i not in b_visited:               
                queue.append(i)
                b_visited.append(i)
     
                
node, edge, start = map(int, sys.stdin.readline().split())

# 그래프
graph = [[] for i in range(node+1)]

# edge 입력
for i in range(edge):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
# 정점 번호가 작은순으로 정렬
for i in graph:
    i.sort()
            
dfs(start)
print(*d_visited)
bfs(start)
print(*b_visited)
