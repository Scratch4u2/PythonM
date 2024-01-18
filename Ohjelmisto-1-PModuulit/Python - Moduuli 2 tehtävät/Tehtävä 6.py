import random

#kolme random numeroa
kolme = random.randint(100, 999)
print(f"{kolme}")

#kolme random numeroa väliltä 1-6
for _ in range(4):
    numero = random.randint(1, 6)
    print(numero, end="")



