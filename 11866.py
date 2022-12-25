from collections import deque

N, K = map(int, input().split())
result = []
q = deque()
for i in range(1, N+1):
    q.append(i)

while q: #q가 비어있지 않다면
    for i in range(1, K):
        q.append(q.popleft()) #K번쨰 아니라면 다시 넣고
    result.append(q.popleft()) #K번째 맞으면 큐에서 없애기

print("<",end='')
for i in range(len(result)-1):
    print("%d, "%result[i], end='')
print(result[-1], end='')
print(">")