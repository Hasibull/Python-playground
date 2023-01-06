tc = int(input()) # taking the number of test case

while tc > 0:
    n = int(input()) # taking the size of the sequence
    a = input() # taking input sequence of 0 and 1

    ans = int(a[0]) # assigning 1st character to the variable ans as integer
    seq = '' # empty variable for containing the sign sequence

    for i in range(1, len(a)):
        if (ans - int(a[i])) >= 0:
            seq += '-'
            ans -= int(a[i]) # updating the value of the variable after each operation
        else:
            seq += '+'
            ans += int(a[i]) # updating the value of the variable after each operation

    print(seq)
    tc -= 1