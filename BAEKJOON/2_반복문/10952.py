import sys
A, B = map(int, input().split())
while A:
    print(A+B)
    A, B = map(int, sys.stdin.readline().split())
