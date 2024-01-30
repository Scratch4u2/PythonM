import random

max_luku = int(input("Maksimi silmäluku: \n"))
heitto = random.randint(1,max_luku)

while heitto < max_luku:
    heitto = random.randint(1,max_luku)
    print(f"Heitto ei {max_luku} ")
if heitto == max_luku:
    print(heitto)
def nopanheitto(max_luku):
    heitto1 = random.randint(1,max_luku)
    print(heitto1)

nopanheitto(max_luku)