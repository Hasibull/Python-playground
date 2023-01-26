weight = int(input())  # Taking the weight

if weight % 2 == 0:
    if (weight - 2) % 2 == 0 and weight > 2:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
