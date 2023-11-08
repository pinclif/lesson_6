def gcd_numbers(x, y):
    if(y == 0):
        return x
    else:
        return gcd_numbers(y, x % y)
x = int(input('Enter the first number:'))
y = int(input('Enter the second number:'))
num = gcd_numbers(x, y)
print('GCD numbers:',num)