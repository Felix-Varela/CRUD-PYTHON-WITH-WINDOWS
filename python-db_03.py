import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", 
passwd="admin", database="bdEjemploPy")

def consulta_ciudades():
    cur = cnn.cursor()
    cur.execute("SELECT * FROM countries")
    datos = cur.fetchall()
    cur.close()    
    return datos


