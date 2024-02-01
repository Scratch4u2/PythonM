"""lista1 = ["John", 1,5,3,1,"John",True,"John"]
lista2 = []

for item in lista1:
    if type(item) == bool or item not in lista2:
        lista2.append(item)

print(lista2)"""

lista = [1,2,3,5]
lista1 = [4,[6,8],9]
lista2 = []

lista2.extend(lista)
lista2.extend(lista1)
print(lista2[5][1])