from sys import stdin

C = int(input())

for i in range(C):
  buffer = list(map(int, stdin.readline().split()))
  N = buffer[0]
  final_grade = buffer[1:]

  avg = sum(final_grade)/N
  count = 0

  for x in final_grade:
    if x> avg:
      count += 1
      
  print("%0.3f%%"%(count/N * 100))
