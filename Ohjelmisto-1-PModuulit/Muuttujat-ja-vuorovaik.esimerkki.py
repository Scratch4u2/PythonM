# muuttuja ja tyyppi
age = 5
print(age)
age = 6
print(age + 2)
# merkkijono
age_string = "seitsemän"
# kokonaisluku
age_int = 6
#ei toimi print(age_string + age_int)

# pluslasku
print(age_int + 4)
# merkkijonojen liittäminen (concantetation)
print (age_string + " vuotta")

#liukuluvut (float(myös double) (ei tarkka niinkuin desimaali)
depth = 10000.0
width = 7_000
area = depth * width
print(area)

#boolean eli true tai false arvo (totuusarvo)(esim, 1(true) tai 0(false))
is_it_true = True
print(is_it_true)

# tyyppimuunnokset (type komento kertoo tyypin(esim print(type(ageInput))
age_input = input("Kuinka vanha olet? \n")
print(age_input)  #tyyppi on string eli "13"

age_int = int(age_input)
new_age = age_int + 1
print("Vuoden päästä olet " +str(new_age)+ " vuotta.")
#tai f-stringillä
print(f"Vuoden päästä olet {new_age} vuotta.")