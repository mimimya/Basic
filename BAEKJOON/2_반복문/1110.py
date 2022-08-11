N = int(input())
cycle = 0
Num = N
while True:
    # = N의 1의 자리를 10의 자리로, N의 각 자릿수 합의 1의자리를 1의자리로 하는 수
    N = (N%10)*10 + (N//10 + N%10) %10
    cycle +=1
    if (Num == N): break
print(cycle)
