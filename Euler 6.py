# Find sum square difference of first 100 nat. numbers
sum_square_num = 0
sum_num = 0
for i in range(1, 101):
    sum_square_num += i ** 2
    sum_num += i
print(sum_num ** 2 - sum_square_num)
