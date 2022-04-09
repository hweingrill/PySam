import sqlite3
import sys


noneToString = lambda text: text or ''

datenbank = "chinook.db"
connection = None

try:
    strSQL = "SELECT" 
    strSQL = strSQL + " AVG(tracks.Milliseconds) AS Durchschnitt"
    strSQL = strSQL + " FROM tracks;"
    
    with sqlite3.connect(datenbank) as connection:
        cursor = connection.cursor()
        cursor.execute(strSQL)
        data = cursor.fetchone()
        print("Der Durchschnitt aller Tracks beträgt: {0:.2f}".format(data[0]))
   
except sqlite3.Error as e:
    print(e)

except IOError:
    print("Die Datei ... konnte nicht geöffnet werden.")
    
except:
    exceptionTupel = sys.exc_info()
    print("Error-Type: ", exceptionTupel[0])
    print("Error-Wert / Beschreibung: ", exceptionTupel[1])
