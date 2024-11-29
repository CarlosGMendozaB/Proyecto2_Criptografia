from lattice_cryptography.lm_one_time_sigs import *
from timeit import default_timer
import numpy as np

tiemposFirmadoMLDSAp = []
tiemposVerificacionMLDSAp = []
validacion = []

def MLDSAdifr(message):
    # Configuración de parámetros
    public_parameters = make_setup_parameters(secpar=256)

    # Generar claves
    secret_seed, signing_key, verification_key = keygen(pp=public_parameters, num_keys_to_gen=1)[0]

    # Mensaje a firmar
    #message = "Este es un mensaje para firmar."

    # Firmar el mensaje
    tiempo_inicial = default_timer()
    signature = sign(pp=public_parameters, otk=(secret_seed, signing_key, verification_key), msg=message)
    tiempo_final = default_timer()
    tiemposFirmadoMLDSAp.append(tiempo_final - tiempo_inicial)
    #print("Firma generada:", signature)

    # Verificar la firma
    tiempo_inicial = default_timer()
    is_valid = verify(pp=public_parameters, otvk=verification_key, sig=signature, msg=message)
    tiempo_final = default_timer()
    tiemposVerificacionMLDSAp.append(tiempo_final - tiempo_inicial)
    if is_valid:
        validacion.append("1")
        #print("La firma es válida.")
    else:
        validacion.append("0")
        print("La firma es inválida.")

with open("vectores.txt") as filevectores:
  for _ in range(5):
    filevectores.seek(0)
    for linea in filevectores:
      linea=linea.rstrip("\n")
      MLDSAdifr(linea)
  prom_firma= np.mean(tiemposFirmadoMLDSAp)
  prom_ver= np.mean(tiemposVerificacionMLDSAp)
  print("El tiempo promedio de firma",prom_firma, "en seg")
  print("El tiempo promedio de verificacion",prom_ver, "en seg")
  print("El tiempo total aproximado del algoritmo ML-DSA: ", prom_firma+prom_ver, "en seg")
  print(validacion.count('1'))
  if validacion.count('1') == "505":
    print(validacion.count('1'))
    print("Firmas validas")
  else:
    print("Existe alguna firma invalida")
  #print("El tiempo tota aproximado de un intercambio entre Bob y Alice ",tiemposEncapsulamientoMLKEM[0]+tiemposDesencapsulamientoMLKEM[0], "en seg")
   # Guardar los promedios en un archivo
 # with open("tiempos_ML-DSA.txt", "w") as f:
  #      f.write(f"{prom_firma}\n")
   #     f.write(f"{prom_ver}\n")
    #    f.write(f"{prom_firma+prom_ver}\n")

