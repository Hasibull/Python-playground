import math

tc = int(input())

while tc > 0:
    lifts = input()

    lifts = lifts.split()
    lifts = [int(val) for val in lifts]

    # if (int(math.fabs(lifts[2] - lifts[1])) + int(math.fabs(lifts[2] - 1))) > int(math.fabs(lifts[0] - 1)):
    #     print('1')
    # elif (int(math.fabs(lifts[2] - lifts[1])) + int(math.fabs(lifts[2] - 1))) == int(math.fabs(lifts[0] - 1)):
    #     print('3')
    # else:
    #     print('1')

    if(lifts[2] < lifts[1]):
        if lifts[0] < lifts[1]:
            print('1')
        elif lifts[0] == lifts[1]:
            print('3')
        else:
            print('2')
    else:
        if ((lifts[2] - lifts[1]) + (lifts[2] - 1)) > (lifts[0] - 1):
            print('1')
        elif ((lifts[2] - lifts[1]) + (lifts[2] - 1)) == (lifts[0] - 1):
            print('3')
        else:
            print('2')
    
    tc -= 1