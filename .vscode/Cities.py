
import mysql.connector


class Cities:
    def __init__(self):
        self.cnn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=" ",
        database="bdEjemplo72")
    
    def __str(self):
        datos=self.consulta_ciudades() 
        aux = " "  
        for row in datos:
            aux=aux+str(row)+ "\n"
        return aux

    def consulta_ciudades(self):
        cur = self.cnn.cursor()
        cur.execute('SELECT * FROM countries')
        datos = cur.fetchall()
        cur.close()
        return datos

    def inserta_ciudad(self, Id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO countries (ISO3, CountryName, Capital, CurrencyCode) 
        VALUES('{}', '{}', '{}', '{}')'''.format(ISO3, CountryName, Capital, CurrencyCode)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n


    def elimina_ciudad(self,Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM countries WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n


# https://youtu.be/qBv8g1xpgbk?list=PLqlQ2-9ypflT5Lx864RXtJx4s7i3sxgs0&t=815