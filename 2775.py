T = int(input())
result = []
for i in range(T):
    k = int(input())
    n = int(input())
    people = list(range(1, n+1)) #1~n까지 people 리스트에 추가 (0층은 i호수 i명)

    for j in range(k): #k층만큼 반복
        for l in range(1, n): #1~n-1까지 사람 수 더해주기
            people[l] += people[l-1]

    print(people[-1])





