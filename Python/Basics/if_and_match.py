age = int(input('Enter your age: '))

if age > 18:
    print('You are not allow!! :)')
else:
    print('Welcome here')


name = input('Enter you name: ').capitalize()

match name:
    case "Chowdhury shaheb":
        print('You are not allow!')
    case "Khan shaheb":
        print('Welcome Khan shaheb')
    case _:
        print('Who are you gorib\'s?')
