N = input()
cycle = 0
Num = N

while True:
    if int(N) < 10: #주어진 수가 10 보다 작다면
        N = '0' + N # 앞에 0을 붙여 두 자리 수로 만들고
  #각 자리의 숫자를 더한다.
    str_sum = 0
    for _ in N:
        str_sum += int(_)
    #주어진 수의 가장 오른쪽 자리 수와 앞서 구한 합의 가장 오른쪽 자리 수를 이어 붙인 새로운 수
    N = N[-1:] + str(str_sum)[-1:]
    cycle +=1
    if int(Num) == int(N) :
        break
print(cycle)
