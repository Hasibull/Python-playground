tc = int(input())  # Taking test case number

while tc > 0:
    n = int(input())  # Taking the array size
    values = input()  # Taking array values
    values = values.split()
    values = [int(val) for val in values]
    
    values.sort()

    ans = -1

    for i in range(len(values)-1):
        if values[i+1] > values[i]:
            ans = i+1
            break
    if ans == -1:
        print('0')
    else:
        print(n-ans)
    tc -= 1