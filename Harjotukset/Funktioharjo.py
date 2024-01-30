#tehdään funktio, jota käytetään jossain kohtaa koodia (metodi/method)

def funktio1():
    print("Hello")
    print("Moi")

#parametrisoitu funktio
def numeroita(calc_type,num1, num2):
    #print(f"{num1 + num2}")
    if calc_type == "add":
        return num1 + num2
    elif calc_type == "multiply":
        return num1 * num2
    return "No calculation type"

sumnum = numeroita(input("Calc type:\n"),2, 3)
print(f"Sum: {sumnum}")
