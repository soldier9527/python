i = {
    2:"sdf",
    "3":"dsfsf",
    "oo":"1"
}
for t in i:
    print(t)


for index,item in i.items():
    print(index,' ',item)

l = [1,2,44,443]
for index,item in enumerate(l):
    print(index, ' ',item)

for x,y,z in [(1,2,3),(3,2,1),(4,5,6)]:
    print(x, " ",y," ",z)