import sqlite3
import sys


def noneToString(text):
    if (text is None):
        return ''
    else:
        return str(text)
    
# noneToString = lambda text: text or ''

datenbank = "chinook.db"
connection = None

try:
    strSQL = "SELECT * FROM customers"
    strSQL = strSQL + " WHERE (Company IS NOT NULL);"
    
    with sqlite3.connect(datenbank) as connection:
        cursor = connection.cursor()
        cursor.execute(strSQL)
        data = cursor.fetchall()

    for zeile in data:
        print(noneToString(zeile[1]) + ' ' + noneToString(zeile[2]))
        print(noneToString(zeile[3]))
        print(noneToString(zeile[4]))
        print(noneToString(zeile[8]) + ' ' + noneToString(zeile[5]) +  ' - ' + noneToString(zeile[6]) + ' - ' + noneToString(zeile[7]))
        print(noneToString(zeile[9]))
        print(noneToString(zeile[10]))
        print('\n')
   
except sqlite3.Error as e:
    print(e)

except IOError:
    print("Die Datei ... konnte nicht geöffnet werden.")
    
except:
    exceptionTupel = sys.exc_info()
    print("Error-Type: ", exceptionTupel[0])
    print("Error-Wert / Beschreibung: ", exceptionTupel[1])
