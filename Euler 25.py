# find the index of first 1000 digit fibonnaci number, where index counting starts at f(1) = 1, f(2) = 1
fib_list = [1,1]
index_count = 2
while len(str(fib_list[-1])) < 1000:
    fib_list.append(fib_list[-1] + fib_list[-2])
    index_count += 1
print(index_count)
