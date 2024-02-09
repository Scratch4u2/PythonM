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
    sql = f"SELECT type FROM airport WHERE iso_country= '{user_input}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount:
        return result

user_input = input("Anna maakoodi: \n").upper()
airport = find_country_by_code(user_input)
if airport != None:
    print(airport)
else:
    print("Ei tuloksia")