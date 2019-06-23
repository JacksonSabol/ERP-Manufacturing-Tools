# Import dependencies
from mysql.connector import Error
import mysql.connector

# Establish connection to the MySQL database
try:
    connection = mysql.connector.connect(
        host="localhost",
        database='erp_manufacturing_tools',
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
        # Use the cursor to select the database we're connected to
        cursor.execute("select database();")
        # Capture a record of the database we're connected to...
        record = cursor.fetchone()
        # Then print it out
        print("Currently connected to - ", record)
        # Structure our query and values to insert the seeds into the database
        query = "INSERT INTO sales (department_name, amount) VALUES (%s, %s)"
        vals = [
            ("Minor Hardware", 1234.56),
            ("LIDAR", 4321.00),
            ("Cabling", 333.33)
        ]
        # Execute the query - insert multiple values using the executemany method
        cursor.executemany(query, vals)
        # Commit the changes to the database
        connection.commit()
        # Print the number of entries we committed
        print(cursor.rowcount, " records inserted.")
        # Print the ID of the row inserted
        # print("ID of row inserted: ", cursor.lastrowid)
        # Select all entries from the 'sales' table and print them
        cursor.execute("SELECT * FROM sales")
        sales_entries = cursor.fetchall()
        for row in sales_entries:
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