
def move(n, a, b, c):
    if n == 1:
        print(a, "==>", c)
        return
    move(n-1,a,c,b)
    print(a, "==>", c)
    move(n-1,b,a,c)
    return


move(1, "A", "B", "C")
print("=========")
move(3, "A", "B", "C")
