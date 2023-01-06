tc = int(input())  # Taking the test case

while tc > 0:
    # taking the value of k and n
    values = input()
    values = values.split()
    k = int(values[0])
    n = int(values[1])

    a = [1] # this will be the final list
    ct = 1

    for i in range(k-1):
        if (a[i]+ct) <= n and (n-(a[i]+ct)) >= (k-i-2):
            a.insert(i+1, a[i] + ct)
            ct += 1
        else:
            a.insert(i+1, a[i] + 1)
    
    for val in a:
        print(val, end=' ')
    print()

    tc -= 1

