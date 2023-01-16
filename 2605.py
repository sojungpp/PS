import sys
input = sys.stdin.readline
result = []
N = int(input())
num = list(map(int, input().split()))

for i in range(N):
    x = num[i]
    if i == 0:
        result.insert(0, i+1)
    else:
        result.insert(i-x, i+1)

print(*result)

