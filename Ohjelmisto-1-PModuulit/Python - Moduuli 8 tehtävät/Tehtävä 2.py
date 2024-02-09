import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def kenttatyyppi(user_input):
    sql = f"SELECT type FROM airport WHERE iso_country= '{user_input}' ORDER BY type"
    cursor = connection.cursor()
    cursor.execute(sql)
    rivit = cursor.fetchall()
    montako = {
        "closed": 0,
        "heliport": 0,
        "large_airport": 0,
        "medium_airport": 0,
        "small_airport": 0,
        "seaplane_base": 0,
        "balloonport": 0
    }
    for rivi in rivit:
        tyyppi = rivi[0]
        if tyyppi in montako:
            montako[tyyppi] += 1
    return montako


user_input = input("Anna maakoodi: \n").upper()
kenttatyypit = kenttatyyppi(user_input)
if kenttatyypit != None:
    print(kenttatyypit)
else:
    print("Ei tuloksia")