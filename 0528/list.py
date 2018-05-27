print(list(range(1, 22)))

print([x*x for x in range(1, 22)])

print([x + x for x in range(0, 10) if x % 2 == 0])


import os

print([o for o in os.listdir('.')])
