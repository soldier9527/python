
def test(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        b = a+b
        a= b
        n = n+1
    
t = test(3)
print(next(t))
print(next(t))
print(next(t))