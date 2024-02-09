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

def icao_haku(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

input1 = icao_haku(input("Ensimmäinen ICAO-kodi: \n").upper())
input2 = icao_haku(input("Toinen ICAO-kodi: \n").upper())

if input1 != None and input2 != None:
    valimatka = geodesic(input1, input2).kilometers
    print(f"Lentokenttien välinen välimatka on: {valimatka:.3f} kilometriä")
else:
    print("Virhe: kenttiä ei löytynyt")