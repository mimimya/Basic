from sys import stdin
T = input()
for _ in range(T):
   A, B = map(int, stdin.readline().split())
   print(f"Case #%d: %d"%(_+1, A+B))
