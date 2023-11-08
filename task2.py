def func(number, scale):
    if scale > number:
        return str(number)
    return func(number // scale, scale) + str(number % scale)

a = int(input())
print(func(a, 2))