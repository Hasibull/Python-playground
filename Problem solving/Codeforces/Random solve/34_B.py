values = input() # Taking the number of televesion for sale and bob ability
values = values.split()
n = int(values[0])
m = int(values[1])

prices = input() # Taking the prices of the televisions
prices = prices.split()
prices = [int(val) for val in prices]

prices.sort()

earn = 0

for i in range(m):
    if prices[i] >= 0:
        break
    else:
        earn += prices[i]

print(earn * -1)