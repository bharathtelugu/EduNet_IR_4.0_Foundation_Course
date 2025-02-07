from database import connect, close
def viewContacts():
    dbconn = connect()
    cursor = dbconn.cursor()
    cursor.execute("USE PCMSdb")
    cursor.execute("SELECT * FROM contactsTBL;")
    contacts = cursor.fetchall()
    close(dbconn)
    for contact in contacts:
        print(contact)
