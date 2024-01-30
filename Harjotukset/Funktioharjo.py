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
#sumnum = numeroita(input("Calc type:\n"),2, 3)
#print(sumnum)

def numeroita_list(calctype,numbers):
    #print(f"{num1 + num2}")
    if calctype == "add":
        numsum = sum(numbers)
        return numsum
    elif calctype == "multiply":
        nummul = 1
        for i in numbers:
            nummul = nummul * i
        return nummul
    return "No calculation type"

#print(numeroita_list("add", [1,2,3,4]))
#print(numeroita_list("multiply", [1,2,3,4]))

#lista parametrina
inventory = ["kynä", "kumi"]
def add_to_reppu(item, new_inventory):
    new_inventory.append(item)
    print(f"Added {item} to inventory")
    return new_inventory

updated_inventory = add_to_reppu("Penaali", inventory)

inventory.append("Hiiri")
print(inventory)
print(updated_inventory)