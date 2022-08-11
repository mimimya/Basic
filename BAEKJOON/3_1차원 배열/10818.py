N = int(input())
Ns = list(map(int, input().split()))
max = min = Ns[0]
for x in Ns:
  if max < x: max = x
  elif min > x : min = x
print(min, max)
