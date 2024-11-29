# graficar.py
import numpy as np
import matplotlib.pyplot as plt


# Listas para almacenar los tiempos de ejecución

resultados_768 = []
resultados_512 = []

# Leer resultados de Kyber768
with open("tiempos_MLKEM_768.txt", "r") as f:
    for linea in f:
        resultados_768.append(float(linea.strip()))

# Leer resultados de Kyber512
with open("tiempos_MLKEM_512.txt", "r") as f:
    for linea in f:
        resultados_512.append(float(linea.strip()))

# Suponiendo que el archivo tiene el formato: [encapsulamiento, desencapsulamiento]
tiempos_512 = [resultados_512[0], resultados_512[1]]
tiempos_768 = [resultados_768[0], resultados_768[1]]
print(tiempos_512)
print(tiempos_768)

# Etiquetas para la gráfica
labels = ['Kyber512 Encaps', 'Kyber512 Decaps',
          'Kyber768 Encaps', 'Kyber768 Decaps']

# Graficar los resultados
plt.figure(figsize=(10, 6))
#tiempos=[tiempos_512, tiempos_768]
plt.bar(labels, tiempos_512 + tiempos_768, color=['blue', 'orange', 'green', 'red'])
plt.title('Tiempos Promedios de Encapsulamiento y Desencapsulamiento')
plt.ylabel('Tiempo (segundos)')
plt.grid(axis='y')


plt.show()
