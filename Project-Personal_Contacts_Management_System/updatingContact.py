from database import connect, close
def updateContact(id, name, phoneNo, email):
    dbconn = connect()
    cursor = dbconn.cursor()
    cursor.execute("USE PCMSdb")
    cursor.execute("UPDATE contactsTBL SET name = %s, phoneNo = %s, email = %s WHERE id = %s", (name, phoneNo, email, id))
    dbconn.commit()
    close(dbconn)
    print(f"Contact ID {id} updated.")