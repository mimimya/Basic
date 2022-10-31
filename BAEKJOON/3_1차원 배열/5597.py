import sys
submited = []
for i in range(28):
    submited.append(int(sys.stdin.readline())) 

noHanded = [student for student in range(1,31) if student not in submited]

for x in noHanded:
    print(x)
