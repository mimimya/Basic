from sys import stdin
min = 100
max = 0
for i in range(9):
  N = int(stdin.readline())
  if max < N:
    max = N
    max_i = i
print(max)
print(max_i+1)
