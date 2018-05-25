h = input("input your height(m): ")
w = input("input your weight(kg): ")
height = float(h)
weight = float(w)
bmi = weight /(height*height)
print(bmi)
if bmi <18.5:
    print("too light")
elif bmi <25:
    print("normal")
elif bmi <28:
    print("too fat")
elif bmi <32:
    print("tooooooo fat")
else:
    print("suprise!!!you are the fatest ")