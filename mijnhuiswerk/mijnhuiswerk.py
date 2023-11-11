print("Geef een getal: ")
getal1 = input()

print("Geef nog een getal: ")
getal2 = input()

print("Geef nog een getal: ")
getal3 = input()

if getal1 < getal2:
    if getal2 < getal3:
        print("het grootste getal is", getal3)
    else:
        print("het grootste getal is", getal2)
else:
    if getal1 < getal3:
        print("het grootste getal is", getal3)
    else:
        print("het grootste getal is", getal1)
