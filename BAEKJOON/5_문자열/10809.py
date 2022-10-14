import sys

alpabet = [chr(i) for i in range(97,123)] #abcd...xyz

S = list(sys.stdin.readline().rstrip())

for a in alpabet:
    location_of_a = -1
    if a in S:
            location_of_a = S.index(a) 
    print(location_of_a,end=' ')
