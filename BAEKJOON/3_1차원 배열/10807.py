import sys
N = int(sys.stdin.readline())

#map(int, list)
numbers = [int(x) for x in sys.stdin.readline().rstrip().split()]

lookingfor = int(sys.stdin.readline().rstrip())

count = 0
for n in numbers:
    if n == lookingfor: count +=1
print(count)
