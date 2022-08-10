from sys import stdin
X = int(stdin.readline())
N = int(stdin.readline())

sum = 0
for i in range(N):
    a,b =  map(int,stdin.readline().split())
    sum += a*b

if sum == X :
    print('Yes')
else:
    print('No')
