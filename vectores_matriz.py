import random
import string

vectores=[]
#El archivo se guardo en la carpeta content
def Gen_Cad():
    cadenas = []
    n = 10
    for i in range(101):
        cadena = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
        cadenas.append(cadena)
        n += 1
    return cadenas

cads = Gen_Cad()
nombre_archivo = "vectores.txt"
with open(nombre_archivo, "w") as archivo:
    for i, cadena in enumerate(cads):
        archivo.write(f"{cadena}\n")

for i in range(5):
    for cadena in cads:
        vectores.append(cadena + f" vuelta {i + 1}")
