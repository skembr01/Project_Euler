# # Find Pythagorean triplet for which a + b + c = 1000, find a*b*c
# # basic triplet = (3,4,5)
ab_list = []
a_value = 2
b_value = 1
c_value = 3
for i in range(1, 100):
    a_value += 1
    b_value += 1
    c_value += 1
    a_mul = a_value * i
    b_mul = b_value * i
    c_mul = c_value * i
    print(a_mul + b_mul + c_mul)
