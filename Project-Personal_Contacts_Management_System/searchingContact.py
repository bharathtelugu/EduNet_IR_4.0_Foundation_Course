from database import connect, close
def searchContact(name):
    dbconn = connect()
    cursor = dbconn.cursor()
    cursor.execute("USE PCMSdb")
    cursor.execute("SELECT * FROM contactsTBL WHERE name LIKE %s;", ('%' + name + '%',))
    contacts = cursor.fetchall()
    close(dbconn)
    for contact in contacts:
        print(contact)