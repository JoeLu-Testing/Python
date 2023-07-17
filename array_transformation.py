def transform_array(a):
    length = len(a)
    b = [0] * length

    for i in range(length):
        if i == 0:
            b[i] = 0 + a[i] + (a[i + 1] if length > 1 else 0)
        elif i == length - 1:
            b[i] = (a[i - 1] if length > 1 else 0) + a[i] + 0
        else:
            b[i] = a[i - 1] + a[i] + a[i + 1]

    return b

a = [1, 2, 3, 4, 5]
b = transform_array(a)
print(b)