# Proyecto 2

Integrantes del equipo:  
* Cruz Martínez Raúl  
* Espinosa Cortez Giselle  
* Mendoza Bolaños Carlos Gabriel  
* Navarrete Zamora Aldo Yael  
* Núñez Hernández Diego Ignacio  
* Villanueva Corona Miguel Angel  

## Proceso para la ejecución de los códigos.
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



