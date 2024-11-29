# graficar.py
import numpy as np
import matplotlib.pyplot as plt
#from ml_kem import mensaje# MLKEMkyber   Importar el primer algoritmo
#from ml_kem_768 import mensaje_768#MLKEMkyber_768   Importar el segundo algoritmo

# Definimos el tamaño de la entrada
n_values = np.arange(1, 1001, 10)  # De 1 a 1000, con un paso de 10

# Listas para almacenar los tiempos de ejecución
time_encap_algorithm_1 = []
time_encap_algorithm_2 = []
time_desencap_algorithm_1 = []
time_desencap_algorithm_2 = []

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
tiempos_512 = [resultados_512[0], resultados_512[1], resultados_512[2]]
tiempos_768 = [resultados_768[0], resultados_768[1], resultados_768[2]]
print(tiempos_512[2])
print(tiempos_768[2])

tiempo_total=[resultados_512[2], resultados_768[2]]
labels_total= ['ML-KEM Kyber512 ', 'KML-KEM Kyber768 ']
plt.bar(labels_total, tiempo_total, color=['blue', 'green'])
#plt.figure(figsize=(10, 6))
plt.title('Tiempos Promedios Total del algoritmo ML-KEM')
plt.ylabel('Tiempo (segundos)')
plt.grid(axis='y')

plt.show()
