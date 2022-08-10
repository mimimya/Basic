score = int(input())
result = 'F'

if score > 59 :
  result = 'D'
if score > 69:
  result = 'C'
if score > 79:
  result = 'B'
if score > 89:
  result = 'A'
  
print(result)
  
