val = input() # Taking the house number and the number of task
val = val.split()
n = int(val[0])
m = int(val[1])

destinations = input() # taking the destination house numbers where the task is
destinations = destinations.split()
destinations = [int(val) for val in destinations]

current_position = 1
total_time = 0

for destination in destinations:
    if destination >= current_position:
        total_time += (destination - current_position)
    else:
        total_time += ((n - current_position) + 1 + (destination - 1))
        
    current_position = destination

print(total_time)
