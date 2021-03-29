# Find smallest positive number that is evenly divisible by all numbers from 1 to 20
def smallest_pos(num_list):
    number_list = []
    for num in num_list:
        if num % 11 == 0 and num % 13 == 0 and num % 15 == 0 and num % 17 == 0 and num % 19 == 0:
            number_list.append(num)
    number_list2 = []
    for number in number_list:
        if number % 12 == 0 and number % 14 == 0 and number % 16 == 0 and number % 18 == 0 and number % 20 ==0:
            number_list2.append(number)
    return number_list2

print(smallest_pos(range(20, 900000000, 2)))
