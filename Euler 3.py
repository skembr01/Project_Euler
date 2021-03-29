# # find the largest prime factor of 600851475143
factor_list = []
for i in range(1, 9000000, 2):
    if i % 2 != 0 and i % 4 != 0 and 6857 % i == 0:
        factor_list.append(i)
print(factor_list)
new_variable = 5753023 / 6857
print(new_variable)
