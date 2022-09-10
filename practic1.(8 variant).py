import math


def result(n,k):
    res = math.factorial(n-k)
    return res

n = int(input("n = "))  # Розмір послідовності
k = int(input("k = "))  # Нерухомі точки


print('Result :', result(n,k))