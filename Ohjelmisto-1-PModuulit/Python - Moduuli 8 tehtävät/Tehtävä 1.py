import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def icao_haku(user_iput1):
    sql = f"SELECT name FROM airport WHERE ident= '{user_input1}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result
user_input1 = input("Anna ICAO-koodi: \n").upper()
airport = icao_haku(user_input1)
if airport != None:
    print(airport)
else:
    print("Ei tuloksia")