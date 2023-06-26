def get_century(year):
    century = (year + 99) // 100
    return century

year = 2023
century = get_century(year)
print(century)
