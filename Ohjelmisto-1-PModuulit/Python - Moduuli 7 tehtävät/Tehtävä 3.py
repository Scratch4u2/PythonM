kysely = input("Haluatko syöttää uuden lentokentän, hakea olemassaolevan tietoja tai lopettaa (uusi, haku, stop): \n")
lentokentat = {"EFHK":"Helsinki-Vantaa",
"KJFK":"John F. Kennedy International Airport",
"KLAX":"Los Angeles International Airport",
"EGLL":"London Heathrow Airport",
"RJTT":"Tokyo Haneda Airport",
"OMDB":"Dubai International Airport",
"ZBAA":"Beijing Capital International Airport",
"EDDF":"Frankfurt am Main Airport",
"EHAM":"Amsterdam Airport Schiphol",
"YSSY":"Sydney Kingsford Smith Airport"
}

while kysely != "stop":
    if kysely == "uusi":
        icao = input("ICAO-koodi: \n")
        nimi = input("Lentokentän nimi: \n")
        lentokentat[icao] = nimi
    elif kysely == "haku":
        avain = input("ICAO-koodi: ")
        if avain in lentokentat:
            print(lentokentat[avain])
        else:
                print(f"{avain}-koodilla ei löytynyt lentokenttää")
    kysely = input("Haluatko syöttää uuden lentokentän, hakea olemassaolevan tietoja tai lopettaa (uusi, haku, stop): \n")