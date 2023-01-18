tc = int(input())  # Taking the test case number

while tc > 0:
    n = int(input())  # taking the array size
    arr = input()  # taking the array
    arr = arr.split()
    arr = [int(i) for i in arr]

    odd = 0
    even = 0

    for val in arr:
        if val % 2 == 0:
            even += 1
        else:
            odd += 1

    if even == odd:
        print('Yes')
    else:
        print('No')
    tc -= 1
