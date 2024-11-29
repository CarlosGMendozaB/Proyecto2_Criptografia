import numpy as np
import matplotlib.pyplot as plt


# Listas para almacenar los tiempos de ejecución

resultados_ml = []
resultados_slh = []

# Leer resultados de Kyber768
with open("tiempos_ML-DSA.txt", "r") as f:
    for linea in f:
        resultados_ml.append(float(linea.strip()))

# Leer resultados de Kyber512
with open("tiempos_SLH-DSA.txt", "r") as f:
    for linea in f:
        resultados_slh.append(float(linea.strip()))

# Suponiendo que el archivo tiene el formato: [encapsulamiento, desencapsulamiento]
ml_dsa = [resultados_ml[0], resultados_ml[1]]
slh_dsa= [resultados_slh[0], resultados_slh[1]]
print(ml_dsa)
print(slh_dsa)


tiempo_total=[resultados_ml[2], resultados_slh[2]]
labels_total= ['ML-DSA Algorithm', 'SLH-DSA Algorithm ']
plt.bar(labels_total, tiempo_total, color=['blue', 'green'])
plt.title('Tiempos Promedios Total de los Algoritmos de Firma Digital')
plt.ylabel('Tiempo (segundos)')
plt.grid(axis='y')

plt.show()
