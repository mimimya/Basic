H, M = map(int,input().split())

m = M - 45

if m <0:
  H -= 1 # 이전 시간
  m = m%60 #음수 나머지 양수로 나옴

if H < 0 :
    H += 24 #시간이 양수로 나오도록 함
print(H, m)
