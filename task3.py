def num_prost(q):
    if q < 2:
        return False
    for i in range(2, int(q ** 0.5 + 1)):
        if q % i == 0:
            return False
    else:
        return True
print(num_prost(int(input('Enter the number:'))))