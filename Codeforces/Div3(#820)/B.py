tc = int(input())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while tc > 0:
    sz = int(input())
    code = input()
    i = len(code) - 1

    val = 0
    ans = ""

    while i >= 0:
        if code[i] == '0':
            val += int(code[i-2])
            val *= 10
            val += int(code[i-1])
            i -= 3
        else:
            val += int(code[i])
            i -= 1

        ans += letters[val-1]
        val = 0
    ans = ans[::-1]
    print(ans)
    tc -= 1

    """
        At I consider iteration from left to right on the string
    """
    # while i < (len(code)):
    #     if((i + 2) < (len(code) - 1)):
    #         if code[i] < '3':
    #             if code[i+1] == '0' and code[i+2] == '0':
    #                 val += int(code[i])
    #                 val *= 10
    #                 val += int(code[i+1])
    #                 i += 3
    #             elif code[i+1] != '0' and code[i+2] == '0':
    #                 if (i + 3) <= (len(code) - 1):
    #                     if code[i+3] == '0':
    #                         val += int(code[i])
    #                         i += 1
    #                     else:
    #                         val += int(code[i])
    #                         val *= 10
    #                         val += int(code[i+1])
    #                         i += 3
    #         else:
    #             val += int(code[i])
    #             i += 1
    #     else:
    #         val += int(code[i])
    #         i += 1
        
    #     print(letters[val-1], sep='', end='')
    #     val = 0
