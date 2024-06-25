import time

from Algotirmo_A import palPart
from Algoritmo_B import minCutDP

def leer_palabras(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        # Leer el contenido del archivo
        contenido = file.read()
        # Reemplazar las comas por espacios y dividir por espacios y saltos de línea
        palabras = contenido.replace(',', ' ').split()

        print (palabras)
    return palabras

# leer una palabra

palabras = leer_palabras('palabras.txt')

file_path = "tiempos.csv"
with open(file_path, 'w') as file:
    file.writelines("Palabra;Largo de la Palabra;Tiempo A[s];Tiempo B[s]\n")


    for palabra in palabras:
        n = len(palabra)

        # Algoritmo A
        start = time.time()
        palPart(palabra)
        end = time.time()

        tiempo_A = end - start

        # Algoritmo A
        start = time.time()
        minCutDP(palabra)
        end = time.time()

        tiempo_B = end - start


        print("Tiempo A: ", tiempo_A, "seg\t Tiempo B:", tiempo_B)

        file.writelines(palabra + ';' + str(n) + ';' + str(tiempo_A) + ';' + str(tiempo_B) + '\n')


print("Archivo " + file_path + " Creado con Exito.")
