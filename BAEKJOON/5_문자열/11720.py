import sys
N = int(input())
sum = 0

for i in range(N):
    sum += int(sys.stdin.read(1))
print(sum)
