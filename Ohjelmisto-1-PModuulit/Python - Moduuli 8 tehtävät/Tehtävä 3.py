import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def icao_haku(user_input):
    sql = f"SELECT name FROM airport WHERE ident= '{user_input}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result != None:
        return result
    else:
        return None

input1 = icao_haku(input("Ensimmäinen ICAO-kodi: \n"))
input2 = icao_haku(input("Toinen ICAO-kodi: \n"))

if input1 != None or input2 != None:
    koordinaatit1 = (input1[0], input1[1])
    koordinaatit2 = (input2[0], input2[1])

    valimatka = geodesic(koordinaatit1, koordinaatit2).kilometers
    print(f"Lentokenttien välinen välimatka on: {valimatka}")
else:
    print("Virhe: kenttiä ei löytynyt")