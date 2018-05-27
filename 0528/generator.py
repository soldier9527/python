
g = (x * x for x in range(5))
print(g)

for x in g:
    print(x)

def fib (max):
    n,a,b= 0,0,1
    while n< max:
        yield b
        n += 1
        b = a+ b
        a = b
    return print("done")

fib(3)

def yieldTest():
    print("yield")
    yield 1
    print("yield1")
    yield 3
    print("yield3")
    yield 2
    print("yield2")


o = yieldTest()
next(o)
next(o)
next(o)


def fib2 (max):
    n,a,b= 0,0,1
    while n< max:
        n += 1
        b = a+ b
        a = b
        return b

f = fib(4)
try:
    fn = next(f)
except StopIteration as e:
    print("generator return",e.value)
    # print("generator return")
