import math
import random
a_maara = 0

piste_maara = int(input("Pisteiden määrä?\n"))
maara = 0

while maara < piste_maara:
    koordinaatti1 = random.uniform(-1,1)
    koordinaatti2 = random.uniform(-1, 1)
    if koordinaatti1**2 + koordinaatti2**2 < 1 :
        a_maara += 1
    maara += 1
    if maara == piste_maara:
        break

likarvo = (4*a_maara) / piste_maara
print(likarvo)