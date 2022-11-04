import requests
from bs4 import BeautifulSoup
import os
from io import open

def webscraping(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup)
    return soup.find_all('h2')


def crearArchivoyGuardar(rutaArch,url):
    archivo = open(rutaArch, "w")
    soup = webscraping(url)
    count = 0
    for titulos in soup[1:]:
        archivo.write(titulos.text + os.linesep)
    archivo.close()

def principal():
    url = 'https://los40.com/los40/2021/02/18/musica/1613476104_405901.html'
    # rutaArch='/home/ku/1000PPython/1000Programadores/script/modulo5/list_top_16.csv'
    rutaArch='list_top_16.csv'
    crearArchivoyGuardar(rutaArch,url)


principal()