not_self_number_list = []
for n in range(1, 10001):
  #d(n):
  for digit in str(n):
    n+=int(digit)
  #d(n)의 n은 생성자이므로 d(n)의 값은 셀프넘버가 아님
  not_self_number_list.append(n)

self_number_list = set(range(1,10001)) - set(not_self_number_list)

#셀프넘버를 출력함
for _ in sorted(self_number_list):
  print(_)
