tc = int(input())  # Taking test case number

while tc > 0:
    n = int(input())

    if n == 1:
        print('2')
    else:
        ans = 0

        while n % 3 != 0:
            n -= 2
            ans += 1

        if n > 0:
            ans += int(n / 3)
            print(ans)
        else:
            print(ans)
    tc -= 1
