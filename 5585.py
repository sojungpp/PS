total = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
result = 0

while total !=0:
    for m in money:
        result += total // m
        total %= m

print(result)
