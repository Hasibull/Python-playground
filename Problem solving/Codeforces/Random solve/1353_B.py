tc = int(input())  # Taking the test case number

while tc > 0:
    val = input()  # Taking the array size and exchange number
    val = val.split()
    n = int(val[0])
    k = int(val[1])

    a = input()  # taking array a
    a = a.split()
    a = [int(i) for i in a]

    b = input()  # taking array b
    b = b.split()
    b = [int(i) for i in b]

    a.sort()  # sorting in ascending order
    b.sort(reverse=True)  # sorting in descending order

    for i in range(k):
        for j in range(len(b)):
            if a[i] < b[j]:
                temp = a[i]
                a[i] = b[j]
                b[j] = temp
                break

    print(sum(a))
    tc -= 1