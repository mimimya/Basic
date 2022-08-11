from sys import stdin
T = int(input())
for x in range(T):
    A,B = map(int, stdin.readline().split())
    print(f"Case #%d: %d + %d = %d"%(x+1, A, B, A+B))
