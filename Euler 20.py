#find sum of digits of in 100!

def factorial(num):
    num_list = list(range(num + 1))
    num_list.pop(0)
    num_list = list(reversed(num_list))
    factorial_val = 1
    for val in num_list:
        factorial_val *= val
    factorial_val = str(factorial_val)
    digit_val = 0
    for digit in factorial_val:
        digit_val += float(digit)
    return digit_val
print(factorial(100))

