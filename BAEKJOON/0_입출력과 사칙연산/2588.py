A, B, C = map(int, input())
a, b, c = map(int, input())

first = 0
second = 0
third = 0

first += c*C
first += c*B*10
first += c*A*100

print(first)

second += b*C
second += b*B*10
second += b*A*100
print(second)

third += a*C
third += a*B*10
third += a*A*100
print(third)

result = 0
result = first + second*10 + third*100
print(result)
