#find other 4digit prime in which when a number is added twice, it creates two additional prime numbers which are permutations of first number
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
for i in range(25, 9999, 2):
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
# print(prime_list)
four_prime = []
for value in prime_list:
    if len(str(value)) >= 4:
        four_prime.append(value)
print(four_prime)
print(9999 - 1000)
first_sum_list = []
for i in range(2, 8999, 2):
    for value in four_prime:
        new_sum = value + i
        if new_sum % 2 != 0 and four_prime.count(new_sum) >= 1:
            first_sum_list.append(value)
print(first_sum_list)
