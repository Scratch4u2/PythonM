import math

def hinta(halkaisija_m,eur):
    pinta_ala = (halkaisija_m/2)**2 * math.pi
    return pinta_ala / eur

pizza1_m = float(input("1 Pizzan halkaisija metreinä: \n"))
pizza1_h = float(input("1 Pizzan hinta euroina: \n"))
pizza2_m = float(input("2 Pizzan halkaisija metreinä: \n"))
pizza2_h = float(input("2 Pizzan hinta euroina: \n"))

hinta1 = hinta(pizza1_m,pizza1_h)
hinta2 = hinta(pizza2_m,pizza2_h)

print(f"1 Pizza on {hinta1:.3f} eur/m^2")
print(f"2 Pizza on {hinta2:.3f} eur/m^2")

if hinta1 > hinta2:
    print("Pizza 1 on hinnaltaan parempi")
else:
    print("Pizza 2 on hinnaltaan parempi")

