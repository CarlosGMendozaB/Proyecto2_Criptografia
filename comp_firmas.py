import numpy as np
import matplotlib.pyplot as plt
from algoritmo import algorithm_1, algorithm_2  # Importar las funciones del otro script

# Definimos el tamaño de la entrada
n_values = np.arange(1, 1001, 10)  # De 1 a 1000, con un paso de 10

# Listas para almacenar los tiempos de ejecución
time_algorithm_1 = []
time_algorithm_2 = []

# Medimos el tiempo de ejecución para ambos algoritmos
for n in n_values:
    time_algorithm_1.append(algorithm_1(n))
    time_algorithm_2.append(algorithm_2(n))

# Graficamos los resultados
plt.figure(figsize=(10, 5))
plt.plot(n_values, time_algorithm_1, label='Algoritmo 1 (Bucle)', marker='o')
plt.plot(n_values, time_algorithm_2, label='Algoritmo 2 (Fórmula de Gauss)', marker='x')
plt.title('Comparación de Tiempos de Ejecución')
plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid()
plt.show()
