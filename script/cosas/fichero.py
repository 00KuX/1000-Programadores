# from io import open

# fichero = open("fichero.txt","r")
# fichero.seek(0)
# # fichero.seek(fichero.readline().find("\n"))
# fichero.seek(open(fichero.readline()))
# t = fichero.read()
# fichero.close()
# print(t)

import csv
 
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")
