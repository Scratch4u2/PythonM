import random

heitto = random.randint(1,6)

while heitto != 6:
    heitto = random.randint(1,6)
    print("Heitto ei 6")
if heitto == 6:
    print(heitto)
def nopanheitto():
    heitto1 = random.randint(1,6)
    print(heitto1)

nopanheitto()