import csv

def crearListadeDiccionarios(rutaArch):
  lista =[]
  with open(rutaArch, newline='') as archivo:  
    reader = csv.reader(archivo)
    for row in reader:
      diccionario = dict([('id',row[0]),('nombre',row[1]),('apellido',row[2]),('nacimiento',row[3])])
      lista.append(diccionario)
  return lista

def mostrarLista(lista):
  for linea in lista:
    print('Nombre y Apellido: {}, {} \t Fecha Nacimiento: {} '.format(linea['nombre'], linea['apellido'],linea['nacimiento']))

def principal():
    nArch ="/home/ku/1000PPython/1000Programadores/script/Modulo5/personas.csv"
    lista = crearListadeDiccionarios(nArch)
    mostrarLista(lista)

principal()