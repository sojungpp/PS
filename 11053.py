N = int(input())
numList = list(map(int, input().split()))
result = [1]*N

for i in range(N):
    for j in range(i):
        if numList[i] > numList[j]:
            result[i] = max(result[i], result[j]+1)

print(max(result))