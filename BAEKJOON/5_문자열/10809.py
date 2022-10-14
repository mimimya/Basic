import sys
S = (sys.stdin.readline())

alpabet = [-1 for i in range(26)]

for (i,a) in enumerate(S):
    if a == 'a':
        if alpabet[0] == -1:
            alpabet[0] = i
    elif a == 'b':
        if alpabet[1] == -1:
            alpabet[1] = i
    elif a == 'c':
        if alpabet[2] == -1:
            alpabet[2] = i
    elif a == 'd':
        if alpabet[3] == -1:
            alpabet[3] = i
    elif a == 'e':
        if alpabet[4] == -1:
         alpabet[4] = i
    elif a == 'f':
        if alpabet[5] == -1:
            alpabet[5] = i
    elif a == 'g':
        if alpabet[6] == -1:
            alpabet[6] = i
    elif a == 'h':
        if alpabet[7] == -1:
            alpabet[7] = i
    elif a == 'i':
        if alpabet[8] == -1:
            alpabet[8] = i  
    elif a == 'j':
        if alpabet[9] == -1:
            alpabet[9] = i
    elif a == 'k':
        if alpabet[10] == -1:
            alpabet[10] = i
    elif a == 'l':
        if alpabet[11] == -1:
            alpabet[11] = i
    elif a == 'm':
        if alpabet[12] == -1:
            alpabet[12] = i
    elif a == 'n':
        if alpabet[13] == -1:
            alpabet[13] = i
    elif a == 'o':
        if alpabet[14] == -1:
            alpabet[14] = i
    elif a == 'p':
        if alpabet[15] == -1:
            alpabet[15] = i
    elif a == 'q':
        if alpabet[16] == -1:
            alpabet[16] = i
    elif a == 'r':
        if alpabet[17] == -1:
            alpabet[17] = i
    elif a == 's':
        if alpabet[18] == -1:
            alpabet[18] = i
    elif a == 't':
        if alpabet[19] == -1:
            alpabet[19] = i
    elif a == 'u':
        if alpabet[20] == -1:
            alpabet[20] = i
    elif a == 'v':
        if alpabet[21] == -1:
            alpabet[21] = i
    elif a == 'w':
        if alpabet[22] == -1:
            alpabet[22] = i
    elif a == 'x':
        if alpabet[23] == -1:
            alpabet[23] = i
    elif a == 'y':
        if alpabet[24] == -1:
            alpabet[24] = i
    elif a == 'z':
        if alpabet[25] == -1:
            alpabet[25] = i

for x in alpabet:
    print(x, end=' ')
  
