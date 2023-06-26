def is_palindrome(num):
    if num < 0:
        return False
    
    reverse = 0
    original = num
    while num > 0:
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = num // 10

    if original == reverse:
        return True
    else:
        return False
    
print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))
