from pyspx import shake_128f as slh
import os
import random
from timeit import default_timer
import numpy as np

tiemposFirmadoSLHDSAp = []
tiemposVerificacionSLHDSAp = []

def SLHDSAdifr(mensaje):

  message_plain: str = mensaje
  message_bytes = message_plain.encode("utf-8")
  seed = os.urandom(slh.crypto_sign_SEEDBYTES)

  public_key, secret_key = slh.generate_keypair(seed)

  tiempo_inicial = default_timer()
  signature = slh.sign(message_bytes, secret_key)
  tiempo_final = default_timer()
  tiemposFirmadoSLHDSAp.append(tiempo_final - tiempo_inicial)

  try:
    tiempo_inicial = default_timer()
    pypsx = slh.verify(message_bytes, signature, public_key)
    tiempo_final = default_timer()
    tiemposVerificacionSLHDSAp.append(tiempo_final - tiempo_inicial)
  except (ValueError):

        tiemposVerificacionSLHDSAp.append(tiempo_final - tiempo_inicial)
        print("Firma Invalida")



with open("vectores.txt") as filevectores:
  for _ in range(5):
    filevectores.seek(0)
    for linea in filevectores:
      linea=linea.rstrip("\n")
      SLHDSAdifr(linea)
  
  prom_firma=np.mean(tiemposFirmadoSLHDSAp)
  prom_ver=np.mean(tiemposVerificacionSLHDSAp)
  print("Firmas validas")
  print("El tiempo promedio de firma",prom_firma, "en seg")
  print("El tiempo promedio de verificacion",prom_ver, "en seg")
  print("El tiempo total aproximado del algoritmo ML-DSA: ", prom_firma+prom_ver, "en seg")
  with open("tiempos_SLH-DSA.txt", "w") as f:
        f.write(f"{prom_firma}\n")
        f.write(f"{prom_ver}\n")
        f.write(f"{prom_firma+prom_ver}\n")
  
