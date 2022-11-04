from io import open
texto = "Una línea con texto\nOtra línea con textoooooooo"
# Ruta donde se crea el fichero, w indica escritura (puntero al principio)
fichero = open('fichero.txt','  ')
# Escribimos el texto
fichero.write(texto)
# Cerramos el fichero
fichero.close()