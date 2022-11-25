number_of_card = int(input())
cards = input()

cards = cards.split()

cards = [int(val) for val in cards]
check = []
left = 0
right = len(cards)-1

s = 0
d = 0

term = 1

while left <= right:
    if cards[left] < cards[right]:
        if term % 2 == 1:
            s += cards[right]
        else:
            d += cards[right]
            
        right -= 1
        term += 1
    else:
        if term % 2 == 1:
            s += cards[left]
        else:
            d += cards[left]
        
        left += 1
        term += 1
    # if cards[left] < cards[right]:
    #     print('none')
    # elif cards[left] > cards[right]:
    #     if cards[left+1] > cards[right]:
    #         if term % 2 == 1:
    #             s += cards[right]
    #         else:
    #             d += cards[right]
            
    #         right -= 1
    #         term += 1
    #     else:
    #         if term % 2 == 1:
    #             s += cards[right]
    #         else:
    #             d += cards[right]
        
    #         term += 1
    #         left += 1

print(s, d)