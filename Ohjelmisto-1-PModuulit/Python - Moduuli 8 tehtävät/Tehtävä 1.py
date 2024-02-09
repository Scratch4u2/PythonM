import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def find_country_by_code(iso_code):
    sql = f"SELECT name FROM airport WHERE ident= '{user_input1}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result
user_input1 = input("Anna ICAO-koodi: \n").upper()
airport = find_country_by_code(user_input1)
if airport != None:
    print(airport)
else:
    print("Ei tuloksia")