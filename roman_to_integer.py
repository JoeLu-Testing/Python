def roman_to_integer(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_numeral)):
        current_value = roman_values[roman_numeral[i]]

        if i + 1 < len(roman_numeral) and roman_values[roman_numeral[i + 1]] > current_value:
            result -= current_value
        else:
            result += current_value
        
    return result

numeral = 'XXIV'
integer = roman_to_integer(numeral)
print(integer)
