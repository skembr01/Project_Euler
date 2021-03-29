# Find the sum of all even values in Fibonnaci Sequence, for values <= 4000000
fib_list = [0, 1, 2]
while fib_list[-1] + fib_list[-2] <= 4000000:
    fib_list.append(fib_list[-1] + fib_list[-2])
count = 0
for element in fib_list:
    if element % 2 == 0:
        count += element
print(count)
