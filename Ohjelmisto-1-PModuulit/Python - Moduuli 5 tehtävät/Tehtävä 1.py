import random
nopat = int(input("Noppeien lukumäärä: \n"))
noppa_summa = 0
for i in range(nopat):
    noppa_summa = noppa_summa + random.randint(1,6)
    i += 1
print(noppa_summa)
