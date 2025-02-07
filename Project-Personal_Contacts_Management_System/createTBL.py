import mysql.connector  as mysql

dbconn = mysql.connect(host="localhost",user="root",passwd="ck.Bharath73")
cursor =dbconn.cursor()
cursor.execute("USE PCMSdb;")
cursor.execute("""CREATE TABLE IF NOT EXISTS contactsTBL (
               id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(50) NOT NULL, 
               phoneNo VARCHAR(20) NOT NULL,
               email VARCHAR(50));""")
cursor.execute("SHOW TABLES;")
print(cursor.fetchall())
dbconn.commit()
cursor.close()
dbconn.close()
