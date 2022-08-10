H, M = map(int, input().split())
cook_m = int(input())

M += cook_m
if M>59:
    H += int(M/60)
    M = M%60

if H > 23:
    H = H%24

print(H, M)
