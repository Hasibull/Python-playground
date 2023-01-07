tc = int(input()) # taking the test case number

while tc > 0:
    n = input() # taking the range as string

    extreme_round = int(n[0]) + ((len(n)-1) * 9) # applying the formula

    print(extreme_round)
    tc -= 1