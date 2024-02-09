nimi = input("Anna nimi (Tyhjä merkkijono lopettaa kyselyn): \n")
nimet = set()
while nimi !="":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
    nimi = input("Anna nimi (Tyhjä merkkijono lopettaa kyselyn): \n")
print(nimet)