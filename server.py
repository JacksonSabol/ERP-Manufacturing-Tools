# Import dependencies
from mysql.connector import Error
import mysql.connector

# Establish connecting to MySQL database
try:
    connection = mysql.connector.connect(
        host="localhost",
        database='erp_manufacturing_tools',
        user="root",
        password="password"
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Currently connected to - ", record)
        cursor.execute("SELECT * FROM sales")
        sales_entries = cursor.fetchall()
        for row in sales_entries:
            print(row)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
