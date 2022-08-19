N = int(input())
count_of_seq = 0

for i in range(1,N+1):
  digit =  [int(c) for c in str(i)]

  if len(digit) == 4:
    if digit[1] - digit[0] == digit[2] - digit[1] == digit[3] - digit[2]:
      count_of_seq += 1
  elif len(digit) == 3:
    if digit[1] - digit[0] == digit[2] - digit[1]:
      count_of_seq += 1
  else: # len is 1 or 2
    #len 1 : Vacuous truth
    #len 2 : common difference of AP is ±n (n: 1 digit number)
    count_of_seq +=1

print(count_of_seq)
