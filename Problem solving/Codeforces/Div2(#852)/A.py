tc = int(input())  # Taking the test case

while tc > 0:
    ab = input()
    ab = ab.split()
    ab = [int(val) for val in ab]
    nm = input()
    nm = nm.split()
    nm = [int(val) for val in nm]

    if nm[1] > nm[0]:
        if (nm[0] * ab[0]) > (nm[0] * ab[1]):
            print(nm[0] * ab[1])
        else:
            print(nm[0] * ab[0])
    else:
        if (nm[1] * ab[0]) > ((nm[1] + 1) * ab[1]):
            print(nm[0] * ab[1])
        else:
            price = int(nm[0] / (nm[1] + 1)) * (nm[1] * ab[0])
            rst = nm[0] - ((int(nm[0] / (nm[1] + 1))) * (nm[1] + 1))
            if (rst * ab[0]) > (rst * ab[1]):
                print((rst * ab[1]) + price)
            else:
                print((rst * ab[0]) + price)
        pass

    tc -= 1
