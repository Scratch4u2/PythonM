lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = []
def parittomat(lista):
    for i in range(2,len(lista) + 1,2):
            lista2.append(i)

parittomat(lista)
print(lista2)