import math

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt(pow((x1-x2),2)+pow((y1-y2),2)) # sqrt = 루트, pow = 제곱 (a**b = a^2와 동일), 점 사이 거리
    if d == 0 and r1==r2: # 같은 원 (겹치는 점 무한)
        print(-1)
    elif d == abs(r1-r2) or d == r1+r2: # 내접 / 외접 (겹치는 점 1개)
        print(1)
    elif abs(r1 - r2) < d < (r1+r2): # 겹치는 점 2개
        print(2)
    else:
        print(0)

