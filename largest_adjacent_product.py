def solution(input):
    max_product = float('-inf')

    for i in range(len(input) - 1):
        product = input[i] * input[i + 1]
        if product > max_product:
            max_product = product
    
    return max_product

input = [3, 6, -2, -5, 7, 3]
print(solution(input))
