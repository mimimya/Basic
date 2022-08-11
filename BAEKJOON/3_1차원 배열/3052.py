from sys import stdin
distinct = []
for i in range(10):
  A = int(stdin.readline())%42
  if A not in distinct:
    distinct.append(A)
print(len(distinct))
