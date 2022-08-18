# 2606 - 바이러스
# BFS
from collections import deque
import sys
read = sys.stdin.readline

computer = int(read())
links = int(read())

# 네트워크 연결과 방문확인
link = [[] for _ in range(computer+1)]
visited = [False for _ in range(computer+1)]

# 네트워크 연결 추가
for i in range(links):   
    x, y = map(int, read().split())
    link[x].append(y)
    link[y].append(x)

# 1과 연결된 모든 컴퓨터 방문(bfs)
queue = deque([1])
visited[1] = True
count = 0 
while queue:
    q = queue.popleft()
    for i in link[q]:
        if not visited[i]:
            count += 1               
            queue.append(i)
            visited[i] = True

print(count)