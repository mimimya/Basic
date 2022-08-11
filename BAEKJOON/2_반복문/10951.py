import sys

lines = sys.stdin.readlines()
for line in lines:
    A, B = map(int, line.split())
    print(A+B)

#또는
#while True:
#  try:
#    A, B = map(int, stdin.readline().split())
#    print(A+B)
#  except:
#    break
