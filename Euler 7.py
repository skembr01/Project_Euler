# Find the 10001st prime digit
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
for i in range(25, 2000000, 2):
    count = 0
    for num in prime_list:
        if i % num != 0:
            count += 0
        elif i % num == 0:
            count += 1
    if count < 1:
        prime_list.append(i)
count = 0
for value in prime_list:
    count += value
print(prime_list)
print(len(prime_list))
print(prime_list[10000])
