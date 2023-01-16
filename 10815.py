import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))
M = int(input())
standard = list(map(int, input().split()))

for i in standard:
    if i in cards:
        print(1, end = " ")
    else:
        print(0, end = " ")
