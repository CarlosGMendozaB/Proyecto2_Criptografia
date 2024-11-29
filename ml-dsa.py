from lattice_cryptography.lm_one_time_sigs import *
from timeit import default_timer
import numpy as np
tiemposFirmadoMLDSAp = []
tiemposVerificacionMLDSAp = []

def MLDSAdifr(mensaje):
  message: str = mensaje

  public_parameters = make_setup_parameters(secpar=256)
  secret_seed, signing_key, verification_key = keygen(pp=public_parameters, num_keys_to_gen=1)[0]

  tiempo_inicial = default_timer()
  signature = sign(pp=public_parameters, otk=(secret_seed, signing_key, verification_key), msg=message)
  tiempo_final = default_timer()
  tiemposFirmadoMLDSAp.append(tiempo_final - tiempo_inicial)

  try:
    tiempo_inicial = default_timer()
    verify(pp=public_parameters, otvk=verification_key, sig=signature, msg=message)
    tiempo_final = default_timer()
    tiemposVerificacionMLDSAp.append(tiempo_final - tiempo_inicial)
  except (ValueError):
    tiemposVerificacionMLDSAp.append(tiempo_final - tiempo_inicial)

with open("vectores.txt") as filevectores:
  for _ in range(5):
    filevectores.seek(0)
    for linea in filevectores:
      linea=linea.rstrip("\n")
      MLDSAdifr(linea)
    
  print("El promedio de firma",np.mean(tiemposFirmadoMLDSAp), "en seg")
  print("El promedio de verificacion",np.mean(tiemposVerificacionMLDSAp), "en seg")
