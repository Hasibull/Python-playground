tc = int(input())  # Taking test case number

while tc > 0:
    values = input()  # Taking n and k
    values = values.split()
    n = int(values[0])
    k = int(values[1])

    ans = 0

    if n > k:
        if n % k == 0:
            val = int(n / k)
            k *= val
        else:
            val = int(n / k) + 1
            k *= val

        if k % n == 0:
            ans = int(k / n)
        else:
            ans = int(k / n) + 1
    else:
        if k % n == 0:
            ans = int(k / n)
        else:
            ans = int(k / n) + 1

    print(ans)
    tc -= 1
