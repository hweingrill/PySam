import sqlite3
import sys

datenbank = "chinook.db"
connection = None

try:
    strSQL = "SELECT customers.City, customers.LastName, customers.FirstName"
    strSQL = strSQL + " FROM customers"
    strSQL = strSQL + " ORDER BY customers.City, customers.LastName;"
    
    with sqlite3.connect(datenbank) as connection:
        connection.text_factory = bytes
        cursor = connection.cursor()
        cursor.execute(strSQL)
        data = cursor.fetchall()

    for zeile in data:
        ausgabe = ''
        for element in zeile:
            if (ausgabe != ''):
                ausgabe = ausgabe + " | "
            unicode =  element.decode("utf8", "replace")  
            ausgabe = ausgabe + unicode
        print(ausgabe)
   
except sqlite3.Error as e:
    print(e)

except IOError:
    print("Die Datei ... konnte nicht geöffnet werden.")
    
except:
    exceptionTupel = sys.exc_info()
    print("Error-Type: ", exceptionTupel[0])
    print("Error-Wert / Beschreibung: ", exceptionTupel[1])
