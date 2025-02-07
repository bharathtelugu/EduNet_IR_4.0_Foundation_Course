from database import connect, close
def deleteContact(id):
    dbconn = connect()
    cursor = dbconn.cursor()
    cursor.execute("USE PCMSdb")
    cursor.execute("DELETE FROM contactsTBL WHERE id = %s",(id,))
    dbconn.commit()
    close(dbconn)
    print(f"Contact ID {id} deleted.")