tc = int(input())  # taking the test case number

while tc > 0:
    n = int(input())  # taking the length of the string
    msg = input()
    ck = 0

    for i in range(len(msg)-1):
        for j in range(i+2, len(msg)-1):
            if msg[i] == msg[j]:
                if msg[i+1] == msg[j+1]:
                    ck = 1
                    break

        if ck == 1:
            break

    if ck == 1:
        print('YES')
    else:
        print('NO')
    tc -= 1
