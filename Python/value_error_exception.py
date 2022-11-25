try:
    money = float(input('Enter your budget: '))
    multiple = 1000.0 / money
except ValueError:
    print('Enter valid budget!')
except ZeroDivisionError:
    print('You are too poor!!')
else:
    print('you are rich!!')