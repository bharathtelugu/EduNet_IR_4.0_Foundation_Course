import mysql.connector as mysql
db = mysql.connect(host="localhost",user="root",passwd="ck.Bharath73")
cursor = db.cursor()

cursor.execute("""CREATE DATABASE IF NOT EXISTS PCMSdb; """)
db.commit()
cursor.close()
db.close()
print("Database created successfully!")