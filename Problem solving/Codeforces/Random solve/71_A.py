tc = int(input())  # taking the test case number

while tc > 0:
    word = input() # taking the word

    if len(word) > 10: # checking the length
        final_word = word[0] + str(len(word)-2) + word[len(word)-1]
        print(final_word)
    else:
        print(word)
    tc -= 1
