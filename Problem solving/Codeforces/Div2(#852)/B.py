tc = int(input())  # Taking the test case

while tc > 0:
    ab = input()
    ab = ab.split()
    ab = [int(val) for val in ab]

    print(int((abs(ab[0]) + abs(ab[1])) * 2))

    for i in range(abs(ab[1])):
        if ab[1] > 0:
            print('0 1', sep='', end=' ')
        else:
            print('0 -1', sep='', end=' ')

    for i in range(abs(ab[0])):
        if ab[0] > 0:
            print('0 1', sep='', end=' ')
        else:
            print('0 -1', sep='', end=' ')

    print()

    tc -= 1
