import mysql.connector

cnn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='bdEjemplo72'
)


def consulta_ciudades():

    cur = cnn.cursor()
    cur.execute('SELECT * FROM countries')
    datos = cur.fetchall()
    cur.close()
    return datos


def inserta_ciudad(ISO3, CountryName, Capital, CurrencyCode):
    cur = cnn.cursor()
    sql = """INSERT INTO countries(ISO3, CountryName, Capital, CurrencyCode) VALUES('{}','{}','{}','{}')""".format(
        ISO3, CountryName, Capital, CurrencyCode)
    cur.execute(sql)
    n = cur.rowcount
    cnn.commit()
    cur.close()
    return n

#print (inserta_ciudad('MEX','Mexico','CDMX','MXN'))


def elimina_ciudad(Id):
    cur = cnn.cursor()
    sql = '''DELETE FROM countries WHERE Id = {}'''.format(Id)
    cur.execute(sql)
    n = cur.rowcount
    cnn.commit()
    cur.close()
    return n


def modifica_ciudad(Id, ISO3, CountryName, Capital, CurrencyCode):
    cur = cnn.cursor()
    sql ='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}', CurrencyCode='{}' WHERE Id ={}'''.format(ISO3, CountryName, Capital,CurrencyCode, Id)
    cur.execute(sql)
    n = cur.rowcount
    cnn.commit()
    cur.close()
    return n


print(modifica_ciudad(9,'EUA','US','Washington','DLS'))


# print(elimina_ciudad(4))

# print (cnn){}
