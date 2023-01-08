N = int(input())
w = [int(input()) for _ in range(N)]
result = []
w.sort(reverse=True)

for i in range(N):
    result.append(w[i]*(i+1))

print(max(result))

