from sys import stdin
T = int(input())

for i in range(T):
  ot_test = stdin.readline() #개행문자
  print(ot_test)
  tmp_score = 0
  result = 0
  for ox in ot_test:
    if ox == 'O':
      tmp_score +=1
      result += tmp_score
    else :
      tmp_score = 0
  print(result)
