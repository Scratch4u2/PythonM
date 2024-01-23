#While silmukat (loopit)

#jakolaskukone
num1 = float(input("Anna jaettava \n"))
num2 = float(input("Anna jakaja \n"))

while num2 == 0:
    print("Jakaja ei voi olla nolla")
    num2 = float(input("Anna jakaja \n"))

result = num1 / num2

print(f"Jakolaskun tulos on: {result:.2f} ")


#iteraatio (laskuri toistokertojen määrittelyä varten)

i = 1
while i < 11:
    print(f"Numero on {i}")
    i = i + 1
print(f"Lopullinen i:n arvo silmukan lopussa on {i}")
print(i == i + 1)