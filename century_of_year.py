import math

def get_century(year):
    century = math.ceil(year / 100)
    return century

year = 2023
century = get_century(year)
print(century)
