import sympy

T = int(input())
x3, y3 = sympy.symbols('x3 y3') ##2개의 미지수
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split());
    expr1 = sympy.Eq(math.pow(x1-x3)+math.pow(y1-y3), r1**2)
    expr2 = sympy.Eq(math.pow(x2-x3)+math.pow(y2-y3), r2**2)
    sol = solve((expr1, expr2))
    print(sol)


