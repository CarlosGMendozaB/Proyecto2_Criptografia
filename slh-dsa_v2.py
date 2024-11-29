import pyspx
from timeit import default_timer
import numpy as np

tiemposFirmadoSLHDSAp = []
tiemposVerificacionSLHDSAp = []
validacion = []

def SLHDSAdifr(message):
    # Generar claves
    sk, pk = pyspx.keygen()

    # Mensaje a firmar
    #message = b"Este es un mensaje para firmar."

    # Firmar el mensaje
    tiempo_inicial = default_timer()
    signature = pyspx.sign(sk, message)
    tiempo_final = default_timer()
    tiemposFirmadoSLHDSAp.append(tiempo_final - tiempo_inicial)
    #print("Firma generada:", signature)

    # Verificar la firmaa
    tiempo_inicial = default_timer()
    is_valid = pyspx.verify(pk, signature, message)
    tiempo_final = default_timer()
    tiemposVerificacionSLHDSAp.append(tiempo_final - tiempo_inicial)
    if is_valid:
        validacion.append("1")
       # print("La firma es válida.")
    else:
        print("La firma es inválida.")

with open("vectores.txt") as filevectores:
  for _ in range(5):
    filevectores.seek(0)
    for linea in filevectores:
      linea=linea.rstrip("\n")
      SLHDSAdifr(linea)
  prom_firma=np.mean(tiemposFirmadoSLHDSAp)
  prom_ver=np.mean(tiemposVerificacionSLHDSAp)
  print("El tiempo promedio de firma",prom_firma, "en seg")
  print("El tiempo promedio de verificacion",prom_ver, "en seg")
  print("El tiempo total aproximado del algoritmo ML-DSA: ", prom_firma+prom_ver, "en seg")
  if validacion.count('1') == "505":
    print(validacion.count('1'))
    print("Firmas validas")
  else:
    print("Existe alguna firma invalida")

  with open("tiempos_SLH-DSA.txt", "w") as f:
        f.write(f"{prom_firma}\n")
        f.write(f"{prom_ver}\n")
        f.write(f"{prom_firma+prom_ver}\n")
