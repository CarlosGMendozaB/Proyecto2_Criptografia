# Proyecto 2

Integrantes del equipo:  
* Cruz Martínez Raúl  
* Espinosa Cortez Giselle  
* Mendoza Bolaños Carlos Gabriel  
* Navarrete Zamora Aldo Yael  
* Núñez Hernández Diego Ignacio  
* Villanueva Corona Miguel Angel  

## Proceso para la ejecución de los códigos.
### Nota importante:
Debe seleccionarse la rama master, ya que en ella se encuentra el contenido de este proyecto.

### Clonación del repositorio.
Primeramente, se instala la herramienta de Git dentro de nuestro sistema, ya que nos permitirá extraer herramientas, así como los códigos involucrados del proyecto.  
```bash
sudo apt install git
```
El siguiente paso es realizar una copia del repositorio en el equipo local haciendo uso de manejador de Git. 

```bash
git clone https://github.com/CarlosGMendozaB/Proyecto2_Criptografia/tree/master
```
Se accederá al Directorio del repositorio clonado anteriormente  
```bash
cd ./Proyecto2_Criptografia
```
Se verificará el estado de nuestro repositorio, para visualizar la existencia de algun cambio.  
```bash
git status
```
En ocasiones es necesario indicar a Git el nombre y correo de nuestra cuenta de Github.  
```bash
git config --global user.name fulanito  
git config --global email.name fulanito@email.com
```
Se le asignará un identificador a la rama u origen de nuestro repositorio para facilitar el manejo del repositorio al momento de actualizar.  
```bash
git pull crypto master
```

### Creación de un entorno virtual.
Para no afectar los paquetes instalados en la máquina actual, se propone hacer un venv de Python. Se hace con los siguientes comandos:
```bash  
sudo apt install python3-venv
```
Crear el entorno virtual:
```bash  
python3 -m venv proyecto_2
```
Activación del venv:
```bash  
source ./proyecto_2/bin/activate
```
### Instalación de bibliotecas.
Dentro de los archivos que se clonaron del repositorio, se encuentra "library.sh", el cual contiene todas las bibliotecas y dependencias necesarias para nuestro proyecto. Este archivo tiene como objetivo instalar todas ellas de forma automatizada, de modo que debemos ejecutar el siguiente comando:  
```bash
sudo ./library.sh
```
### Ejecución del código para la matriz de vectores:
Para poder ejecutar los algoritmos es necesario contar con una matriz que almacenará vectores de cadenas que sera la entrada de cada algoritmo.
```bash
python3 vectores_matriz.py
```
### Ejecución de los código con los algoritmos:
Para realizar la ejecución de los códigos deberá ejecutarse el siguiente comando:
```bash
python3 <codigo>
```
Donde codigo debe sustituirse por los siguientes códigos:
- ml_kem.py
- slh-dsa.py
- ml-dsa.py  
_Nota:_ Para hacer uso de la llave de 768 bytes se presenta comentarios para cambios en el código original o esta el código  ml_kem_768.py

### Salir del entorno virtual de Python
Finalmente, tras haber ejecutado los códigos, se debe terminar la ejecución del entorno virtual. Lo anterior se hace con el siguiente comando:
```bash
deactivate
```
