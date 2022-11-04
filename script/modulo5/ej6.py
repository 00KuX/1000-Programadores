#Buscando ejemplos en la web, esta importacion no esta presente. 
#IMPORTANTE, de otro modo "open" no funciona.
from io import open 
import csv

with open('personas.csv', 'r',newline='') as myFile:
    readersito = csv.reader(myFile)
    sortedlist = sorted(readersito, key=lambda row: row[1], reverse=False)
    for row in sortedlist:
        print(row) # esto es una lista
print("readersito completooo")
