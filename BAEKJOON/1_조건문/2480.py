global same
same = 0

a,b,c = map(int, input().split())
def is_same(a,b):#같은 눈이 나오는지 확인하고 같은 눈을 저장하는 함수
  global same
  if a==b:
    same = a
    return 1 # !=0 is true
  else:
    return 0 # false

if is_same(a,b) or is_same(b,c) or is_same(c,a): # 같은 눈이 두개 이상인 경우
  prize = 1000+same*100
  if a == b == c : # 모두 같은 눈이 나올 경우
    prize = 10000+a*1000   
else : # 모두 다른 눈이 나올 경우
  #최댓값 찾기
  if a>b: # a-b
    if a>c: # a-b-c or a-c-b
      max = a
  else: # b-a
     if b>c: # b-a-c of b-c-a
       max = b
  if c>b: # c-b
    if c>a: # c-a-b or c-b-a
      max = c
  prize = max * 100

print(prize)
