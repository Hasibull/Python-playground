
from os import sep

cs = 1

while True:
    try : 
        n = int(input())

        ans = int((n*(n+1))/2)
        ans = ans + 1

        if ans == 1:
            print("Caso ", cs, ": ", ans, " numero", sep="", end="\n")
        else:
            print("Caso ", cs, ": ", ans, " numeros", sep="", end="\n")
        
        if ans == 1:
            print("0", sep="", end="\n")
        else:
            print("0 ", sep="", end="")
            
        for i in range(1, n+1):
            for j in range(0, i):
                if i == n and j == i-1:
                    print(i, sep="", end="\n")
                else:
                    print(i, sep="", end= " ")
        cs = cs + 1
    except EOFError:
        break;


