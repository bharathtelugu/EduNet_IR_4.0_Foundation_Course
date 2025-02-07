import mysql.connector as mysql

def connect():
    dbconn = mysql.connect(host="localhost",user="root",passwd="ck.Bharath73")
    return dbconn

def close(dbconn):
    dbconn.close()