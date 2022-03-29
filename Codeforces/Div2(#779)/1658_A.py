tc = int(input())

while tc > 0:
    tc -= 1
    n = int(input())
    cosplay = input()
    ans = 0

    for i in range(len(cosplay)):
        if cosplay[i] == '0':
            if i+1 < len(cosplay) and cosplay[i+1] == '0':
                ans += 2
            elif i+1 < len(cosplay) and cosplay[i+1] == '1':
                if i+2 < len(cosplay) and cosplay[i+2] == '0':
                    ans += 1
                    i += 2
                
    print(ans)
