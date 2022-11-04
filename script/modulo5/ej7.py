import os

def contarCantPalabras(rutaArch):
  cant = 0
  with open(rutaArch, newline='') as archivo:  
    for linea in archivo:
        palabras = linea.split(" ")
        print(palabras)
        cant += len(palabras)
        print(cant)

def principal():
    rutaArch ="/home/ku/1000PPython/1000Programadores/script/modulo5/texto.txt"
    contarCantPalabras(rutaArch)

principal()

