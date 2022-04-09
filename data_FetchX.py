import sqlite3
import sys


noneToString = lambda text: text or ''

datenbank = "chinook.db"
connection = None

try:
    strSQL = "SELECT" 
    strSQL = strSQL + " albums.Title," 
    strSQL = strSQL + " SUM(tracks.Milliseconds) AS LaengeAlbum" 
    strSQL = strSQL + " FROM tracks" 
    strSQL = strSQL + " INNER JOIN albums" 
    strSQL = strSQL + " ON (tracks.AlbumId = albums.AlbumId)" 	
    strSQL = strSQL + " GROUP BY albums.Title" 
    strSQL = strSQL + " ORDER BY Sum(tracks.Milliseconds) DESC;"

    print(strSQL)
    
    with sqlite3.connect(datenbank) as connection:
        cursor = connection.cursor()
        cursor.execute(strSQL)

        while True:
            data = cursor.fetchmany(3)

            if data is None:
                break

            for zeile in data:
                print("Das Album '{0}' hat eine Laufzeit von {1} Millisekunden".format(zeile[0], zeile[1]))
   
except sqlite3.Error as e:
    print(e)

except IOError:
    print("Die Datei ... konnte nicht geöffnet werden.")
    
except:
    exceptionTupel = sys.exc_info()
    print("Error-Type: ", exceptionTupel[0])
    print("Error-Wert / Beschreibung: ", exceptionTupel[1])
