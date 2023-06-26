def reverse_integer(num):
    negative = False
    if num < 0:
        negative = True
        num = abs(num)

    reversed_num = 0
    while num != 0:
        last_digit = num % 10
        reversed_num = (reversed_num * 10) + last_digit
        num = num // 10

    if negative:
        reversed_num *= -1

    if reversed_num < -2**31 or reversed_num > (2**31 - 1):
        return 0
    
    return reversed_num

num = 123
reversed_num = reverse_integer(num)
print(reversed_num)
