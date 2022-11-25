tc = int(input())

cnt = 0

while(cnt < tc):
    n = int(input())

    a = input()
    a = a.split()
    a = [int(val) for val in a]

    b = input()
    b = b.split()
    b = [int(val) for val in b]

    ans = 0

    while(len(b) > 0):
        val = min(b)

        for i in range(len(b)):
            if b[i] == val:
                ans += a[i]
                a.remove(a[i])
                b.remove(b[i])
    
    print(ans)
    cnt += 1

        

    
                
