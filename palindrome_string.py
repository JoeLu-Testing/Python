def is_palindrome(string):
    cleaned_str = ''.join(ch.lower() for ch in string if ch.isalnum())
    reversed_str = cleaned_str[::-1]
    return cleaned_str == reversed_str

string1 = "hello"
print(is_palindrome(string1))

string2 = "racecar"
print(is_palindrome(string2))
