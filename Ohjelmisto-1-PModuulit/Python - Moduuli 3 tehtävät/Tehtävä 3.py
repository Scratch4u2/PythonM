suku = input("Oletko mies vai nainen?\n").lower()
arvo = float(input("Hemoglobiiniarvo g/l: \n"))

while suku == "mies":
    if 134 <= arvo <= 195:
        print("Normaali arvo")
    elif(arvo < 134):
        print("Alhainen hemoglobiini")
    else:
        print("Korkea hemoglobiini")
    break

while suku == "nainen":
    if 117 <= arvo <= 175:
        print("Normaali arvo")
    elif(arvo < 117):
        print("Alhainen hemoglobiini")
    else:
        print("Korkea hemoglobiini")
    break