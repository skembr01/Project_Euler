# Largest Palindromic product of 2 three-digit numbers
new_list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        mult_value = i * j
        new_list.append(str(mult_value))
pal_list = []
for element in new_list:
    if element[-1] == element[0] and element[-2] == element[1] and element[-3] == element[2]:
        pal_list.append(int(element))
pal_list.sort()
print(pal_list[-1])
