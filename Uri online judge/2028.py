
from os import sep

cs = 1

while True:
    try : 
        n = int(input())

        ans = int((n*(n+1))/2)
        ans = ans + 1

        if ans == 1:
            print("Caso %d: %d numero" %(cs, ans), sep="", end="\n")
        else:
            print("Caso %d: %d numeros" %(cs, ans), sep="", end="\n")
        
        if ans == 1:
            print("0", sep="", end="\n")
        else:
            print("0 ", sep="", end="")

        cnt = 2

        for i in range(1, n+1):
            for j in range(0, i):
                if cnt == ans:
                    print(i, sep="", end="\n")
                else:
                    print(i, sep="", end=" ")
                cnt += 1
        print("")
        cs += 1
    except EOFError:
        break;


