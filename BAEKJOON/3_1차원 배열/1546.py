N = int(input())
subject = list(map(int, input().split()))
M = max(subject)
i = 0
sum = 0
for x in subject:
  sum+= x/M*100
  i+=1
print(sum/N)
