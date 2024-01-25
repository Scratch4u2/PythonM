import random
number = random.randint(1,10)
user_number = int(input("Arvaa numero\n"))
while user_number != number:
    if user_number > number:
        print("Liian suuri luku")
        user_number = int(input("Arvaa numero\n"))
    elif user_number < number:
        print("Liian pieni luku")
        user_number = int(input("Arvaa numero\n"))
print("Oikein!")