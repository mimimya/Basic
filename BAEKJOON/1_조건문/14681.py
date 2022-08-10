x = int(input())
y = int(input())

quadrant = 0
if x == 0 or y == 0:
    quadrant = 0

if y>0 :
    if x>0:
        quadrant = 1
    else:
        quadrant = 2
else :
    if x<0:
        quadrant = 3
    else:
        quadrant = 4

print(quadrant)
