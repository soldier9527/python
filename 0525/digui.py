def digui(n):
    if n==1:
        return 1
    return n* digui(n-1)

print(digui(3))
print(digui(100))
# print(digui(1000))

def digui2(n):
    return degui_fact(n,1)


def degui_fact(n,product):
    if n==1:
        return product
    return degui_fact(n-1,n * product)

print(digui2(100))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

fact(100)