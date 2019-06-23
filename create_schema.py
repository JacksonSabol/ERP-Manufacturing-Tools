# Import dependencies
from mysql.connector import Error
import mysql.connector

# Establish connection to the MySQL RDBMS
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    # If connection is successful...
    if connection.is_connected():
        # Get the server information...
        db_Info = connection.get_server_info()
        # And print it to the console.
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
        # Establish a pointer to the connection cursor
        cursor = connection.cursor()
        # Drop any database by the same name we want (if it exists)
        cursor.execute("DROP DATABASE IF EXISTS erp_manufacturing_tools;")
        # Create a database to store our ERP information
        cursor.execute("CREATE DATABASE erp_manufacturing_tools;")
        # Point the cursor to the database
        cursor.execute("USE erp_manufacturing_tools;")
        # Create a 'sales' table in the database
        cursor.execute("CREATE TABLE sales (id int NOT NULL AUTO_INCREMENT, department_name varchar(255) NOT NULL, amount DECIMAL(13,2) NOT NULL, created_at TIMESTAMP default CURRENT_TIMESTAMP, PRIMARY KEY (id));")
        # Check to see if the table was created
        cursor.execute("SHOW TABLES")
        for row in cursor:
            print(row)
# If we run into any exceptions (errors), capture them and print them
except Error as e:
    print("Error while connecting to MySQL", e)
# End the connection once the database and schema have been created
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")