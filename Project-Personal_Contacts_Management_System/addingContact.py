from database import connect, close

def addContact(name, phoneNo, email):
    dbconn = connect()
    cursor = dbconn.cursor()
    cursor.execute("USE PCMSdb")
    cursor.execute("INSERT INTO contactsTBL (name, phoneNo, email) VALUES (%s, %s, %s);", (name, phoneNo, email))
    dbconn.commit()
    close(dbconn)
    print(f"Contact {name} added.")