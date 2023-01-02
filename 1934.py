def divisor(num):  # 약수 구하기
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


T = int(input())
for i in range(T):
    a, b = map(int, input().split())

    divisorA = divisor(a)
    divisorB = divisor(b)
    commonDivisor = list(set(divisorA).intersection(divisorB)) # 공약수
    maxDivisor = max(commonDivisor) # 최대공약수
    print(int(maxDivisor * a/maxDivisor * b/maxDivisor))