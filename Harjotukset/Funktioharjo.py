#tehdään funktio, jota käytetään jossain kohtaa koodia (metodi/method)

def funktio1():
    print("Hello")
    print("Moi")

#parametrisoitu funktio
def numeroita(num1, num2):
    #print(f"{num1 + num2}")
    return num1 + num2

sumnum = numeroita(2, 3)
print(f"Summa on: {sumnum}")
