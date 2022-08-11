import sys
N = int(sys.stdin.readline())
for x in range(N):
  for i in range(x+1):
    print('*',end = '')
  print()
