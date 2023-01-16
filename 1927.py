import heapq, sys
input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq, x)
