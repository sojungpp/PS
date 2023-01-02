T = int(input())

def prime(num):  # 소수 여부 구하기
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(T):
    num = int(input())
    a = num // 2 # 중앙 값부터 구하기 (최소 차 구하려고)
    b = num // 2

    while a>0 and b<num:
        if prime(a) and prime(b): # 소수 여부 체크
            print(a, b)
            break
        else:
            a = a-1
            b = b+1
