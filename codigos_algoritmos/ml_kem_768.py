from kyber import Kyber768 #Cambiar Kyber768 a Kyber768 para cambiar longitud de la llave
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from timeit import default_timer
import numpy as np

tiemposEncapsulamientoMLKEM = []
tiemposDesencapsulamientoMLKEM = []

def MLKEMkyber(mensaje):
  pk, sk = Kyber768.keygen()

  tiempo_inicial = default_timer()
  c, llave_encapsulada = Kyber768.enc(pk)
  tiempo_final = default_timer()
  tiemposEncapsulamientoMLKEM.append(tiempo_final-tiempo_inicial)

  tiempo_inicial = default_timer()
  llavedesencapsulada = Kyber768.dec(c, sk)
  tiempo_final = default_timer()
  tiemposDesencapsulamientoMLKEM.append(tiempo_final-tiempo_inicial)

  msg=mensaje.encode('utf-8')
  msgPad=pad(msg, 256)

  #Cifrado Simétrico con la llave generada
  AES_ECBcypher=AES.new(llavedesencapsulada, AES.MODE_ECB)

  ciphertext_ld = AES_ECBcypher.encrypt(msgPad)
  descifrado_aes_ld = AES_ECBcypher.decrypt(ciphertext_ld)



with open("vectores.txt") as filevectores:
    for _ in range(5):
       filevectores.seek(0)
       for linea in filevectores:
           linea=linea.rstrip("\n")
           MLKEMkyber(linea)

    prom_encap=np.mean(tiemposEncapsulamientoMLKEM)
    prom_desencap=np.mean(tiemposDesencapsulamientoMLKEM)
    print("El tiempo promedio de encapsulamiento",prom_encap, "en seg")
    print("El tiempo promedio de desencapsulamiento",prom_desencap, "en seg")
    print("El tiempo total aproximado de un intercambio entre Bob y Alice ",prom_encap+prom_desencap, "en seg")
    #returna
    # Guardar los promedios en un archivo
    with open("tiempos_MLKEM_768.txt", "w") as f:
        f.write(f"{prom_encap}\n")
        f.write(f"{prom_desencap}\n")
        f.write(f"{prom_encap+prom_desencap}\n")
