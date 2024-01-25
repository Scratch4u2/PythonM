luku = input("Anna luku\n")
korkein = float(luku)
pienin = float(luku)
while luku != "":
    luku = float(luku)
    if luku < pienin:
        pienin = luku
    elif luku > korkein:
        korkein = luku
    luku = input("Anna luku\n")
print(f"Pienin luku {pienin}")
print(f"Suurin luku {korkein}")
