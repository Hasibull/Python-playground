tc = int(input())

cnt = 0

while(cnt < tc):
    dmn = input()
    dmn = dmn.split()
    n = int(dmn[0])
    m = int(dmn[1])

    x = []
    y = []

    for i in range(m):
        dmn = input()
        dmn = dmn.split()
        x.append(int(dmn[0]))
        y.append(int(dmn[1]))

    ck = 0

    for i in range(m):
        if (x[i]-1) > 0:
            if (x[i]-1) in x:
                ck = 0
            else:
                ck = 1
                break
        if (x[i]+1) <= n:
            if (x[i]+1) in x:
                ck = 0
            else:
                ck = 1
                break
        if (y[i]-1) > 0:
            if (y[i]-1) in y:
                ck = 0
            else:
                ck = 1
                break
        if (y[i]+1) <= n:
            if (y[i]+1) in y:
                ck = 0
            else:
                ck = 1
                break
    
    if ck == 1:
        print('YES')
    else:
        print('NO')
    cnt += 1
                
