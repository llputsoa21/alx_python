import MySQLdb

try:
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user="username",
        passwd="password",
        db="hbtn_0e_0_usa",
        port=3306
    )
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    
    cursor.execute("GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost' IDENTIFIED BY 'password'")

    # Execute the SQL query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

except MySQLdb.Error as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if db:
        db.close()