leiviskä = float(input("Leiviskät.\n"))
naulat = float(input("Naulat. \n"))
luodit = float(input("Luodit. \n"))

paino = 13.3 * (luodit + (naulat * 32 + (leiviskä * 20 * 32)))

print("Massa nykymittojen mukaan: " + str(int(paino // 1000)) + "kiloa ja " + str(int(paino % 1000)) + "grammaa")
