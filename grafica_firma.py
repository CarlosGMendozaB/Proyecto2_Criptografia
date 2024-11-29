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

# Etiquetas para la gráfica
labels = ['ML-DSA Signature', 'ML-DSA Verification',
          'SLH-DSA Signature', 'SLH-DSA Verification']

# Graficar los resultados
plt.figure(figsize=(10, 6))
#tiempos=[tiempos_512, tiempos_768]
plt.bar(labels,  ml_dsa + slh_dsa, color=['blue', 'orange', 'green', 'red'])
plt.title('Tiempos Promedios de Firma y Verificacion')
plt.ylabel('Tiempo (segundos)')
plt.grid(axis='y')


plt.show()
