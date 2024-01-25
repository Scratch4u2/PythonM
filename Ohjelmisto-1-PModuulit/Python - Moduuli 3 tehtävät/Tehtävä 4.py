vuosi = int(input("Mikä vuosi: \n"))
##
if vuosi < 100:
    if vuosi % 4 == 0 and vuosi % 100 != 0:
        print(f"Vuosi {vuosi} on karkausvuosi")
    else:
        print(f"Vuosi {vuosi} ei ole karkausvuosi")

elif vuosi >= 100:
    if vuosi % 4 == 0 and vuosi % 400 == 0:
        print(f"Vuosi {vuosi} on karkausvuosi")
    else:
        print(f"Vuosi {vuosi} ei ole karkausvuosi")


