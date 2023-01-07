tc = int(input())  # taking the test case number

while tc > 0:
    n = int(input())  # taking the length of the string
    arr = input()
    arr = arr.split()
    arr = [int(val) for val in arr]
    smallest = 100

    for i in range(n):
        val = arr[i]
        if smallest > val:
            smallest = val
        arr.append(val)

    if smallest == arr[0]:
        print('YES')
    else:
        print('NO')
    tc -= 1
